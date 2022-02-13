import os
import area
from mainwindow import *
from getdata import Data

'''主窗口'''


# 继承mainwindow.py的Ui_MainWindow类，实现功能与布局分离
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        '''设置各按钮对应的方法'''
        self.existing_diagnostic_map.clicked.connect(d.show_now_c_html)
        self.cumulative_diagnosis_map.clicked.connect(d.show_c_html)
        self.high_risk_area_map.clicked.connect(d.show_high_area_html)
        self.medium_risk_area_map.clicked.connect(d.show_middle_area_html)
        self.high_risk_areas.clicked.connect(self.show_h_area_name)
        self.medium_risk_areas.clicked.connect(self.show_m_area_name)
        self.world_cumulative_diagnosis_map.clicked.connect(d.show_ab_c_html)
        self.world_key_countries_map.clicked.connect(d.show_key_countries_html)
        self.world_existing_diagnosis_map.clicked.connect(d.show_ab_now_c_html)
        self.cumulative_diagnosis_provincial_history.clicked.connect(  # lambda表达式可以在按钮click的时候能够传递参数
            lambda: d.show_hi_c_html(self.province_name[0], self.province_confirmedCount[0],
                                     self.dateId[0], self.s_date[0], self.e_date[0]))
        self.provincial_history_current_diagnosis.clicked.connect(
            lambda: d.show_hi_c_html(self.province_name[0], self.province_currentConfirmedCount[0],
                                     self.dateId[0], self.s_date[0], self.e_date[0]))
        self.cumulative_deaths_history_province.clicked.connect(
            lambda: d.show_hi_c_html(self.province_name[0], self.province_deadCount[0], self.dateId[0],
                                     self.s_date[0], self.e_date[0]))

        # 在查询之前禁用查询历史信息的三个按钮
        self.cumulative_diagnosis_provincial_history.setEnabled(False)
        self.provincial_history_current_diagnosis.setEnabled(False)
        self.cumulative_deaths_history_province.setEnabled(False)

        # 设置提示信息
        self.save.appendPlainText('获取成功')
        self.save.appendPlainText(r'数据保存在{0}\{1}'.format(os.getcwd(), d.file_path))

        '''二级下拉列表（点击省匹配对应地级市）'''
        # 初始化省
        self.cb_province.clear()  # 清空items
        self.cb_province.addItem('请选择')
        for k, v in area.dictProvince.items():
            self.cb_province.addItem(v, k)  # 键、值反转

    @Slot(int)
    # 取市的键值
    def on_cb_province_activated(self, index):
        key = self.cb_province.itemData(index)
        # print(key)
        self.cb_city.clear()  # 清空items
        if key:
            self.cb_city.addItem('请选择')
            self.cb_city.addItem('境外输入')
            # 初始化市
            for k, v in area.dictCity[key].items():
                self.cb_city.addItem(v, k)  # 键、值反转

    @Slot()
    # 点击查询按钮时执行
    def on_select_clicked(self):
        # 获取当前选项框索引
        province_index = self.cb_province.currentIndex()
        city_index = self.cb_city.currentIndex()
        # 取当前省市县名称
        province_name = self.cb_province.itemText(province_index)
        city_name = self.cb_city.itemText(city_index)
        # print(province_name, city_name)
        '''二级下拉列表结束'''

        # 启用查询历史信息的三个按钮
        self.cumulative_diagnosis_provincial_history.setEnabled(True)
        self.provincial_history_current_diagnosis.setEnabled(True)
        self.cumulative_deaths_history_province.setEnabled(True)

        # 成员变量（方便查看历史信息的三个按钮调用，解决按钮函数被重复调用问题）
        self.province_name = []
        self.province_confirmedCount = []
        self.province_currentConfirmedCount = []
        self.province_deadCount = []
        self.dateId = []
        self.s_date = []
        self.e_date = []
        # 清空上次数据
        self.province.setText('')
        self.p_currentConfirmedCount.setText('')
        self.p_confirmedCount.setText('')
        self.p_suspectedCount.setText('')
        self.p_curedCount.setText('')
        self.p_deadCount.setText('')
        self.area.setText('')
        self.a_currentConfirmedCount.setText('')
        self.a_confirmedCount.setText('')
        self.a_suspectedCount.setText('')
        self.a_curedCount.setText('')
        self.a_deadCount.setText('')
        # 保存省名
        self.province_name.append(province_name)

        # 获取时间数据
        s_qdate = self.start_dateEdit.date()  # 返回 PySide2.QtCore.QDate 对象
        s_year = str(s_qdate.year())
        s_month = str(s_qdate.month())
        if len(s_month) < 2:  # 格式化时间，使小于两位数的时间前加‘0’
            s_month = '0' + s_month
        s_day = str(s_qdate.day())
        if len(s_day) < 2:
            s_day = '0' + s_day
        e_qdate = self.end_dateEdit.date()
        e_year = str(e_qdate.year())
        e_month = str(e_qdate.month())
        if len(e_month) < 2:
            e_month = '0' + e_month
        e_day = str(e_qdate.day())
        if len(e_day) < 2:
            e_day = '0' + e_day
        s_date = int(s_year + s_month + s_day)  # 开始时间
        e_date = int(e_year + e_month + e_day)  # 结束时间
        self.s_date.append(s_date)
        self.e_date.append(e_date)

        if not os.path.exists(d.file_path + '\\国内\\' + province_name):  # 创建省信息文件夹
            # print('省信息文件夹不存在')
            self.save.appendPlainText('省信息文件夹不存在')
            os.makedirs(d.file_path + '\\国内\\' + province_name)
            # print('省信息文件夹创建成功,创建目录为%s' % (d.file_path + '/' + province_name))
            self.save.appendPlainText(r'省信息文件夹创建成功,创建目录为{0}\{1}\国内\{2}'.format(os.getcwd(),
                                                                            d.file_path, province_name))
        else:
            # print('省信息保存在目录：%s' % (d.file_path + '/' + province_name))
            self.save.appendPlainText(r'省信息保存在目录：{0}\{1}\国内\{2}'.format(os.getcwd(), d.file_path, province_name))

        # 匹配省数据
        for province_data in d.get_data_dictype():
            provinceShortName = province_data['provinceShortName']
            if province_name == provinceShortName:
                province_confirmedCount, province_currentConfirmedCount, province_deadCount, dateId = \
                    d.get_province_json(province_data['statisticsData'], s_date, e_date)
                if not dateId:  # 日期超出范围时弹出警告框
                    QMessageBox.warning(
                        self,  # 窗口
                        '查询失败',  # 标题
                        '选择的日期超出了范围'  # 内容
                    )
                else:
                    self.province_confirmedCount.append(province_confirmedCount)
                    self.province_currentConfirmedCount.append(province_currentConfirmedCount)
                    self.province_deadCount.append(province_deadCount)
                    self.dateId.append(dateId)
                    # 显示省数据
                    self.province.setText(provinceShortName)
                    self.p_currentConfirmedCount.setText(str(province_data['currentConfirmedCount']))
                    self.p_confirmedCount.setText(str(province_data['confirmedCount']))
                    self.p_suspectedCount.setText(str(province_data['suspectedCount']))
                    self.p_curedCount.setText(str(province_data['curedCount']))
                    self.p_deadCount.setText(str(province_data['deadCount']))
                    self.cumulative_diagnosis_provincial_history.setText('{0}历史累计确诊'.format(province_name))
                    self.provincial_history_current_diagnosis.setText('{0}历史现有确诊'.format(province_name))
                    self.cumulative_deaths_history_province.setText('{0}历史累计死亡'.format(province_name))

                    # 匹配地级市数据
                    for city_data in province_data['cities']:
                        if city_name == city_data['cityName']:
                            # 显示地级市数据
                            self.area.setText(str(city_data['cityName']))
                            self.a_currentConfirmedCount.setText(str(city_data['currentConfirmedCount']))
                            self.a_confirmedCount.setText(str(city_data['confirmedCount']))
                            self.a_suspectedCount.setText(str(city_data['suspectedCount']))
                            self.a_curedCount.setText(str(city_data['curedCount']))
                            self.a_deadCount.setText(str(city_data['deadCount']))

    # 点击高风险地区按钮时执行
    def show_h_area_name(self):
        # 实例化另外一个窗口
        self.h = h_area_name()
        for item in d.h_area_name:
            self.h.textEdit.appendPlainText(item)  # 将高风险地区追加到文本输入框
        # 显示新窗口
        self.h.show()

    # 点击中风险地区按钮时执行
    def show_m_area_name(self):
        # 实例化另外一个窗口
        self.m = m_area_name()
        for item in d.m_area_name:
            self.m.textEdit.appendPlainText(item)  # 将中风险地区追加到文本输入框
        # 显示新窗口
        self.m.show()



if __name__ == '__main__':
    import sys
    d = Data()  # 创建getdata.py里类Data的对象，方便调用对应的变量和方法
    d.save_data_to_excle()  # 爬取并保存数据
    d.sjvisual()  # 生成地图
    # GUI
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
