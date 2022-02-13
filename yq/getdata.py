# encoding: utf-8
import requests
import os
import time
import json
import faker
import pandas as pd
import re
import subprocess
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Line, Page
from threading import Thread


class Data:
    # 初始化
    def __init__(self):
        self.response = []  # 目标网站html
        self.file_path = '疫情情况采集'  # 保存路径
        self.ab_label = []  # 全球城市名称
        self.ab_c = []  # 全球累计确诊人数
        self.ab_now_c = []  # 全球现在确诊人数
        self.GBR_c = []  # 英国新增确诊
        self.USA_c = []  # 美国新增确诊
        self.BRA_c = []  # 巴西新增确诊
        self.IND_c = []  # 印度新增确诊
        self.JPN_c = []  # 日本新增确诊
        self.CHN_c = []  # 中国新增确诊
        self.dateId = []  # 重点国家新增确诊时间范围
        self.labels = []  # 国内省份名称
        self.c = []  # 国内累计确诊人数
        self.now_c = []  # 国内现在确诊人数
        self.hcount = []  # 高风险地区数
        self.mcount = []  # 中风险地区数
        self.h_province = []  # 高风险省
        self.m_province = []  # 中风险省
        self.h_area_name = []  # 高风险地区
        self.m_area_name = []  # 中风险地区
        self.h_province_count = []  # 高风险省数量
        self.m_province_count = []  # 中风险省数量
        self.headers = {'User-Agent': faker.Faker().user_agent()}  # 随机ua
        # self.connect = create_engine(f'mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8')  # 连接数据库
        self.current_time = time.strftime("%Y年%m月%d日", time.localtime())  # 获取本地时间

    """爬取数据"""

    # 爬取疫情总体信息
    def get_data_html(self):
        # 请求页面
        self.response.append(requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0',
                                          headers=self.headers, timeout=3))

    # 获取历史数据
    def get_province_json(self, json_url, s_date, e_date):
        province_confirmedCount = []  # 历史累计确诊
        province_deadCount = []  # 历史累计死亡
        province_currentConfirmedCount = []  # 历史现有确诊
        dateId = []  # 时间
        s_data_index = []  # 开始下标
        e_date_index = []  # 结束下标
        flag = False
        # 请求页面
        response = requests.get(json_url, headers=self.headers,
                                timeout=3)
        response.encoding = 'utf-8'
        json_data = json.loads(response.text)
        data = json_data['data']
        # 将data缩小为指定的范围，使其爬取指定日期内的数据
        for i in range(len(data)):
            if s_date == data[i]['dateId']:
                s_data_index.append(i)
                flag = True
            if flag and e_date == data[i]['dateId']:
                e_date_index.append(i)
                break
        else:  # 若找不到指定日期则返回空值
            return province_confirmedCount, province_currentConfirmedCount, province_deadCount, dateId

        for i in range(s_data_index[0], e_date_index[0]):
            if 'confirmedCount' in data[i]:
                province_confirmedCount.append(data[i]['confirmedCount'])
            else:
                province_confirmedCount.append('无')
            if 'deadCount' in data[i]:
                province_deadCount.append(data[i]['deadCount'])
            else:
                province_deadCount.append('无')
            if 'currentConfirmedCount' in data[i]:
                province_currentConfirmedCount.append(data[i]['currentConfirmedCount'])
            else:
                province_currentConfirmedCount.append('无')
            if 'dateId' in data[i]:
                dateId.append(data[i]['dateId'])
            else:
                dateId.append('无')
        return province_confirmedCount, province_currentConfirmedCount, province_deadCount, dateId

    # 筛选全球疫情信息
    def get_abroad(self):
        self.response[0].encoding = 'utf-8'
        soup = BeautifulSoup(self.response[0].text, 'lxml')
        # 爬取选择网页文档的内容
        data = soup.find_all(name='script', attrs={'id': 'getListByCountryTypeService2true'})
        # 转为字符串
        account = str(data)
        account1 = account[95:-21]  # 切片截取从52到后面倒数21取到需要的数据
        account1_json = json.loads(account1)

        # 提取数据到列表
        ab_id = []
        ab_continents = []
        ab_provinceName = []
        ab_currentConfirmedCount = []
        ab_confirmedCount = []
        ab_confirmedCountRank = []
        ab_suspectedCount = []
        ab_curedCount = []
        ab_deadCount = []
        ab_deadCountRank = []
        ab_deadRate = []
        ab_deadRateRank = []
        ab_locationId = []
        ab_statisticsData = []
        for a in account1_json:
            if 'id' in a:
                ab_id.append(a['id'])
            else:
                ab_id.append('无')
            ab_continents.append(a['continents'])
            ab_provinceName.append(a['provinceName'])
            self.ab_label.append(ab_provinceName)
            ab_currentConfirmedCount.append(a['currentConfirmedCount'])
            self.ab_now_c.append(ab_currentConfirmedCount)
            ab_confirmedCount.append(a['confirmedCount'])
            self.ab_c.append(ab_confirmedCount)
            if 'confirmedCountRank' in a:
                ab_confirmedCountRank.append(a['confirmedCountRank'])
            else:
                ab_confirmedCountRank.append('无')
            ab_suspectedCount.append(a['suspectedCount'])
            ab_curedCount.append(a['curedCount'])
            ab_deadCount.append(a['deadCount'])
            if 'deadCountRank' in a:
                ab_deadCountRank.append(a['deadCountRank'])
            else:
                ab_deadCountRank.append('无')
            if 'deadRate' in a:
                ab_deadRate.append(a['deadRate'])
            else:
                ab_deadRate.append('无')
            if 'deadRateRank' in a:
                ab_deadRateRank.append(a['deadRateRank'])
            else:
                ab_deadRateRank.append('无')
            if 'locationId' in a:
                ab_locationId.append(a['locationId'])
                if a['locationId'] == 961007:
                    self.GBR_c.append(self.get_epidemic_situation_in_key(a['statisticsData']))
                elif a['locationId'] == 971002:
                    self.USA_c.append(self.get_epidemic_situation_in_key(a['statisticsData']))
                elif a['locationId'] == 973003:
                    self.BRA_c.append(self.get_epidemic_situation_in_key(a['statisticsData']))
                elif a['locationId'] == 953003:
                    self.IND_c.append(self.get_epidemic_situation_in_key(a['statisticsData']))
                elif a['locationId'] == 951002:
                    self.JPN_c.append(self.get_epidemic_situation_in_key(a['statisticsData']))
                elif a['locationId'] == 951001:
                    self.CHN_c.append(self.get_epidemic_situation_in_key(a['statisticsData']))
            else:
                ab_locationId.append('无')
            if 'statisticsData' in a:
                ab_statisticsData.append(a['statisticsData'])
            else:
                ab_statisticsData.append('无')

        # 转换成pandas数组
        df = {
            'id': pd.Series(ab_id),
            '所在大洲': pd.Series(ab_continents),
            '城市': pd.Series(ab_provinceName),
            '当前确诊': pd.Series(ab_currentConfirmedCount),
            '累计确诊': pd.Series(ab_confirmedCount),
            '确诊排名': pd.Series(ab_confirmedCountRank),
            '疑似病例': pd.Series(ab_suspectedCount),
            '治愈人数': pd.Series(ab_curedCount),
            '死亡人数': pd.Series(ab_deadCount),
            '死亡人数排名': pd.Series(ab_deadCountRank),
            '死亡率': pd.Series(ab_deadRate),
            '死亡率排名': pd.Series(ab_deadRateRank),
            '地区id': pd.Series(ab_locationId),
            '历史数据': pd.Series(ab_statisticsData)
        }
        pds = pd.DataFrame(df)
        pds.to_csv(r'.\疫情情况采集\全球\全球疫情实时采集-{0}.csv'.format(self.current_time))  # 保存到csv
        # pds.to_sql(name='全球疫情信息表', con=self.connect, if_exists='replace', index=False)  # 保存到mysql

    # 获取重点国家疫情信息
    def get_epidemic_situation_in_key(self, url):
        e_currentConfirmedCount = []
        dateId = []
        response = requests.get(url, headers={'User-Agent': faker.Faker().user_agent()}, timeout=3)
        response.encoding = 'utf-8'
        json_data = json.loads(response.text)
        data = json_data['data']
        for i in range(len(data) - 1, len(data) - 270, -1):  # 获取最近9个月数据
            if 'currentConfirmedCount' in data[i]:
                e_currentConfirmedCount.append(data[i]['currentConfirmedCount'])
            else:
                e_currentConfirmedCount.append(0)
            if 'dateId' in data[i]:
                dateId.append(data[i]['dateId'])
        self.dateId.append(dateId)
        return e_currentConfirmedCount

    # 获取风险地区
    def get_dangerous_area(self):
        headers = {
            'User-Agent': faker.Faker().user_agent()  # 随机ua
        }
        response = requests.get('http://diqu.gezhong.vip/api.php',
                                headers=headers,
                                timeout=3)
        # 请求页面
        response.encoding = 'utf-8'
        json_data = json.loads(response.text)
        hcount1 = json_data['data']['hcount']  # 高风险地区数
        mcount1 = json_data['data']['mcount']  # 中风险地区数
        self.hcount.append(hcount1)
        self.mcount.append(mcount1)
        h_province2 = []
        m_province2 = []

        '''高风险省 数量'''
        for i in json_data['data']['highlist']:
            h_province2.append(i['province'])
            h_province2.append(len(i['communitys']))
            for n in i['communitys']:
                self.h_area_name.append(i['area_name'] + ' ' + n)
        for h in range(len(h_province2)):
            if type(h_province2[h]) == int:
                continue
            if h + 2 <= len(h_province2):
                for h2 in range(h + 2, len(h_province2)):
                    if type(h_province2[h2]) == int:
                        continue
                    else:
                        if h_province2[h] == h_province2[h2]:
                            count = h_province2[h + 1] + h_province2[h2 + 1]
                            h_province2.append(h_province2[h])
                            h_province2.append(count)
                            h_province2[h] = 0
                            h_province2[h + 1] = 0
                            h_province2[h2] = 0
                            h_province2[h2 + 1] = 0
                            break
        for i in range(len(h_province2)):  # 简化省名称
            char = ''
            if type(h_province2[i]) == int:
                continue
            else:
                if '省' in h_province2[i]:
                    for j in h_province2[i]:
                        if j == '省':
                            continue
                        else:
                            char += j
                    self.h_province.append(char)
                else:
                    self.h_province.append(h_province2[i])
                self.h_province_count.append(h_province2[i + 1])
        del h_province2

        '''中风险省 数量'''
        for i in json_data['data']['middlelist']:
            m_province2.append(i['province'])
            m_province2.append(len(i['communitys']))
            for n in i['communitys']:
                self.m_area_name.append(i['area_name'] + ' ' + n)
        for m in range(len(m_province2)):
            if type(m_province2[m]) == int:
                continue
            if m + 2 <= len(m_province2):
                for m2 in range(m + 2, len(m_province2)):
                    if type(m_province2[m2]) == int:
                        continue
                    else:
                        if m_province2[m] == m_province2[m2]:
                            count = m_province2[m + 1] + m_province2[m2 + 1]
                            m_province2.append(m_province2[m])
                            m_province2.append(count)
                            m_province2[m] = 0
                            m_province2[m + 1] = 0
                            m_province2[m2] = 0
                            m_province2[m2 + 1] = 0
                            break
        for i in range(len(m_province2)):
            char = ''
            if type(m_province2[i]) == int:
                continue
            else:
                if '省' in m_province2[i]:
                    for j in m_province2[i]:
                        if j == '省':
                            continue
                        else:
                            char += j
                    self.m_province.append(char)
                else:
                    self.m_province.append(m_province2[i])
                self.m_province_count.append(m_province2[i + 1])
        del m_province2

    # 获取国内疫情信息
    def get_data_dictype(self):
        areas_type_dic_raw = re.findall('try { window.getAreaStat = (.*?)}catch\(e\)',
                                        str(self.response[0].content, 'utf-8'))
        areas_type_dic = json.loads(areas_type_dic_raw[0])
        # 返回经过json转换过的字典化的数据
        return areas_type_dic

    """确定及创建项目保存路径"""

    # 检查并创建数据目录
    def make_dir(self):
        if not os.path.exists(self.file_path):
            print('数据文件夹不存在')
            os.makedirs(self.file_path)
            os.makedirs(self.file_path + r'\国内')
            os.makedirs(self.file_path + r'\全球')
            print('数据文件夹创建成功,创建目录为{0}'.format(self.file_path))
        else:
            print('数据保存在目录：{0}'.format(self.file_path))

    """数据写入Excel"""

    # 爬取数据并保存在Excel中
    def save_data_to_excle(self):
        self.make_dir()  # 调用方法检查数据目录是否存在，不存在则创建数据文件夹
        self.get_data_html()  # 爬取目标网站html
        self.get_abroad()  # 爬取全球疫情信息并保存
        self.get_dangerous_area()  # 爬取风险地区
        # 提取数据到列表
        provinceshortName = []
        p_currentconfirmedCount = []
        p_confirmedcount = []
        p_suspectedcount = []
        p_curedcount = []
        p_deadcount = []
        p_locationid = []
        p_statisticsData = []
        cityname = []
        c_currentconfirmedCount = []
        c_confirmedcount = []
        c_suspectedcount = []
        c_curedcount = []
        c_deadcount = []
        c_locationid = []
        for province_data in self.get_data_dictype():
            provincename = province_data['provinceName']
            provinceshortName.append(province_data['provinceShortName'])
            p_currentconfirmedCount.append(province_data['currentConfirmedCount'])
            p_confirmedcount.append(province_data['confirmedCount'])
            p_suspectedcount.append(province_data['suspectedCount'])
            p_curedcount.append(province_data['curedCount'])
            p_deadcount.append(province_data['deadCount'])
            p_locationid.append(province_data['locationId'])
            p_statisticsData.append(province_data['statisticsData'])
            self.labels.append(province_data['provinceShortName'])
            self.c.append(province_data['confirmedCount'])
            self.now_c.append(province_data['currentConfirmedCount'])
            # 用循环获取省级以及该省以下城市的数据
            for citiy_data in province_data['cities']:
                # 该部分获取某个省下某城市的数据
                cityname.append(citiy_data['cityName'])
                c_currentconfirmedCount.append(citiy_data['currentConfirmedCount'])
                c_confirmedcount.append(citiy_data['confirmedCount'])
                c_suspectedcount.append(citiy_data['suspectedCount'])
                c_curedcount.append(citiy_data['curedCount'])
                c_deadcount.append(citiy_data['deadCount'])
                c_locationid.append(citiy_data['locationId'])
                # 转换成pandas数组
                c_df = {
                    '城市名称': pd.Series(cityname),
                    '现存确诊人数': pd.Series(c_currentconfirmedCount),
                    '累计确诊人数': pd.Series(c_confirmedcount),
                    '疑似人数': pd.Series(c_suspectedcount),
                    '治愈人数': pd.Series(c_curedcount),
                    '死亡人数': pd.Series(c_deadcount),
                    '地区ID编码': pd.Series(c_locationid),
                }
                c_pds = pd.DataFrame(c_df)
                c_pds.to_csv(r'.\疫情情况采集\国内\{0}.csv'.format(provincename))  # 保存到csv
                # c_pds.to_sql(name=provincename, con=self.connect, if_exists='replace', index=False)  # 保存到mysql
        # 转换成pandas数组
        df = {
            '城市名称': pd.Series(provinceshortName),
            '现存确诊人数': pd.Series(p_currentconfirmedCount),
            '累计确诊人数': pd.Series(p_confirmedcount),
            '疑似人数': pd.Series(p_suspectedcount),
            '治愈人数': pd.Series(p_curedcount),
            '死亡人数': pd.Series(p_deadcount),
            '地区ID编码': pd.Series(p_locationid),
            '历史数据': pd.Series(p_statisticsData),
        }
        pds = pd.DataFrame(df)
        pds.to_csv(r'.\疫情情况采集\国内\国内疫情实时采集-{0}.csv'.format(self.current_time))  # 保存到csv
        # pds.to_sql(name='国内疫情信息表', con=self.connect, if_exists='replace', index=False)  # 保存到mysql
        print('---数据爬取成功---')

    """生成地图文件"""

    def sjvisual(self):

        self.domestic_epidemic_map(self.c, '累计确诊')
        self.domestic_epidemic_map(self.now_c, '现有确诊')
        self.global_epidemic_map(self.ab_c, '累计确诊')
        self.global_epidemic_map(self.ab_now_c, '现有确诊')
        self.page_draggable_layout()

    # 国内疫情地图
    def domestic_epidemic_map(self, data, str1):
        # 定义每个字段的范围，以及每个字段的样式
        pieces = [
            {'min': 10000, 'color': '#540d0d'},
            {'max': 9999, 'min': 1000, 'color': '#9c1414'},
            {'max': 999, 'min': 500, 'color': '#d92727'},
            {'max': 499, 'min': 100, 'color': '#ed3232'},
            {'max': 99, 'min': 10, 'color': '#f27777'},
            {'max': 9, 'min': 1, 'color': '#f7adad'},
            {'max': 0, 'color': '#f7e4e4'},
        ]
        z = zip(self.labels, data)
        s = sorted(z, key=lambda x: x[1], reverse=False)
        labels = [data[0] for data in s]
        counts = [data[1] for data in s]
        m = Map(init_opts=opts.InitOpts(width="1500px",
                                        height="650px",
                                        page_title="国内疫情", ))
        m.add('{0}'.format(str1), [list(z) for z in zip(labels, counts)], 'china')
        # 初始化配置项
        # 系列配置项，可配置图元样式、文字样式、标签样式、电线样式等
        m.set_series_opts(label_opts=opts.LabelOpts(font_size=12), is_show=False)
        # 全局配置项，可配置标题、动画、坐标轴、图例等
        # is_piecewise参数表示是否分段，is_show参数表示是否显示视觉映射配置
        m.set_global_opts(title_opts=opts.TitleOpts(title='实时{0}数据'.format(str1), subtitle='数据来源：丁香园网站'),
                          legend_opts=opts.LegendOpts(is_show=False),
                          visualmap_opts=opts.VisualMapOpts(pieces=pieces, is_piecewise=True, is_show=True))
        # render()会生成本地html文件
        filepath = './疫情情况采集/国内/国内疫情{0}人数.html'.format(str1)
        m.render(path=filepath)

    # 全球疫情地图
    def global_epidemic_map(self, data, str1):
        # pyecharts全球地图默认英文名,需要替换为中文
        name_map = {
            'Singapore Rep.': '新加坡',
            'Dominican Rep.': '多米尼加',
            'Palestine': '巴勒斯坦',
            'Bahamas': '巴哈马',
            'Timor-Leste': '东帝汶',
            'Afghanistan': '阿富汗',
            'Guinea-Bissau': '几内亚比绍',
            "Côte d'Ivoire": '科特迪瓦',
            'Siachen Glacier': '锡亚琴冰川',
            "Br. Indian Ocean Ter.": '英属印度洋领土',
            'Angola': '安哥拉',
            'Albania': '阿尔巴尼亚',
            'United Arab Emirates': '阿联酋',
            'Argentina': '阿根廷',
            'Armenia': '亚美尼亚',
            'French Southern and Antarctic Lands': '法属南半球和南极领地',
            'Australia': '澳大利亚',
            'Austria': '奥地利',
            'Azerbaijan': '阿塞拜疆',
            'Burundi': '布隆迪',
            'Belgium': '比利时',
            'Benin': '贝宁',
            'Burkina Faso': '布基纳法索',
            'Bangladesh': '孟加拉国',
            'Bulgaria': '保加利亚',
            'The Bahamas': '巴哈马',
            'Bosnia and Herz.': '波斯尼亚和黑塞哥维那',
            'Belarus': '白俄罗斯',
            'Belize': '伯利兹',
            'Bermuda': '百慕大',
            'Bolivia': '玻利维亚',
            'Brazil': '巴西',
            'Brunei': '文莱',
            'Bhutan': '不丹',
            'Botswana': '博茨瓦纳',
            'Central African Rep.': '中非',
            'Canada': '加拿大',
            'Switzerland': '瑞士',
            'Chile': '智利',
            'China': '中国',
            'Ivory Coast': '象牙海岸',
            'Cameroon': '喀麦隆',
            'Dem. Rep. Congo': '刚果民主共和国',
            'Congo': '刚果',
            'Colombia': '哥伦比亚',
            'Costa Rica': '哥斯达黎加',
            'Cuba': '古巴',
            'N. Cyprus': '北塞浦路斯',
            'Cyprus': '塞浦路斯',
            'Czech Rep.': '捷克',
            'Germany': '德国',
            'Djibouti': '吉布提',
            'Denmark': '丹麦',
            'Algeria': '阿尔及利亚',
            'Ecuador': '厄瓜多尔',
            'Egypt': '埃及',
            'Eritrea': '厄立特里亚',
            'Spain': '西班牙',
            'Estonia': '爱沙尼亚',
            'Ethiopia': '埃塞俄比亚',
            'Finland': '芬兰',
            'Fiji': '斐',
            'Falkland Islands': '福克兰群岛',
            'France': '法国',
            'Gabon': '加蓬',
            'United Kingdom': '英国',
            'Georgia': '格鲁吉亚',
            'Ghana': '加纳',
            'Guinea': '几内亚',
            'Gambia': '冈比亚',
            'Guinea Bissau': '几内亚比绍',
            'Eq. Guinea': '赤道几内亚',
            'Greece': '希腊',
            'Greenland': '格陵兰',
            'Guatemala': '危地马拉',
            'French Guiana': '法属圭亚那',
            'Guyana': '圭亚那',
            'Honduras': '洪都拉斯',
            'Croatia': '克罗地亚',
            'Haiti': '海地',
            'Hungary': '匈牙利',
            'Indonesia': '印度尼西亚',
            'India': '印度',
            'Ireland': '爱尔兰',
            'Iran': '伊朗',
            'Iraq': '伊拉克',
            'Iceland': '冰岛',
            'Israel': '以色列',
            'Italy': '意大利',
            'Jamaica': '牙买加',
            'Jordan': '约旦',
            'Japan': '日本',
            'Kazakhstan': '哈萨克斯坦',
            'Kenya': '肯尼亚',
            'Kyrgyzstan': '吉尔吉斯斯坦',
            'Cambodia': '柬埔寨',
            'Korea': '韩国',
            'Kosovo': '科索沃',
            'Kuwait': '科威特',
            'Lao PDR': '老挝',
            'Lebanon': '黎巴嫩',
            'Liberia': '利比里亚',
            'Libya': '利比亚',
            'Sri Lanka': '斯里兰卡',
            'Lesotho': '莱索托',
            'Lithuania': '立陶宛',
            'Luxembourg': '卢森堡',
            'Latvia': '拉脱维亚',
            'Morocco': '摩洛哥',
            'Moldova': '摩尔多瓦',
            'Madagascar': '马达加斯加',
            'Mexico': '墨西哥',
            'Macedonia': '马其顿',
            'Mali': '马里',
            'Myanmar': '缅甸',
            'Montenegro': '黑山',
            'Mongolia': '蒙古',
            'Mozambique': '莫桑比克',
            'Mauritania': '毛里塔尼亚',
            'Malawi': '马拉维',
            'Malaysia': '马来西亚',
            'Namibia': '纳米比亚',
            'New Caledonia': '新喀里多尼亚',
            'Niger': '尼日尔',
            'Nigeria': '尼日利亚',
            'Nicaragua': '尼加拉瓜',
            'Netherlands': '荷兰',
            'Norway': '挪威',
            'Nepal': '尼泊尔',
            'New Zealand': '新西兰',
            'Oman': '阿曼',
            'Pakistan': '巴基斯坦',
            'Panama': '巴拿马',
            'Peru': '秘鲁',
            'Philippines': '菲律宾',
            'Papua New Guinea': '巴布亚新几内亚',
            'Poland': '波兰',
            'Puerto Rico': '波多黎各',
            'Dem. Rep. Korea': '朝鲜',
            'Portugal': '葡萄牙',
            'Paraguay': '巴拉圭',
            'Qatar': '卡塔尔',
            'Romania': '罗马尼亚',
            'Russia': '俄罗斯',
            'Rwanda': '卢旺达',
            'W. Sahara': '西撒哈拉',
            'Saudi Arabia': '沙特阿拉伯',
            'Sudan': '苏丹',
            'S. Sudan': '南苏丹',
            'Senegal': '塞内加尔',
            'Solomon Is.': '所罗门群岛',
            'Sierra Leone': '塞拉利昂',
            'El Salvador': '萨尔瓦多',
            'Somaliland': '索马里兰',
            'Somalia': '索马里',
            'Serbia': '塞尔维亚',
            'Suriname': '苏里南',
            'Slovakia': '斯洛伐克',
            'Slovenia': '斯洛文尼亚',
            'Sweden': '瑞典',
            'Swaziland': '斯威士兰',
            'Syria': '叙利亚',
            'Chad': '乍得',
            'Togo': '多哥',
            'Thailand': '泰国',
            'Tajikistan': '塔吉克斯坦',
            'Turkmenistan': '土库曼斯坦',
            'East Timor': '东帝汶',
            'Trinidad and Tobago': '特里尼达和多巴哥',
            'Tunisia': '突尼斯',
            'Turkey': '土耳其',
            'Tanzania': '坦桑尼亚',
            'Uganda': '乌干达',
            'Ukraine': '乌克兰',
            'Uruguay': '乌拉圭',
            'United States': '美国',
            'Uzbekistan': '乌兹别克斯坦',
            'Venezuela': '委内瑞拉',
            'Vietnam': '越南',
            'Vanuatu': '瓦努阿图',
            'West Bank': '西岸',
            'Yemen': '也门',
            'South Africa': '南非',
            'Zambia': '赞比亚',
            'Zimbabwe': '津巴布韦'
        }
        pieces = [
            {'min': 1000000, 'color': '#642100'},
            {'max': 9999999, 'min': 1000000, 'color': '#A23400'},
            {'max': 999999, 'min': 100000, 'color': '#D94600'},
            {'max': 99999, 'min': 10000, 'color': '#FF5809'},
            {'max': 9999, 'min': 1000, 'color': '#FF8F59'},
            {'max': 999, 'min': 100, 'color': '#FFAD86'},
            {'max': 99, 'min': 1, 'color': '#FFE7BA'},
            {'max': 0, 'color': '#FFF3EE'},
        ]
        z = zip(self.ab_label[0], data[0])
        s = sorted(z, key=lambda x: x[1], reverse=False)
        labels = [data[0] for data in s]
        counts = [data[1] for data in s]
        m = Map(init_opts=opts.InitOpts(width="1500px",
                                        height="650px",
                                        page_title="全球疫情",
                                        ))
        m.add('{0}'.format(str1), [list(z) for z in zip(labels, counts)], 'world', name_map=name_map)
        m.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        m.set_global_opts(title_opts=opts.TitleOpts(title='实时{0}数据'.format(str1), subtitle='数据来源：丁香园网站'),
                          # legend_opts=opts.LegendOpts(is_show=False),
                          visualmap_opts=opts.VisualMapOpts(pieces=pieces, is_piecewise=True, is_show=True))
        filepath = './疫情情况采集/全球/全球疫情{0}人数.html'.format(str1)
        m.render(path=filepath)

    # 国内疫情折线图
    def domestic_epidemic_line(self, x, y, str1, province, s_date, e_date):
        x2 = []
        for i in range(len(x)):
            x2.append(str(x[i]))
        x = x2
        del x2
        l = Line(init_opts=opts.InitOpts(width="1500px",
                                         height="650px",
                                         page_title=province,
                                         ))
        l.set_global_opts(title_opts=opts.TitleOpts(title='{0}{1}数据'.format(province, str1), subtitle='数据来源：丁香园网站'),
                          tooltip_opts=opts.TooltipOpts(is_show=False),
                          xaxis_opts=opts.AxisOpts(type_="category"),
                          yaxis_opts=opts.AxisOpts(type_="value",
                                                   axistick_opts=opts.AxisTickOpts(is_show=True),
                                                   splitline_opts=opts.SplitLineOpts(is_show=True),
                                                   ), )
        l.add_xaxis(xaxis_data=x)
        l.add_yaxis(series_name='',
                    y_axis=y,
                    symbol="emptyCircle",
                    is_symbol_show=True,
                    label_opts=opts.LabelOpts(is_show=True),
                    )
        l.render(r'.\疫情情况采集\国内\{0}\{2}-{3}{0}{1}人数.html'.format(province, str1, s_date, e_date))

    # 英国疫情折线图
    def GBR_c_line(self) -> Line:
        x = []
        for i in range(len(self.dateId[0])):
            x.append(str(self.dateId[0][i]))
        c = (
            Line(init_opts=opts.InitOpts(width="800px",
                                         height="500px",
                                         page_title='英国疫情折线图',
                                         ))
            .add_xaxis(x)
            .add_yaxis("新增确诊", self.GBR_c[0])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="英国"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        return c

    # 美国疫情折线图
    def USA_c_line(self) -> Line:
        x = []
        for i in range(len(self.dateId[0])):
            x.append(str(self.dateId[0][i]))
        c = (
            Line(init_opts=opts.InitOpts(width="800px",
                                         height="500px",
                                         page_title='美国疫情折线图',
                                         ))
            .add_xaxis(x)
            .add_yaxis("新增确诊", self.USA_c[0])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="美国"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        return c

    # 巴西疫情折线图
    def BRA_c_line(self) -> Line:
        x = []
        for i in range(len(self.dateId[0])):
            x.append(str(self.dateId[0][i]))
        c = (
            Line(init_opts=opts.InitOpts(width="800px",
                                         height="500px",
                                         page_title='巴西折线图',
                                         ))
            .add_xaxis(x)
            .add_yaxis("新增确诊", self.BRA_c[0])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="巴西"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        return c

    # 印度疫情折线图
    def IND_c_line(self) -> Line:
        x = []
        for i in range(len(self.dateId[0])):
            x.append(str(self.dateId[0][i]))
        c = (
            Line(init_opts=opts.InitOpts(width="800px",
                                         height="500px",
                                         page_title='印度疫情折线图',
                                         ))
            .add_xaxis(x)
            .add_yaxis("新增确诊", self.IND_c[0])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="印度"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        return c

    # 日本疫情折线图
    def JPN_c_line(self) -> Line:
        x = []
        for i in range(len(self.dateId[0])):
            x.append(str(self.dateId[0][i]))
        c = (
            Line(init_opts=opts.InitOpts(width="800px",
                                         height="500px",
                                         page_title='日本疫情折线图',
                                         ))
            .add_xaxis(x)
            .add_yaxis("新增确诊", self.JPN_c[0])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="日本"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        return c

    # 中国疫情折线图
    def CHN_c_line(self) -> Line:
        x = []
        for i in range(len(self.dateId[0])):
            x.append(str(self.dateId[0][i]))
        c = (
            Line(init_opts=opts.InitOpts(width="800px",
                                         height="500px",
                                         page_title='中国疫情折线图',
                                         ))
            .add_xaxis(x)
            .add_yaxis("新增确诊", self.CHN_c[0])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="中国"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        return c

    def page_draggable_layout(self):
        page = Page(layout=Page.DraggablePageLayout)
        page.add(
            self.GBR_c_line(),
            self.USA_c_line(),
            self.BRA_c_line(),
            self.IND_c_line(),
            self.JPN_c_line(),
            self.CHN_c_line(),
        )
        page.render("./疫情情况采集/全球/重点国家疫情折线图.html")

    # 国内风险地区地图
    def domestic_risk_area_map(self, province, data, str1):
        pieces = [
            {'min': 50, 'color': '#540d0d'},
            {'max': 40, 'min': 31, 'color': '#d92727'},
            {'max': 30, 'min': 21, 'color': '#ed3232'},
            {'max': 20, 'min': 11, 'color': '#f27777'},
            {'max': 10, 'min': 1, 'color': '#f7adad'},
            {'max': 0, 'color': '#f7e4e4'},
        ]
        z = zip(province, data)
        s = sorted(z, key=lambda x: x[1], reverse=False)
        labels = [data[0] for data in s]
        counts = [data[1] for data in s]
        m = Map(init_opts=opts.InitOpts(width="1500px",
                                        height="650px",
                                        page_title="国内疫情",
                                        ))
        m.add('{0}'.format(str1), [list(z) for z in zip(labels, counts)], 'china')
        m.set_series_opts(label_opts=opts.LabelOpts(font_size=12), is_show=False)
        m.set_global_opts(
            title_opts=opts.TitleOpts(title='{0}'.format(str1), subtitle='数据来源：http://diqu.gezhong.vip/api.php'),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(pieces=pieces, is_piecewise=True, is_show=True))
        filepath = './疫情情况采集/国内/国内{0}.html'.format(str1)
        m.render(path=filepath)

    # 打开文件
    def show_c_html(self):
        def threadFunc():  # 使用子线程打开文件，解决打开文件时主界面僵死问题
            # os.system(r'.\疫情情况采集\国内疫情累计确诊人数.html')  # 调用cmd命令（第一行加utf-8，否则有可能乱码）
            # 使用该方法替代os.system()解决程序打包成exe后运行cmd命令时弹窗问题
            subprocess.run(r'.\疫情情况采集\国内\国内疫情累计确诊人数.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)  # 创建子线程对象（target表示执行的函数，不能加'()'，arge表示函数的参数，元组类型）
        thread.start()  # start之后子线程就会执行target的函数

    # 打开文件
    def show_now_c_html(self):
        def threadFunc():
            subprocess.run(r'.\疫情情况采集\国内\国内疫情现有确诊人数.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    @staticmethod
    # 打开文件
    def show_ab_c_html():
        def threadFunc():
            subprocess.run(r'.\疫情情况采集\全球\全球疫情累计确诊人数.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    @staticmethod
    # 打开文件
    def show_ab_now_c_html():
        def threadFunc():
            subprocess.run(r'.\疫情情况采集\全球\全球疫情现有确诊人数.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    # 打开文件
    def show_hi_c_html(self, province, province_confirmedCount, dateId, s_date, e_date):
        self.domestic_epidemic_line(dateId, province_confirmedCount, '历史累计确诊', province, s_date, e_date)

        def threadFunc():
            subprocess.run(r'.\疫情情况采集\国内\{0}\{1}-{2}{0}历史累计确诊人数.html'.format(province, s_date, e_date),
                           shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    # 打开文件
    def show_hi_now_c_html(self, province, province_currentConfirmedCount, dateId, s_date, e_date):
        self.domestic_epidemic_line(dateId, province_currentConfirmedCount, '历史现有确诊', province, s_date, e_date)

        def threadFunc():
            subprocess.run(r'.\疫情情况采集\国内\{0}\{1}-{2}{0}历史现有确诊人数.html'.format(province, s_date, e_date),
                           shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    # 打开文件
    def show_hi_dead_html(self, province, province_deadCount, dateId, s_date, e_date):
        self.domestic_epidemic_line(dateId, province_deadCount, '历史累计死亡', province, s_date, e_date)

        def threadFunc():
            subprocess.run(r'.\疫情情况采集\国内\{0}\{1}-{2}{0}历史累计死亡人数.html'.format(province, s_date, e_date),
                           shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    # 打开文件
    def show_high_area_html(self):
        self.domestic_risk_area_map(self.h_province, self.h_province_count, '高风险地区')

        def threadFunc():
            subprocess.run(r'.\疫情情况采集\国内\国内高风险地区.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    # 打开文件
    def show_middle_area_html(self):
        self.domestic_risk_area_map(self.m_province, self.m_province_count, '中风险地区')

        def threadFunc():
            subprocess.run(r'.\疫情情况采集\国内\国内中风险地区.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()

    @staticmethod
    # 打开文件
    def show_key_countries_html():
        def threadFunc():
            subprocess.run(r'.\疫情情况采集\全球\重点国家疫情折线图.html', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        thread = Thread(target=threadFunc)
        thread.start()
