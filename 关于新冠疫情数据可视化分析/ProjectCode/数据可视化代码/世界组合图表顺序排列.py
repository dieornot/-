import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie,Map,Page,Funnel
from pyecharts.globals import ThemeType

data_1 = pd.read_csv('../疫情数据/全球疫情数据.csv')
data_1.columns = ['country','newly_add','cumulative','cure','death']
# print(data.head())
data_1['newly_add'] = data_1['newly_add'].astype(np.int64)
data_1['cumulative'] = data_1['cumulative'].astype(np.int64)
data_1['cure'] = data_1['cure'].astype(np.int64)
data_1['death'] = data_1['death'].astype(np.int64)
# print(data.info())
country_list = data_1['country']
cumulative_list = data_1['cumulative']

# 将列名改成英文
data_1.columns = ['country', 'add', 'cumulative', 'recovered', 'deaths']
data_1.reset_index(drop=True,inplace=True)
data_1['cumulative'] = data_1['cumulative'].astype(np.int64)
# df.info()
# [('key','value')]
data_2 = data_1.groupby('country')['cumulative'].mean()
name_1 = data_2.sort_values(ascending=False)[:10].index.tolist()
num_1 = data_2.sort_values(ascending=False)[:10].values.tolist()
data_pair_1 = [i for i in zip(name_1, num_1)]

data_3 = data_1.groupby('country')['deaths'].mean()
name_2 = (data_3.sort_values(ascending=False)[:5]).index.tolist()
num_2 = (data_3.sort_values(ascending=False)[:5]).values.tolist()


nameMap = {
        'Singapore Rep.':'新加坡',
        'Dominican Rep.':'多米尼加',
        'Palestine':'巴勒斯坦',
        'Bahamas':'巴哈马',
        'Timor-Leste':'东帝汶',
        'Afghanistan':'阿富汗',
        'Guinea-Bissau':'几内亚比绍',
        "Côte d'Ivoire":'科特迪瓦',
        'Siachen Glacier':'锡亚琴冰川',
        "Br. Indian Ocean Ter.":'英属印度洋领土',
        'Angola':'安哥拉',
        'Albania':'阿尔巴尼亚',
        'United Arab Emirates':'阿拉伯联合酋长国',
        'Argentina':'阿根廷',
        'Armenia':'亚美尼亚',
        'French Southern and Antarctic Lands':'法属南半球和南极领地',
        'Australia':'澳大利亚',
        'Austria':'奥地利',
        'Azerbaijan':'阿塞拜疆',
        'Burundi':'布隆迪',
        'Belgium':'比利时',
        'Benin':'贝宁',
        'Burkina Faso':'布基纳法索',
        'Bangladesh':'孟加拉国',
        'Bulgaria':'保加利亚',
        'The Bahamas':'巴哈马',
        'Bosnia and Herz.':'波斯尼亚和黑塞哥维那',
        'Belarus':'白俄罗斯',
        'Belize':'伯利兹',
        'Bermuda':'百慕大',
        'Bolivia':'玻利维亚',
        'Brazil':'巴西',
        'Brunei':'文莱',
        'Bhutan':'不丹',
        'Botswana':'博茨瓦纳',
        'Central African Rep.':'中非共和国',
        'Canada':'加拿大',
        'Switzerland':'瑞士',
        'Chile':'智利',
        'China':'中国',
        'Ivory Coast':'象牙海岸',
        'Cameroon':'喀麦隆',
        'Dem. Rep. Congo':'刚果（布）',
        'Congo':'刚果（布）',
        'Colombia':'哥伦比亚',
        'Costa Rica':'哥斯达黎加',
        'Cuba':'古巴',
        'N. Cyprus':'北塞浦路斯',
        'Cyprus':'塞浦路斯',
        'Czech Rep.':'捷克',
        'Germany':'德国',
        'Djibouti':'吉布提',
        'Denmark':'丹麦',
        'Algeria':'阿尔及利亚',
        'Ecuador':'厄瓜多尔',
        'Egypt':'埃及',
        'Eritrea':'厄立特里亚',
        'Spain':'西班牙',
        'Estonia':'爱沙尼亚',
        'Ethiopia':'埃塞俄比亚',
        'Finland':'芬兰',
        'Fiji':'斐济',
        'Falkland Islands':'福克兰群岛',
        'France':'法国',
        'Gabon':'加蓬',
        'United Kingdom':'英国',
        'Georgia':'格鲁吉亚',
        'Ghana':'加纳',
        'Guinea':'几内亚',
        'Gambia':'冈比亚',
        'Guinea Bissau':'几内亚比绍',
        'Eq. Guinea':'赤道几内亚',
        'Greece':'希腊',
        'Greenland':'格陵兰岛',
        'Guatemala':'危地马拉',
        'French Guiana':'法属圭亚那',
        'Guyana':'圭亚那合作共和国',
        'Honduras':'洪都拉斯',
        'Croatia':'克罗地亚',
        'Haiti':'海地',
        'Hungary':'匈牙利',
        'Indonesia':'印度尼西亚',
        'India':'印度',
        'Ireland':'爱尔兰',
        'Iran':'伊朗',
        'Iraq':'伊拉克',
        'Iceland':'冰岛',
        'Israel':'以色列',
        'Italy':'意大利',
        'Jamaica':'牙买加',
        'Jordan':'约旦',
        'Japan':'日本',
        'Kazakhstan':'哈萨克斯坦',
        'Kenya':'肯尼亚',
        'Kyrgyzstan':'吉尔吉斯斯坦',
        'Cambodia':'柬埔寨',
        'Korea':'韩国',
        'Kosovo':'科索沃',
        'Kuwait':'科威特',
        'Lao PDR':'老挝',
        'Lebanon':'黎巴嫩',
        'Liberia':'利比里亚',
        'Libya':'利比亚',
        'Sri Lanka':'斯里兰卡',
        'Lesotho':'莱索托',
        'Lithuania':'立陶宛',
        'Luxembourg':'卢森堡',
        'Latvia':'拉脱维亚',
        'Morocco':'摩洛哥',
        'Moldova':'摩尔多瓦',
        'Madagascar':'马达加斯加',
        'Mexico':'墨西哥',
        'Macedonia':'北马其顿',
        'Mali':'马里',
        'Myanmar':'缅甸',
        'Montenegro':'黑山',
        'Mongolia':'蒙古国',
        'Mozambique':'莫桑比克',
        'Mauritania':'毛里塔尼亚',
        'Malawi':'马拉维',
        'Malaysia':'马来西亚',
        'Namibia':'纳米比亚',
        'New Caledonia':'新喀里多尼亚',
        'Niger':'尼日尔',
        'Nigeria':'尼日利亚',
        'Nicaragua':'尼加拉瓜',
        'Netherlands':'荷兰',
        'Norway':'挪威',
        'Nepal':'尼泊尔',
        'New Zealand':'新西兰',
        'Oman':'阿曼',
        'Pakistan':'巴基斯坦',
        'Panama':'巴拿马',
        'Peru':'秘鲁',
        'Philippines':'菲律宾',
        'Papua New Guinea':'巴布亚新几内亚',
        'Poland':'波兰',
        'Puerto Rico':'波多黎各',
        'Dem. Rep. Korea':'朝鲜',
        'Portugal':'葡萄牙',
        'Paraguay':'巴拉圭',
        'Qatar':'卡塔尔',
        'Romania':'罗马尼亚',
        'Russia':'俄罗斯',
        'Rwanda':'卢旺达',
        'W. Sahara':'西撒哈拉',
        'Saudi Arabia':'沙特阿拉伯',
        'Sudan':'苏丹',
        'S. Sudan':'南苏丹',
        'Senegal':'塞内加尔',
        'Solomon Is.':'所罗门群岛',
        'Sierra Leone':'塞拉利昂',
        'El Salvador':'萨尔瓦多',
        'Somaliland':'索马里兰',
        'Somalia':'索马里',
        'Serbia':'塞尔维亚',
        'Suriname':'苏里南',
        'Slovakia':'斯洛伐克',
        'Slovenia':'斯洛文尼亚',
        'Sweden':'瑞典',
        'Swaziland':'斯威士兰',
        'Syria':'叙利亚',
        'Chad':'乍得',
        'Togo':'多哥',
        'Thailand':'泰国',
        'Tajikistan':'塔吉克斯坦',
        'Turkmenistan':'土库曼斯坦',
        'East Timor':'东帝汶',
        'Trinidad and Tobago':'特立尼达和多巴哥',
        'Tunisia':'突尼斯',
        'Turkey':'土耳其',
        'Tanzania':'坦桑尼亚',
        'Uganda':'乌干达',
        'Ukraine':'乌克兰',
        'Uruguay':'乌拉圭',
        'United States':'美国',
        'Uzbekistan':'乌兹别克斯坦',
        'Venezuela':'委内瑞拉',
        'Vietnam':'越南',
        'Vanuatu':'瓦努阿图共和国',
        'West Bank':'西岸',
        'Yemen':'也门',
        'South Africa':'南非',
        'Zambia':'赞比亚',
        'Zimbabwe':'津巴布韦'
    }
