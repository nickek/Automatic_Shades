import time
import csv
import os
import sys
from datetime import datetime
from time import sleep

from PySide2.QtCore import Qt, QCoreApplication, QTimer, Signal, Slot, QObject, QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QStackedWidget, QVBoxLayout, QWidget

from mainwindow_ui import Ui_MainWindow as ui
from motor_control import Motor
from ultrasonic_sensor import Ultrasonic
import sensor_read

class Worker(QObject):
    temperature_updated = Signal(float)
    motor_status_updated = Signal(str)
    finished = Signal()
    
    def __init__(self, user_preferences, counters, motor, parent=None):
        super(Worker, self).__init__(parent)
        self.user_preferences = user_preferences
        self.counters = counters
        self.motor = motor
        self.i = 0
        self.lux = 0
        self.resistance = 0
        self.tempf = 0
        self.tempc = 0
        self.motor_status = {'status': 'Open'}
        self.is_running = True
        self.auto_enabled = True
        self.paused = False
        
    def run(self):
        while self.is_running:
            if not self.paused:
                if self.i < 6:
                    light, temp = sensor_read.sensorValues()
                    print(self.i)
                    self.lux += light['lux']
                    self.resistance += light['resistance']
                    self.tempf += temp['tempf']
                    self.tempc += temp['tempc']
                    self.i += 1
                    sleep(0.2)  # Simulate some delay in the loop
                else:
                    self.process_data()
                    self.i = 0
                    self.lux = 0
                    self.resistance = 0
                    self.tempf = 0
                    self.tempc = 0
                    sleep(1)  # Interval before starting the next cycle

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def process_data(self):
        self.lux /= 6
        self.resistance /= 6
        self.tempf /= 6
        self.tempc /= 6

        self.lux = round(self.lux, 2)
        self.resistance = round(self.resistance, 2)
        self.tempf = round(self.tempf, 2)
        self.tempc = round(self.tempc, 2)

        # Calibrate Fahrenheit
        self.tempf -= 5
        self.tempc -= 2.5

        current_time = datetime.now().strftime("%H:%M:%S")
        data = {'time': current_time, 'lux': self.lux, 'resistance': self.resistance, 'tempf': self.tempf, 'tempc': self.tempc, 'top distance': self.motor.top_dist, 'bot distance': self.motor.bot_dist}
        saveCSV('blinds_data.csv', data)
        
        autoBlinds(data, self.user_preferences, self.counters, self.motor, self.motor_status)
        print('---------------------------------')
        print(f'Lux value: {self.lux:.2f}, Resistance value: {self.resistance:.2f}')
        print(f'Temperature: {self.tempf:.2f} F, {self.tempc:.2f} C')
        print(f'Motor Status: {self.motor_status["status"]}')
        print(f'Auto Status: {self.auto_enabled}')
        print(f'User Preferences: {self.user_preferences["value"]} F')

        # Emit signals to the QT GUI
        self.temperature_updated.emit(self.tempf)
        self.motor_status_updated.emit(self.motor_status['status'])

    def stop(self):
        self.is_running = False
        
    @Slot(bool)
    def set_auto_control_enabled(self, enabled):
        print(f"Auto control enabled set to: {enabled}")
        self.auto_enabled = enabled
    
    @Slot(float)
    def update_temperature_preference(self, value):
        self.user_preferences['value'] = value
        print(f"User temperature preference updated to: {value}")
    
    
