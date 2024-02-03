# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(150, 0))
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_home = QPushButton(self.frame_top)
        self.button_home.setObjectName(u"button_home")
        font = QFont()
        font.setPointSize(16)
        self.button_home.setFont(font)
        self.button_home.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.horizontalLayout.addWidget(self.button_home)

        self.button_control = QPushButton(self.frame_top)
        self.button_control.setObjectName(u"button_control")
        self.button_control.setFont(font)
        self.button_control.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.horizontalLayout.addWidget(self.button_control)

        self.button_settings = QPushButton(self.frame_top)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setFont(font)
        self.button_settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.horizontalLayout.addWidget(self.button_settings)


        self.verticalLayout_10.addWidget(self.frame_top)

        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.page_1_home = QWidget()
        self.page_1_home.setObjectName(u"page_1_home")
        self.horizontalLayout_2 = QHBoxLayout(self.page_1_home)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_home = QFrame(self.page_1_home)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_home_temperature = QFrame(self.frame_home)
        self.frame_home_temperature.setObjectName(u"frame_home_temperature")
        self.frame_home_temperature.setFrameShape(QFrame.StyledPanel)
        self.frame_home_temperature.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_home_temperature)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_home_temperature = QLabel(self.frame_home_temperature)
        self.label_home_temperature.setObjectName(u"label_home_temperature")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_home_temperature.setFont(font1)
        self.label_home_temperature.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_home_temperature, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_home_temperature)

        self.label_home_status = QLabel(self.frame_home)
        self.label_home_status.setObjectName(u"label_home_status")
        self.label_home_status.setFont(font1)
        self.label_home_status.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_home_status, 0, Qt.AlignHCenter)

        self.version = QLabel(self.frame_home)
        self.version.setObjectName(u"version")
        self.version.setFont(font1)
        self.version.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.version, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_home)

        self.stackedWidget.addWidget(self.page_1_home)
        self.page_2_control = QWidget()
        self.page_2_control.setObjectName(u"page_2_control")
        self.verticalLayout_2 = QVBoxLayout(self.page_2_control)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_control = QFrame(self.page_2_control)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_control)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_control_top = QFrame(self.frame_control)
        self.frame_control_top.setObjectName(u"frame_control_top")
        self.frame_control_top.setMaximumSize(QSize(16777215, 50))
        self.frame_control_top.setFrameShape(QFrame.StyledPanel)
        self.frame_control_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_control_top)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_control_status = QLabel(self.frame_control_top)
        self.label_control_status.setObjectName(u"label_control_status")
        self.label_control_status.setFont(font1)
        self.label_control_status.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_control_status, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_control_top)

        self.frame_control_middle = QFrame(self.frame_control)
        self.frame_control_middle.setObjectName(u"frame_control_middle")
        self.frame_control_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_control_middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_control_middle)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_control_middle_left = QFrame(self.frame_control_middle)
        self.frame_control_middle_left.setObjectName(u"frame_control_middle_left")
        self.frame_control_middle_left.setFrameShape(QFrame.StyledPanel)
        self.frame_control_middle_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control_middle_left)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_control_open = QPushButton(self.frame_control_middle_left)
        self.pushButton_control_open.setObjectName(u"pushButton_control_open")
        self.pushButton_control_open.setMinimumSize(QSize(150, 0))
        self.pushButton_control_open.setMaximumSize(QSize(16777215, 200))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        self.pushButton_control_open.setFont(font2)
        self.pushButton_control_open.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_control_open)

        self.pushButton_control_close = QPushButton(self.frame_control_middle_left)
        self.pushButton_control_close.setObjectName(u"pushButton_control_close")
        self.pushButton_control_close.setMinimumSize(QSize(150, 0))
        self.pushButton_control_close.setMaximumSize(QSize(16777215, 200))
        self.pushButton_control_close.setFont(font1)
        self.pushButton_control_close.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_control_close)


        self.horizontalLayout_7.addWidget(self.frame_control_middle_left)

        self.frame_control_middle_right = QFrame(self.frame_control_middle)
        self.frame_control_middle_right.setObjectName(u"frame_control_middle_right")
        self.frame_control_middle_right.setFrameShape(QFrame.StyledPanel)
        self.frame_control_middle_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_control_middle_right)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_control_up = QPushButton(self.frame_control_middle_right)
        self.pushButton_control_up.setObjectName(u"pushButton_control_up")
        self.pushButton_control_up.setMinimumSize(QSize(150, 0))
        self.pushButton_control_up.setMaximumSize(QSize(16777215, 200))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Emoji"])
        font3.setPointSize(32)
        font3.setBold(True)
        self.pushButton_control_up.setFont(font3)
        self.pushButton_control_up.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_control_up)

        self.pushButton_control_down = QPushButton(self.frame_control_middle_right)
        self.pushButton_control_down.setObjectName(u"pushButton_control_down")
        self.pushButton_control_down.setMinimumSize(QSize(150, 0))
        self.pushButton_control_down.setMaximumSize(QSize(16777215, 200))
        self.pushButton_control_down.setFont(font3)
        self.pushButton_control_down.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(143, 143, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(125, 125, 125);\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_control_down)


        self.horizontalLayout_7.addWidget(self.frame_control_middle_right)


        self.verticalLayout_7.addWidget(self.frame_control_middle)

        self.frame_control_bottom = QFrame(self.frame_control)
        self.frame_control_bottom.setObjectName(u"frame_control_bottom")
        self.frame_control_bottom.setMaximumSize(QSize(16777215, 50))
        self.frame_control_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_control_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_control_bottom)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_7.addWidget(self.frame_control_bottom)


        self.verticalLayout_2.addWidget(self.frame_control)

        self.stackedWidget.addWidget(self.page_2_control)
        self.page_3_settings = QWidget()
        self.page_3_settings.setObjectName(u"page_3_settings")
        self.verticalLayout_5 = QVBoxLayout(self.page_3_settings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_settings = QFrame(self.page_3_settings)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_settings)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_settings_temperature = QFrame(self.frame_settings)
        self.frame_settings_temperature.setObjectName(u"frame_settings_temperature")
        self.frame_settings_temperature.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_temperature.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_settings_temperature)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_settings_temperature_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_settings_temperature_1)

        self.label_settings_temperature = QLabel(self.frame_settings_temperature)
        self.label_settings_temperature.setObjectName(u"label_settings_temperature")
        self.label_settings_temperature.setMinimumSize(QSize(200, 0))
        self.label_settings_temperature.setMaximumSize(QSize(200, 142))
        self.label_settings_temperature.setFont(font1)
        self.label_settings_temperature.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_settings_temperature)

        self.horizontalSlider_settings_temperature = QSlider(self.frame_settings_temperature)
        self.horizontalSlider_settings_temperature.setObjectName(u"horizontalSlider_settings_temperature")
        self.horizontalSlider_settings_temperature.setMinimumSize(QSize(300, 50))
        self.horizontalSlider_settings_temperature.setMaximumSize(QSize(450, 16777215))
        self.horizontalSlider_settings_temperature.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 25px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 25px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 5px;\n"
