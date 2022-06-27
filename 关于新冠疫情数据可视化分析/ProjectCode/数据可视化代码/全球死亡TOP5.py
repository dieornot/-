import os
import numpy as np
import pandas as pd
#导入主题样式
from pyecharts.globals import ThemeType
import csv

# file_list = os.listdir('./M数据')
# file_list
#
# data = [pd.read_csv(f'./M数据/{i}') for i in file_list]
# df = pd.concat(data,axis=0,ignore_index=True) #ignore_index是否重构原表索引True重构
# df
df = pd.read_csv('../疫情数据/全球疫情数据.csv')
# 重命名
df.columns = ['country','add','cumulative','recovered','deaths']
# df.head()

# 画图
from pyecharts.charts import Funnel,Polar
from pyecharts import options as opts
# [('key','value')]
data1 = df.groupby('country')['deaths'].mean()
name = (data1.sort_values(ascending=False)[:5]).index.tolist()
num = (data1.sort_values(ascending=False)[:5]).values.tolist()
data_pair = [i for i in zip(name,num)]
# data_pair
C = (

    Funnel(init_opts=opts.InitOpts(width="800px", height="400px", theme=ThemeType.ROMANTIC))
        .add(
        series_name="死亡人数",
        data_pair=[list(z) for z in zip(name, num)],  # 使用zip将两个序列组合成一个序列
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}人"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )

        .set_global_opts(
        title_opts=opts.TitleOpts(title="全球死亡人数TOP5", subtitle="截至到2021/10/27"),
        visualmap_opts=opts.VisualMapOpts(min_=200000, max_=800000, pos_top="40%")

    )
        .render("../可视化/全球死亡人数TOP5.html")
)