class MainWindow(QMainWindow):
    open_shades_request = Signal()
    close_shades_request = Signal()
    auto_control_enabled = Signal(bool)
    temperature_preference_changed = Signal(float)
    open_shades_increment = Signal()
    close_shades_increment = Signal()
    
    def __init__(self):
        super().__init__()
        # Initialize the UI
        self.ui = ui()
        self.ui.setupUi(self)

        # Connect tab buttons to functions
        self.ui.button_home.clicked.connect(self.show_home)
        self.ui.button_control.clicked.connect(self.show_control)
        self.ui.button_settings.clicked.connect(self.show_settings)

        # Connect shade control buttons to functions
        self.ui.pushButton_control_open.clicked.connect(self.request_open_shades)
        self.ui.pushButton_control_close.clicked.connect(self.request_close_shades)
        self.ui.pushButton_control_up.clicked.connect(self.move_up)
        self.ui.pushButton_control_down.clicked.connect(self.move_down)

        # Connect sliders to functions
        self.ui.horizontalSlider_settings_temperature.valueChanged.connect(self.manage_user_preferences)
        # Initialize tab contents
        self.home_widget = QWidget()
        self.home_layout = QVBoxLayout(self.home_widget)
        self.home_layout.addWidget(QLabel("Home Tab Contents"))

        self.control_widget = QWidget()
        self.control_layout = QVBoxLayout(self.control_widget)
        self.control_layout.addWidget(QLabel("Control Tab Contents"))

        self.settings_widget = QWidget()
        self.settings_layout = QVBoxLayout(self.settings_widget)
        self.settings_layout.addWidget(QLabel("Settings Tab Contents"))

        self.ui.stackedWidget.addWidget(self.home_widget)
        self.ui.stackedWidget.addWidget(self.control_widget)
        self.ui.stackedWidget.addWidget(self.settings_widget)
        
        self.set_manual_controls_enabled(True)
        self.ui.auto_man_switch.stateChanged.connect(self.toggle_auto_manual)
    
    def toggle_auto_manual(self, state):
        if state == Qt.Checked:
            self.ui.auto_man_switch.setText("Automatic")
            self.set_manual_controls_enabled(False)
            self.auto_control_enabled.emit(True)
        else:
            self.ui.auto_man_switch.setText("Manual")
            self.set_manual_controls_enabled(True)
            self.auto_control_enabled.emit(False)

    def set_manual_controls_enabled(self, enabled):
        self.manual_controls_enabled = enabled
        self.ui.pushButton_control_open.setEnabled(enabled)
        self.ui.pushButton_control_close.setEnabled(enabled)
        self.ui.pushButton_control_up.setEnabled(enabled)
        self.ui.pushButton_control_down.setEnabled(enabled)

    def show_home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_control(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_settings(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def request_open_shades(self):
        self.open_shades_request.emit()

    def request_close_shades(self):
        self.close_shades_request.emit()

    def move_up(self):
        # Function to move shades up
        print("Moving shades up")
        self.open_shades_increment.emit()

    def move_down(self):
        # Function to move shades downauto_control_enabled = Signal(bool)
        print("Moving shades down")
        self.close_shades_increment.emit()
    
    def manage_user_preferences(self, value):
        print(f"Emitting temperature preference change: {value}")
        self.temperature_preference_changed.emit(value)
    
    @Slot(float)
    def change_temperature(self, value):
        self.ui.label_home_temperature.setText(QCoreApplication.translate("MainWindow", f"Temperature: {value} F", None))

    @Slot(str)
    def update_motor(self, value):
        self.ui.label_home_status.setText(QCoreApplication.translate("MainWindow", f"Status: {value}", None))
        self.ui.label_control_status.setText(QCoreApplication.translate("MainWindow", f"Status: {value}", None))

    def change_speed(self, value):
        # Function to handle speed slider changes
        print(f"Speed slider value changed to: {value}")

class MainApp(QObject):
    def __init__(self, user_preferences, counters, motor, window):
        super(MainApp, self).__init__()
        self.user_preferences = user_preferences
        self.counters = counters
        self.motor = motor

        self.worker = Worker(user_preferences, counters, motor)
        self.worker_thread = QThread()

        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        # Connect signals to the window's slots
        self.worker.temperature_updated.connect(window.change_temperature)
        self.worker.motor_status_updated.connect(window.update_motor)
        window.open_shades_request.connect(self.handle_open_shades_request)
        window.close_shades_request.connect(self.handle_close_shades_request)
        window.open_shades_increment.connect(self.increment_open_shades)
        window.close_shades_increment.connect(self.increment_close_shades)
        window.auto_control_enabled.connect(self.worker.set_auto_control_enabled)
        window.temperature_preference_changed.connect(self.worker.update_temperature_preference)
        self.worker_thread.start()
    
    def increment_open_shades(self):
        self.worker.pause()
        if self.worker.motor_status['status'] != 'Open':
            self.worker.motor.incrementC()
            print(self.worker.motor.u.distance())
            if self.worker.motor.u.distance() >= self.worker.motor.dist:
                self.worker.motor_status['status'] = 'Open'
                self.worker.motor_status_updated.emit(self.worker.motor_status['status'])
        else:
            print("Shades are already open")
        self.worker.resume()
        
    def increment_close_shades(self):
        self.worker.pause()
        if self.worker.motor_status['status'] != 'Close':
            self.worker.motor.incrementCC()
            print(self.worker.motor.u.distance())
            if self.worker.motor.u.distance() < 10:
                self.worker.motor_status['status'] = 'Close'
                self.worker.motor_status_updated.emit(self.worker.motor_status['status'])
        else:
            print("Shades are already close")
        self.worker.resume()
        
    def handle_open_shades_request(self):
        self.worker.pause()
        if self.worker.motor_status['status'] != 'Open':
            print("Opening shades")
            self.worker.motor.spinC()
            self.worker.motor_status['status'] = 'Open'
            self.worker.motor_status_updated.emit(self.worker.motor_status['status'])
        else:
            print("Shades are already open")
        self.worker.resume()

    def handle_close_shades_request(self):
        self.worker.pause()
        if self.worker.motor_status['status'] != 'Close':
            print("Closing shades")
            self.worker.motor.spinCC()
            self.worker.motor_status['status'] = 'Close'
            self.worker.motor_status_updated.emit(self.worker.motor_status['status'])
        else:
            print("Shades are already closed")
        self.worker.resume()

def saveCSV(filename, data):
    # Check if the file exists
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['time', 'lux', 'resistance', 'tempf', 'tempc', 'top distance', 'bot distance'])

        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

def autoBlinds(data, user_preferences, counters, motor, motor_status):
    temperature_read = data[user_preferences['temperature']]
    lux_read = data['lux']
    user_temperature = user_preferences['value']
    print("Checking state of blinds...")

    if temperature_read < user_temperature:
        if lux_read >= 500:
            counters['open'] += 1
            print(f'Adding counter to open: {counters["open"]}')
    else:
        counters['close'] += 1
        print(f'Adding counter to close: {counters["close"]}')

    if counters['open'] >= 5:
        print("Opening blinds!")
        motor.spinC()
        counters['open'] = 0
        counters['close'] = 0
        motor_status['status'] = 'Open'

    if counters['close'] >= 5:
        print("Closing blinds!")
        motor.spinCC()
        counters['open'] = 0
        counters['close'] = 0
        motor_status['status'] = 'Close'

def main():
    user_preferences = {'temperature': 'tempf', 'value': 75.0}

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    counters = {'open': 0, 'close': 0}
    motor = Motor(17, 27, 22)

    main_app = MainApp(user_preferences, counters, motor, window)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
