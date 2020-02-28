import os
import csv


dictionary = {"Hubei": '湖北省', "Guangdong": '广东省', "Zhejiang": '浙江省', "Henan": '河南省', "Hunan": '湖南省', "Anhui": '安徽省', "Jiangxi": '江西省', "Jiangsu": '江苏省', "Chongqing": '重庆市', "Shandong": '山东省', "Sichuan": '四川省', "Beijing": '北京市', "Heilongjiang": '黑龙江省', "Shanghai": '上海市', "Fujian": '福建省', "Hebei": '河北省', "Shaanxi": '陕西省', "Guangxi": '广西壮族自治区', "Yunnan": '云南省', "Hainan": '海南省', "Shanxi": '山西省', "Guizhou": '贵州省', "Liaoning": '辽宁省', "Tianjin": '天津市', "Gansu": '甘肃省', "Jilin": '吉林省', "Inner Mongolia": '内蒙古自治区', "Ningxia": '宁夏回族自治区', "Xinjiang": '新疆维吾尔自治区', "Hong Kong": '香港', "Taiwan": '台湾', "Qinghai": '青海省', "Macau": '澳门', "Tibet": '西藏自治区'}


def clean(row: list):
    x = list()
    x.append(row[0])
    x.append(row[1])
    x.append('0')
    x.append('0')
    x.append(row[2])
    if x[0].startswith('#') or x[0].startswith('CHINA'):
        x[2] = 'suspected'
        x[3] = 'cured'
        return x
    x[0] = dictionary[x[0]]
    return x


with open('e.g. /Your/dir/to/Provinces/provinces_02-15.csv') as file:
    reader = csv.reader(file)
    for _ in range(2):
        next(reader)
    with open('e.g. /Your/dir/to/Provinces/provinces_02-15-(yourSuffix).csv', 'w+') as out:
        writer = csv.writer(out)
        for _ in range(3):
            writer.writerow(['', '', ''])
        count = 0
        for row in reader:
            # print(row[0].split('|'))
            if count == 35:
                break
            writer.writerow(clean(row[0].split('|')))
            count += 1
