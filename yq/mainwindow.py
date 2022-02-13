# -*- coding: utf-8 -*-
# 该类由QT设计师的ui文件自动生成（有改动）
################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 810)
        icon = QIcon()
        icon.addFile(u"./images/\u7edf\u8ba1.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks | QMainWindow.AnimatedDocks)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/bg1.jpg")))
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1201, 800))
        self.widget.setMinimumSize(QSize(1201, 800))
        self.widget.setMaximumSize(QSize(1201, 800))
        self.widget.setStyleSheet(
            "/*\u6309\u94ae\uff08\u6b63\u5e38\uff09*/\n"
            "QPushButton{\n"
            "/*border-image:url();*/\n"
            "background-color:rgba(255,255,255,0);\n"
            "color:#FFFFFF;\n"
            # "border:2px solid white;\n"
            "border-radius:10px;\n"
            "}\n"
            "\n"
            "/*\u6309\u94ae\uff08\u60ac\u505c\uff09*/\n"
            "QPushButton:hover{\n"
            "/*border-image:url();*/\n"
            "background-color:rgba(84,204,243,0);\n"
            "color:rgb(84,204,243);\n"
            "border:2px solid rgb(84,204,243);\n"
            "border-radius:10px;\n"
            "}\n"
            "\n"
            "/*\u6309\u94ae\uff08\u6309\u4e0b\uff09*/\n"
            "QPushButton:pressed{\n"
            "/*border-image:url();*/\n"
            "background-color:rgba(29,107,214,0);\n"
            "color:rgb(29,107,214);\n"
            "border:2px solid rgb(29,107,214);\n"
            "border-radius:10px;\n"
            "}\n"
            "\n"
            "/*\u6587\u672c*/\n"
            "QLabel{\n"
            "border-image:url();\n"
            "font-weight:bold;\n"
            "color:#FFFFFF;\n"
            "}\n"
            "\n"
            "/*\u4e0b\u62c9\u5217\u8868*/\n"
            "QComboBox{\n"
            "border-image:url();\n"
            "}")
        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(110, 240, 91, 21))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(360, 240, 101, 21))
        self.label_32.setFont(font)
        self.end_dateEdit = QDateEdit(self.widget)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setGeometry(QRect(470, 240, 110, 22))
        self.end_dateEdit.setDate(QDate.currentDate())  # 设置结束日期
        self.start_dateEdit = QDateEdit(self.widget)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setGeometry(QRect(230, 240, 110, 22))
        self.start_dateEdit.setDate(QDate(2020, 1, 25))  # 设置开始日期
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 40, 451, 91))
        font = QFont()
        font.setFamily(u"UD Digi Kyokasho NK-B")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.b_out = QPushButton(self.widget)
        self.b_out.setObjectName(u"b_out")
        self.b_out.setGeometry(QRect(1130, 10, 51, 51))
        self.b_out.setStyleSheet(u"QPushButton{\n"
                                 "border-image:url(./images/\u9009\u9879\u5361\u5173"
                                 "\u95ed\u6309\u94ae.png);\n "
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "border-image:url(./images/\u9009\u9879\u5361\u5173"
                                 "\u95ed\u6309\u94ae2.png);\n "
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "border-image:url(./images/\u9009\u9879\u5361\u5173"
                                 "\u95ed\u6309\u94ae3.png);\n "
                                 "}")
        self.b_out.clicked.connect(MainWindow.close)
        self.cb_province = QComboBox(self.widget)
        self.cb_province.setObjectName(u"cb_province")
        self.cb_province.setGeometry(QRect(252, 180, 87, 22))
        self.cb_city = QComboBox(self.widget)
        self.cb_city.setObjectName(u"cb_city")
        self.cb_city.setGeometry(QRect(501, 182, 87, 22))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 300, 72, 21))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 370, 141, 21))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 440, 131, 21))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 510, 101, 31))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 650, 91, 31))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 580, 91, 31))
        self.label_8.setFont(font1)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(360, 650, 91, 31))
        self.label_10.setFont(font1)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(360, 370, 141, 31))
        self.label_11.setFont(font1)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(360, 440, 141, 31))
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(360, 510, 101, 21))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(360, 580, 91, 31))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(360, 300, 71, 31))
        self.label_15.setFont(font1)
        self.cumulative_deaths_history_province = QPushButton(self.widget)
        self.cumulative_deaths_history_province.setObjectName(u"cumulative_deaths_history_province")
        self.cumulative_deaths_history_province.setGeometry(QRect(610, 440, 181, 28))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.cumulative_deaths_history_province.setFont(font2)
        self.cumulative_diagnosis_provincial_history = QPushButton(self.widget)
        self.cumulative_diagnosis_provincial_history.setObjectName(u"cumulative_diagnosis_provincial_history")
        self.cumulative_diagnosis_provincial_history.setGeometry(QRect(610, 300, 181, 28))
        self.cumulative_diagnosis_provincial_history.setFont(font2)
        self.provincial_history_current_diagnosis = QPushButton(self.widget)
        self.provincial_history_current_diagnosis.setObjectName(u"provincial_history_current_diagnosis")
        self.provincial_history_current_diagnosis.setGeometry(QRect(610, 370, 181, 28))
        self.provincial_history_current_diagnosis.setFont(font2)
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.select = QPushButton(self.widget)
        self.select.setObjectName(u"select")
        self.select.setGeometry(QRect(620, 170, 171, 71))
        self.select.setFont(font4)
        self.b_minimize = QPushButton(self.widget)
        self.b_minimize.setObjectName(u"b_minimize")
        self.b_minimize.setGeometry(QRect(1033, 10, 91, 55))
        self.b_minimize.setStyleSheet(u"QPushButton {\n"
                                      "border-image:url(./images/\u6700\u5c0f\u5316"
                                      "\u6309\u94ae.png);\n "
                                      "padding:25px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "border-image:url(./images/\u6700\u5c0f\u5316"
                                      "\u6309\u94ae2.png);\n "
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "border-image:url(./images/\u6700\u5c0f\u5316"
                                      "\u6309\u94ae3.png);\n "
                                      "}")
        self.b_minimize.clicked.connect(MainWindow.showMinimized)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(110, 110, 121, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_16.setFont(font3)
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(810, 120, 121, 31))
        self.label_17.setFont(font3)
        self.existing_diagnostic_map = QPushButton(self.widget)
        self.existing_diagnostic_map.setObjectName(u"existing_diagnostic_map")
        self.existing_diagnostic_map.setGeometry(QRect(810, 180, 141, 31))
        self.existing_diagnostic_map.setFont(font2)
        self.existing_diagnostic_map.setStyleSheet(u"")
        self.cumulative_diagnosis_map = QPushButton(self.widget)
        self.cumulative_diagnosis_map.setObjectName(u"cumulative_diagnosis_map")
        self.cumulative_diagnosis_map.setGeometry(QRect(980, 180, 141, 28))
        self.cumulative_diagnosis_map.setFont(font2)
        self.high_risk_areas = QPushButton(self.widget)
        self.high_risk_areas.setObjectName(u"high_risk_areas")
        self.high_risk_areas.setGeometry(QRect(810, 300, 121, 28))
        self.high_risk_areas.setFont(font2)
        self.high_risk_area_map = QPushButton(self.widget)
        self.high_risk_area_map.setObjectName(u"high_risk_area_map")
        self.high_risk_area_map.setGeometry(QRect(810, 240, 161, 28))
        self.high_risk_area_map.setFont(font2)
        self.medium_risk_area_map = QPushButton(self.widget)
        self.medium_risk_area_map.setObjectName(u"medium_risk_area_map")
        self.medium_risk_area_map.setGeometry(QRect(980, 240, 161, 28))
        self.medium_risk_area_map.setFont(font2)
        self.medium_risk_areas = QPushButton(self.widget)
        self.medium_risk_areas.setObjectName(u"medium_risk_areas")
        self.medium_risk_areas.setGeometry(QRect(980, 300, 121, 28))
        self.medium_risk_areas.setFont(font2)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(810, 370, 121, 41))
        self.label_2.setFont(font3)
        self.world_cumulative_diagnosis_map = QPushButton(self.widget)
        self.world_cumulative_diagnosis_map.setObjectName(u"world_cumulative_diagnosis_map")
        self.world_cumulative_diagnosis_map.setGeometry(QRect(810, 440, 181, 28))
        self.world_cumulative_diagnosis_map.setFont(font2)
        self.world_key_countries_map = QPushButton(self.widget)
        self.world_key_countries_map.setObjectName(u"world_key_countries_map")
        self.world_key_countries_map.setGeometry(QRect(1000, 440, 151, 31))
        self.world_key_countries_map.setFont(font2)
        self.world_existing_diagnosis_map = QPushButton(self.widget)
        self.world_existing_diagnosis_map.setObjectName(u"world_existing_diagnosis_map")
        self.world_existing_diagnosis_map.setGeometry(QRect(810, 500, 181, 28))
        self.world_existing_diagnosis_map.setFont(font2)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(110, 170, 121, 41))
        self.label_9.setFont(font1)
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(360, 180, 121, 31))
        self.label_18.setFont(font1)
        self.save = QPlainTextEdit(self.widget)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(110, 700, 1041, 70))
        # self.save.setFont(font1)
        self.province = QLabel(self.widget)
        self.province.setObjectName(u"province")
        self.province.setGeometry(QRect(260, 300, 72, 25))
        self.province.setFont(font4)
        self.p_currentConfirmedCount = QLabel(self.widget)
        self.p_currentConfirmedCount.setObjectName(u"p_currentConfirmedCount")
        self.p_currentConfirmedCount.setGeometry(QRect(260, 370, 72, 25))
        self.p_currentConfirmedCount.setFont(font4)
        self.p_confirmedCount = QLabel(self.widget)
        self.p_confirmedCount.setObjectName(u"p_confirmedCount")
        self.p_confirmedCount.setGeometry(QRect(260, 440, 72, 25))
        self.p_confirmedCount.setFont(font4)
        self.p_suspectedCount = QLabel(self.widget)
        self.p_suspectedCount.setObjectName(u"p_suspectedCount")
        self.p_suspectedCount.setGeometry(QRect(260, 510, 72, 25))
        self.p_suspectedCount.setFont(font4)
        self.p_curedCount = QLabel(self.widget)
        self.p_curedCount.setObjectName(u"p_curedCount")
        self.p_curedCount.setGeometry(QRect(260, 580, 72, 25))
        self.p_curedCount.setFont(font4)
        self.p_deadCount = QLabel(self.widget)
        self.p_deadCount.setObjectName(u"p_deadCount")
        self.p_deadCount.setGeometry(QRect(260, 650, 72, 25))
        self.p_deadCount.setFont(font4)
        self.area = QLabel(self.widget)
        self.area.setObjectName(u"area")
        self.area.setGeometry(QRect(430, 300, 160, 25))
        self.area.setFont(font4)
        self.a_currentConfirmedCount = QLabel(self.widget)
        self.a_currentConfirmedCount.setObjectName(u"a_currentConfirmedCount")
        self.a_currentConfirmedCount.setGeometry(QRect(510, 370, 72, 25))
        self.a_currentConfirmedCount.setFont(font4)
        self.a_confirmedCount = QLabel(self.widget)
        self.a_confirmedCount.setObjectName(u"a_confirmedCount")
        self.a_confirmedCount.setGeometry(QRect(510, 440, 72, 25))
        self.a_confirmedCount.setFont(font4)
        self.a_suspectedCount = QLabel(self.widget)
        self.a_suspectedCount.setObjectName(u"a_suspectedCount")
        self.a_suspectedCount.setGeometry(QRect(510, 510, 72, 25))
        self.a_suspectedCount.setFont(font4)
        self.a_curedCount = QLabel(self.widget)
        self.a_curedCount.setObjectName(u"a_curedCount")
        self.a_curedCount.setGeometry(QRect(510, 580, 72, 25))
        self.a_curedCount.setFont(font4)
        self.a_deadCount = QLabel(self.widget)
        self.a_deadCount.setObjectName(u"a_deadCount")
        self.a_deadCount.setGeometry(QRect(510, 650, 72, 25))
        self.a_deadCount.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1199, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u65b0\u51a0\u75ab\u60c5\u667a\u6167\u7edf\u8ba1\u4fe1\u606f\u5e73\u53f0",
                                                             None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u65f6\u95f4\uff1a", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f\u65f6\u95f4\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u65b0\u51a0\u75ab\u60c5\u667a\u6167\u7edf\u8ba1\u4fe1\u606f\u5e73\u53f0",
                                                      None))
        self.b_out.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7701\u4efd\uff1a", None))
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"\u73b0\u6709\u786e\u8bca\u4eba\u6570\uff1a", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"\u7d2f\u8ba1\u786e\u8bca\u4eba\u6570\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7591\u4f3c\u4eba\u6570\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6b7b\u4ea1\u4eba\u6570\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6cbb\u6108\u4eba\u6570\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6b7b\u4ea1\u4eba\u6570\uff1a", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"\u73b0\u6709\u786e\u8bca\u4eba\u6570\uff1a", None))
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"\u7d2f\u8ba1\u786e\u8bca\u4eba\u6570\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7591\u4f3c\u4eba\u6570\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6cbb\u6108\u4eba\u6570\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5730\u533a\uff1a", None))
        self.cumulative_deaths_history_province.setText("")
        self.cumulative_diagnosis_provincial_history.setText("")
        self.provincial_history_current_diagnosis.setText("")
        self.b_minimize.setText("")
        self.select.setText("查询")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u7701\u5e02\u75ab\u60c5", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u56fd\u5185\u75ab\u60c5", None))
        self.existing_diagnostic_map.setText(
            QCoreApplication.translate("MainWindow", u"\u73b0\u6709\u786e\u8bca\u5730\u56fe", None))
        self.cumulative_diagnosis_map.setText(
            QCoreApplication.translate("MainWindow", u"\u7d2f\u8ba1\u786e\u8bca\u5730\u56fe", None))
        self.high_risk_areas.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u98ce\u9669\u5730\u533a", None))
        self.high_risk_area_map.setText(
            QCoreApplication.translate("MainWindow", u"\u9ad8\u98ce\u9669\u5730\u533a\u5730\u56fe", None))
        self.medium_risk_area_map.setText(
            QCoreApplication.translate("MainWindow", u"\u4e2d\u98ce\u9669\u5730\u533a\u5730\u56fe", None))
        self.medium_risk_areas.setText(
            QCoreApplication.translate("MainWindow", u"\u4e2d\u98ce\u9669\u5730\u533a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e16\u754c\u75ab\u60c5", None))
        self.world_cumulative_diagnosis_map.setText(
            QCoreApplication.translate("MainWindow", u"\u4e16\u754c\u7d2f\u8ba1\u786e\u8bca\u5730\u56fe", None))
        self.world_key_countries_map.setText(
            QCoreApplication.translate("MainWindow", u"\u91cd\u70b9\u56fd\u5bb6\u6298\u7ebf\u56fe", None))
        self.world_existing_diagnosis_map.setText(
            QCoreApplication.translate("MainWindow", u"\u4e16\u754c\u73b0\u6709\u786e\u8bca\u5730\u56fe", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7701\u4efd\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u5730\u533a\uff1a", None))
        self.province.setText("")
        self.p_currentConfirmedCount.setText("")
        self.p_confirmedCount.setText("")
        self.p_suspectedCount.setText("")
        self.p_curedCount.setText("")
        self.p_deadCount.setText("")
        self.area.setText("")
        self.a_currentConfirmedCount.setText("")
        self.a_confirmedCount.setText("")
        self.a_suspectedCount.setText("")
        self.a_curedCount.setText("")
        self.a_deadCount.setText("")
    # retranslateUi


'''创建中高风险地区对应的窗口'''


class h_area_name(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(649, 523)
        self.setWindowTitle('高风险地区')
        icon = QIcon()
        icon.addFile(u"./images/\u7edf\u8ba1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.textEdit = QPlainTextEdit()
        # self.textEdit.setGeometry(QRect(10, 10, 631, 411))
        grid = QGridLayout(centralWidget)
        grid.addWidget(self.textEdit)
        # self.b_back = QPushButton('返回')
        # self.b_back.move(500, 750)
        # self.b_back.clicked.connect(self.close)


class m_area_name(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(649, 523)
        self.setWindowTitle('中风险地区')
        icon = QIcon()
        icon.addFile(u"./images/\u7edf\u8ba1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.textEdit = QPlainTextEdit()
        # self.textEdit.setGeometry(QRect(10, 10, 631, 411))
        grid = QGridLayout(centralWidget)
        grid.addWidget(self.textEdit)
        # self.b_back = QPushButton('返回')
        # self.b_back.move(500, 750)
        # self.b_back.clicked.connect(self.close)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