"}\n"
""
                        "\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 5px;\n"
"}")
        self.horizontalSlider_settings_temperature.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSlider_settings_temperature)

        self.horizontalSpacer_horizontalSpacer_settings_temperature_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_horizontalSpacer_settings_temperature_2)


        self.verticalLayout_8.addWidget(self.frame_settings_temperature)

        self.frame_settings_speed = QFrame(self.frame_settings)
        self.frame_settings_speed.setObjectName(u"frame_settings_speed")
        self.frame_settings_speed.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_speed.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_settings_speed)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_settings_speed_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_settings_speed_1)

        self.label_settings_speed = QLabel(self.frame_settings_speed)
        self.label_settings_speed.setObjectName(u"label_settings_speed")
        self.label_settings_speed.setMinimumSize(QSize(200, 0))
        self.label_settings_speed.setMaximumSize(QSize(200, 143))
        self.label_settings_speed.setFont(font1)
        self.label_settings_speed.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_settings_speed)

        self.horizontalSlider_settings_speed = QSlider(self.frame_settings_speed)
        self.horizontalSlider_settings_speed.setObjectName(u"horizontalSlider_settings_speed")
        self.horizontalSlider_settings_speed.setEnabled(True)
        self.horizontalSlider_settings_speed.setMinimumSize(QSize(300, 50))
        self.horizontalSlider_settings_speed.setMaximumSize(QSize(450, 16777215))
        self.horizontalSlider_settings_speed.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 25px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 25px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 5px;\n"
"}\n"
""
                        "\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 5px;\n"
"}")
        self.horizontalSlider_settings_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider_settings_speed)

        self.horizontalSpacer_settings_speed_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_settings_speed_2)


        self.verticalLayout_8.addWidget(self.frame_settings_speed)


        self.verticalLayout_5.addWidget(self.frame_settings)

        self.stackedWidget.addWidget(self.page_3_settings)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_10.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Automatic Shades", None))
        self.button_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.button_control.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.button_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_home_temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature: 0", None))
        self.label_home_status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v.0.0.1", None))
        self.label_control_status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.pushButton_control_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_control_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_control_up.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.pushButton_control_down.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.label_settings_temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature: ", None))
        self.label_settings_speed.setText(QCoreApplication.translate("MainWindow", u"Motor Speed:", None))
    # retranslateUi

