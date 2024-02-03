from mainwindow_ui import Ui_MainWindow as ui
import sys
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QStackedWidget, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
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
        self.ui.pushButton_control_open.clicked.connect(self.open_shades)
        self.ui.pushButton_control_close.clicked.connect(self.close_shades)
        self.ui.pushButton_control_up.clicked.connect(self.move_up)
        self.ui.pushButton_control_down.clicked.connect(self.move_down)

        # Connect sliders to functions
        self.ui.horizontalSlider_settings_temperature.valueChanged.connect(self.change_temperature)
        self.ui.horizontalSlider_settings_speed.valueChanged.connect(self.change_speed)

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

    def show_home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_control(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_settings(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def open_shades(self):
        # Function to open shades
        print("Opening shades")
        self.ui.label_home_status.setText(QCoreApplication.translate("MainWindow", u"Status: Open", None))
        self.ui.label_control_status.setText(QCoreApplication.translate("MainWindow", u"Status: Open", None))

    def close_shades(self):
        # Function to close shades
        print("Closing shades")
        self.ui.label_home_status.setText(QCoreApplication.translate("MainWindow", u"Status: Close", None))
        self.ui.label_control_status.setText(QCoreApplication.translate("MainWindow", u"Status: Close", None))

    def move_up(self):
        # Function to move shades up
        print("Moving shades up")

    def move_down(self):
        # Function to move shades down
        print("Moving shades down")

    def change_temperature(self, value):
        # Function to handle temperature slider changes
        print(f"Temperature slider value changed to: {value}")
        self.ui.label_home_temperature.setText(QCoreApplication.translate("MainWindow", f"Temperature: {value}", None))

    def change_speed(self, value):
        # Function to handle speed slider changes
        print(f"Speed slider value changed to: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())