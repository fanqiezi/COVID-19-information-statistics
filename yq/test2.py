# encoding:utf-8
import json

import faker
import requests

hcount = []  # 高风险地区数
mcount = []  # 中风险地区数
h_province = []  # 高风险省
m_province = []  # 中风险省
h_area_name = []  # 高风险地区
m_area_name = []  # 中风险地区
h_province_count = []  # 高风险省对应的数量
m_province_count = []  # 中风险省对应的数量

def get_dangerous_area():  # 爬取风险地区
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
    hcount.append(hcount1)
    mcount.append(mcount1)
    h_province2 = []
    m_province2 = []

    '''高风险省 数量'''
    for i in json_data['data']['highlist']:
        h_province2.append(i['province'])
        h_province2.append(len(i['communitys']))
        for n in i['communitys']:
            h_area_name.append(i['area_name'] + ' ' + n)
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
                h_province.append(char)
            else:
                h_province.append(h_province2[i])
            h_province_count.append(h_province2[i + 1])
    del h_province2

    '''中风险省 数量'''
    for i in json_data['data']['middlelist']:
        m_province2.append(i['province'])
        m_province2.append(len(i['communitys']))
        for n in i['communitys']:
            m_area_name.append(i['area_name'] + ' ' + n)
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
                m_province.append(char)
            else:
                m_province.append(m_province2[i])
            m_province_count.append(m_province2[i + 1])
    del m_province2

get_dangerous_area()