def map_world() -> Map:
        a = (
                Map(init_opts=opts.InitOpts(width="100%", height="800px", theme=ThemeType.ROMANTIC))
                        .add(series_name="累计确诊人数", data_pair=[i for i in zip(country_list, cumulative_list)],
                             maptype="world", is_map_symbol_show=False, name_map=nameMap)
                        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                        .set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0, max_=5000000,pos_top="40%"),
                                         title_opts=opts.TitleOpts(title="全球疫情数据")
                                         )
        )
        return a
def pie_world() -> Pie:
        b = (
                Pie(init_opts=opts.InitOpts(width="49%", height="700px",theme=ThemeType.ROMANTIC))
                .add("",data_pair_1,radius=["25%", "70%"],rosetype="radius")
                .set_colors(["SandyBrown ", "LightSteelBlue  ", "LightGreen ", "LightPink", "LightSalmon ",
                             "LightSeaGreen ", "LightSkyBlue", "LightSlateBlue ", "LightSlateGray ", "SlateGray"])
                .set_global_opts(title_opts=opts.TitleOpts(title="Pie-blue"))
                .set_global_opts(title_opts=opts.TitleOpts(title="世界各国确诊人数TOP10", pos_left="30%"),legend_opts=opts.LegendOpts(
                                orient="vertical",
                                pos_left="5%",
                                pos_top="10%"
                        )
                )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
        )
        return b
def funnel_world() -> Funnel:
        c = (
                Funnel(init_opts=opts.InitOpts(width="51%", height="700px", theme=ThemeType.ROMANTIC))
                        .add(
                        series_name="死亡人数",
                        data_pair=[list(z) for z in zip(name_2, num_2)],  # 使用zip将两个序列组合成一个序列
                        gap=2,
                        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}人"),
                        label_opts=opts.LabelOpts(is_show=True, position="inside"),
                        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
                )

                        .set_global_opts(
                        title_opts=opts.TitleOpts(title="全球死亡人数TOP5", subtitle="截至到2021/10/27"),
                        visualmap_opts=opts.VisualMapOpts(min_=200000, max_=800000, pos_top="40%")

                )
        )
        return c

def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        map_world(),
        pie_world(),
        funnel_world()
    )
    page.render("../可视化/世界组合图表顺序排列.html")


if __name__ == "__main__":
    page_simple_layout()