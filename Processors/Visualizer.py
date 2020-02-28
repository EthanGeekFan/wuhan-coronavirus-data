from pyecharts.charts import Map, Pie
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import csv


# def sort(target: dict):
#     result = {}
#     for i in len(target):
#         index = target.keys()[]
#         for key in target:
#             val = target[key]
#             if val > target[index]:
#                 index = key
#         result[index]




params = {}
# for example, your prediction of a specific date.
with open('File that contain: provinceName, value', 'r') as values:
    reader = csv.reader(values)
    next(reader)
    for row in reader:
        pro, val = row
        pro = pro.replace('省', '')
        pro = pro.replace('自治区', '')
        pro = pro.replace('族', '')
        pro = pro.replace('回', '')
        pro = pro.replace('壮', '')
        pro = pro.replace('维吾尔', '')
        pro = pro.replace('市', '')
        if pro != '':
            params[pro] = val

total = 0

for i in params:
    total += float(params[i])

for i in params:
    params[i] = float(params[i]) / total

print(params)
attr = list(params.keys())
value = list(params.values())


map = Map()
map.add("", [list(z) for z in zip(params.keys(), params.values())], 'china')
map.set_global_opts(
    # title_opts=opts.TitleOpts(title='中国疫情空间分布'),
    visualmap_opts=opts.VisualMapOpts(max_=100),
    legend_opts=opts.LegendOpts(
                type_="scroll", pos_left="80%", orient="vertical", is_show=False
    ),
)
map.render(path='map.html')
# make_snapshot(snapshot, map.render(), "map.png")
print(params['广东'])
print(params['浙江'])
print(params['河南'])
print(params['湖南'])
print(params['安徽'])
print(params['江西'])
