import csv
import os


provinces = ['湖北省', '浙江省', '广东省', '河南省', '重庆市', '湖南省', '安徽省', '北京市', '四川省', '上海市', '山东省', '江西省',
             '广西壮族自治区', '江苏省', '海南省', '陕西省', '辽宁省', '福建省', '黑龙江省', '天津市', '河北省', '云南省', '山西省',
             '内蒙古自治区', '甘肃省', '贵州省', '香港', '澳门', '宁夏回族自治区', '吉林省', '新疆维吾尔自治区', '台湾', '青海省',
             '西藏自治区']

dictionary = {'湖北省': [], '浙江省': [], '广东省': [], '河南省': [], '重庆市': [], '湖南省': [], '安徽省': [], '北京市': [],
              '四川省': [], '上海市': [], '山东省': [], '江西省': [], '广西壮族自治区': [], '江苏省': [], '海南省': [],
              '陕西省': [], '辽宁省': [], '福建省': [], '黑龙江省': [], '天津市': [], '河北省': [], '云南省': [], '山西省': [],
              '内蒙古自治区': [], '甘肃省': [], '贵州省': [], '香港': [], '澳门': [], '宁夏回族自治区': [], '吉林省': [],
              '新疆维吾尔自治区': [], '台湾': [], '青海省': [], '西藏自治区': []}


def wash(path):
    root = '/Your/dir/to/Province/dataset/'
    with open(path, 'w+') as target:
        for i in range(26, 32, 1):
            source = root + 'provinces_01-' + str(i) + '.csv'
            with open(source, 'r') as src:
                reader = csv.reader(src)
                for _ in range(4):
                    next(reader)
                for row in reader:
                    pro = row[0]
                    if pro == '待明确地区':
                        continue
                    dictionary[pro].append(row[1:])
                for key in dictionary:
                    # print(dictionary[key])
                    if len(dictionary[key]) == 0:
                        dictionary[key] = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]

        for i in range(1, 9, 1):
            source = root + 'provinces_02-0' + str(i) + '.csv'
            with open(source, 'r') as src:
                reader = csv.reader(src)
                for _ in range(4):
                    next(reader)
                for row in reader:
                    pro = row[0]
                    if pro == '待明确地区':
                        continue
                    dictionary[pro].append(row[1:])
                for key in dictionary:
                    # print(dictionary[key])
                    if len(dictionary[key]) == 0:
                        dictionary[key] = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]

wash('test.csv')
root = 'dataset/'
for key in dictionary:
    uri = root + key + '.csv'
    with open(uri, 'w+') as output:
        writer = csv.writer(output)
        for row in dictionary[key]:
            writer.writerow(row)
    print(key + ' OK')
