import csv
import os
import pyecharts.options as opts
from pyecharts.charts import Bar
import numpy as np
import pandas as pd
from pyecharts.globals import ThemeType

# file_list = os.listdir('./中国数据')
# file_list
# data = [
#     pd.read_csv(f'./中国数据/{i}') for i in file_list
#     ]
# df = pd.concat(data,axis=0,ignore_index=True)
df = pd.read_csv('../疫情数据/中国疫情数据.csv')
df.columns = ['city','add','current','accumulate','cure','death']
data1 = df.groupby('city')['accumulate'].mean()
name = data1.sort_values(ascending=False)[:10].index.tolist()
num = data1.sort_values(ascending=False)[:10].values.tolist()
A = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
        .set_colors("#df9464")
        .add_xaxis(name)
        .add_yaxis("累计病例TOP10", num, category_gap="50%")
        .set_global_opts(title_opts=opts.TitleOpts(title="中国确诊城市TOP10", subtitle=""))
        .render("../可视化/中国地区确诊数量TOP10.html")

)
