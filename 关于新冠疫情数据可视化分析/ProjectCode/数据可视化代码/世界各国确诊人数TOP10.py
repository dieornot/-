import os
import numpy as np
import pandas as pd

from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType

df = pd.read_csv('../疫情数据/全球疫情数据.csv')

# 将列名改成英文
df.columns = ['country', 'add', 'cumulative', 'recovered', 'deaths']
df.reset_index(drop=True,inplace=True)
df['cumulative'] = df['cumulative'].astype(np.int64)
# df.info()
# [('key','value')]
data1 = df.groupby('country')['cumulative'].mean()
name = data1.sort_values(ascending=False)[:10].index.tolist()
num = data1.sort_values(ascending=False)[:10].values.tolist()
data_pair = [i for i in zip(name, num)]

A = (
   Pie(init_opts=opts.InitOpts(width="49%", height="700px",theme=ThemeType.ROMANTIC))
    .add("",data_pair,radius=["25%", "70%"],rosetype="radius")
       .set_colors(["SandyBrown ", "LightSteelBlue  ", "LightGreen ", "LightPink", "LightSalmon ",
                    "LightSeaGreen ", "LightSkyBlue", "LightSlateBlue ", "LightSlateGray ", "SlateGray"])
       .set_global_opts(title_opts=opts.TitleOpts(title="Pie-blue"))
       .set_global_opts(title_opts=opts.TitleOpts(title="世界各国确诊人数TOP10", pos_left="30%"), legend_opts=opts.LegendOpts(
       orient="vertical",
       pos_left="5%",
       pos_top="10%"
   )
                        )

    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    .render('../可视化/世界各国确诊人数TOP10.html')
)