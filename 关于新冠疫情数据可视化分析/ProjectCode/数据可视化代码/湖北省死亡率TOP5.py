import os
import numpy as np
import pandas as pd
df = pd.read_csv('../各省市数据/湖北.csv')
df.columns = ['city', 'add','now', 'cumulative', 'recovered', 'deaths']
# 画图
from pyecharts.charts import Funnel,Polar, Liquid,Grid,Line
from pyecharts import options as opts
df['death rate'] = df['deaths']/df['cumulative']
df['death rate']=df['death rate'] *100
# [('key','value')]
data2 = df.groupby('city')['death rate'].mean()
name2 =  round(data2.sort_values(ascending=False)[:5],2).index.tolist()
num2 = round(data2.sort_values(ascending=False)[:5],2).values.tolist()
data_pair = [i for i in zip(name2,num2)]
B =(
    Line(init_opts=opts.InitOpts(width="1080px", height="520px"))
    .add_xaxis(name2)
    .add_yaxis("死亡率(%)",
        num2,
        symbol="triangle",
        symbol_size=20,
        linestyle_opts=opts.LineStyleOpts(color="Wheat", width=4, type_="dashed"),
        label_opts=opts.LabelOpts(is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(
            border_width=3, border_color="yellow", color="Tomato"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="湖北省死亡率TOP5"),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),)

    .render("../可视化/湖北死亡top5.html")
)