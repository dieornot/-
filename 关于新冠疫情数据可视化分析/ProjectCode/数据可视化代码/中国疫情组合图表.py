import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Map, Page, Tree, Line, WordCloud, Scatter
from pyecharts.globals import ThemeType

data = pd.read_csv('../疫情数据/中国疫情数据.csv')
# print(data)
# 将列名改成英文
data.columns = ['city','newly_add','existing','cumulative','cure','death']
# print(data.head())
data['newly_add'] = data['newly_add'].astype(np.int64)
data['existing'] = data['existing'].astype(np.int64)
data['cumulative'] = data['cumulative'].astype(np.int64)
data['cure'] = data['cure'].astype(np.int64)
data['death'] = data['death'].astype(np.int64)
# print(data.info())
city_list = data['city']
cumulative_list = data['cumulative']
data_list = [i for i in zip(city_list,cumulative_list)]

data1 = data.groupby('city')['cumulative'].mean()
city= data1.sort_values(ascending=False)[:10].index.tolist()
cumulative = data1.sort_values(ascending=False)[:10].values.tolist()


df = pd.read_csv('../各省市数据/湖北.csv')
# 将列名改成英文
df.columns = ['city', 'add', 'now', 'cumulative', 'recovered', 'deaths']
df.reset_index(drop=True,inplace=True)
# df.info()
name_sries = df.groupby('city')['cumulative'].mean()
name = round(name_sries.sort_values(ascending=False)[:10],1).index.tolist()
list_1 = [{'name':i}for i in name]
list_2 = [{'children':list_1,'name':'湖北省'}]

df['death rate'] = df['deaths']/df['cumulative']
df['death rate']=df['death rate'] *100
# [('key','value')]
data2 = df.groupby('city')['death rate'].mean()
name2 =  round(data2.sort_values(ascending=False)[:5],2).index.tolist()
num2 = round(data2.sort_values(ascending=False)[:5],2).values.tolist()
data_pair = [i for i in zip(name2,num2)]

city_list = data['city']
newly_add_list = data['newly_add']
data_list_2 = [i for i in zip(city_list,newly_add_list)]


map = Scatter(init_opts=opts.InitOpts(bg_color='#404a59')) # 设置底图颜色

def map_china() -> Map:
    a = (
        Map(init_opts=opts.InitOpts(width="100%",height="800px",theme=ThemeType.ROMANTIC))
        .add("确诊人数",data_list,"china")
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0,max_=5000),
         title_opts=opts.TitleOpts(title="中国疫情分布图"))
    )
    return a

def bar_china() -> Bar:
    b = (
        Bar(init_opts=opts.InitOpts(width="100%",theme=ThemeType.ROMANTIC))
            .set_colors("#df9464")
            .add_xaxis(city)
            .add_yaxis("累计病例TOP10", cumulative, category_gap="50%")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国确诊城市TOP10", subtitle=""))
    )
    return b

def tree_hubei() -> Tree:
    c = (
        Tree(init_opts=opts.InitOpts(width="50%", height="520px",theme=ThemeType.ROMANTIC))
            .add("",list_2)
            .set_global_opts(title_opts=opts.TitleOpts(title="湖北疫情城市TOP10"))
    )
    return c

def line_hubei() -> Line:
    d = (
        Line(init_opts=opts.InitOpts(width="50%", height="520px",theme=ThemeType.ROMANTIC))
            .add_xaxis(name2)
            .add_yaxis("死亡率(%)",
                       num2,
                       symbol="triangle",
                       symbol_size=20,
                       linestyle_opts=opts.LineStyleOpts(color="#df9464", width=4, type_="dashed"),
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
            ), )
    )
    return d


def wordcolud_china() -> WordCloud:
    e = (
        WordCloud(init_opts=opts.InitOpts(width="100%",height="600px",theme=ThemeType.ROMANTIC))
        .add(series_name="疫情分析", data_pair=data_list_2, word_size_range=[40, 100])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="中国各地区新增情况", title_textstyle_opts=opts.TextStyleOpts(font_size=20)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return e


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        map_china(),
        bar_china(),
        tree_hubei(),
        line_hubei(),
        wordcolud_china()
    )
    page.render("../可视化/中国组合图表顺序排列.html")


if __name__ == "__main__":
    page_simple_layout()