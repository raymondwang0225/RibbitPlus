import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lightweight_charts import renderLightweightCharts
import pandas as pd
import plost
import json;

priceVolumeSeriesArea = [
    { "time": '2019-03-01', "value": 56.96 },
    { "time": '2019-03-04', "value": 56.24 },
    { "time": '2019-03-05', "value": 56.08 },
    { "time": '2019-03-06', "value": 55.68 },
    { "time": '2019-03-07', "value": 56.30 },
    { "time": '2019-03-08', "value": 56.53 },
    { "time": '2019-03-11', "value": 57.58 },
    { "time": '2019-03-12', "value": 57.43 },
    { "time": '2019-03-13', "value": 57.66 },
    { "time": '2019-03-14', "value": 57.95 },
    { "time": '2019-03-15', "value": 58.39 },
    { "time": '2019-03-18', "value": 58.07 },
    { "time": '2019-03-19', "value": 57.50 },
    { "time": '2019-03-20', "value": 57.67 },
    { "time": '2019-03-21', "value": 58.29 },
    { "time": '2019-03-22', "value": 59.76 },
    { "time": '2019-03-25', "value": 60.08 },
    { "time": '2019-03-26', "value": 60.63 },
    { "time": '2019-03-27', "value": 60.88 },
    { "time": '2019-03-28', "value": 59.08 },
    { "time": '2019-03-29', "value": 59.13 },
    { "time": '2019-04-01', "value": 59.09 },
    { "time": '2019-04-02', "value": 58.53 },
    { "time": '2019-04-03', "value": 58.87 },
    { "time": '2019-04-04', "value": 58.99 },
    { "time": '2019-04-05', "value": 59.09 },
    { "time": '2019-04-08', "value": 59.13 },
    { "time": '2019-04-09', "value": 58.40 },
    { "time": '2019-04-10', "value": 58.61 },
    { "time": '2019-04-11', "value": 58.56 },
    { "time": '2019-04-12', "value": 58.74 },
    { "time": '2019-04-15', "value": 58.71 },
    { "time": '2019-04-16', "value": 58.79 },
    { "time": '2019-04-17', "value": 57.78 },
    { "time": '2019-04-18', "value": 58.04 },
    { "time": '2019-04-22', "value": 58.37 },
    { "time": '2019-04-23', "value": 57.15 },
    { "time": '2019-04-24', "value": 57.08 },
    { "time": '2019-04-25', "value": 55.85 },
    { "time": '2019-04-26', "value": 56.58 },
    { "time": '2019-04-29', "value": 56.84 },
    { "time": '2019-04-30', "value": 57.19 },
    { "time": '2019-05-01', "value": 56.52 },
    { "time": '2019-05-02', "value": 56.99 },
    { "time": '2019-05-03', "value": 57.24 },
    { "time": '2019-05-06', "value": 56.91 },
    { "time": '2019-05-07', "value": 56.63 },
    { "time": '2019-05-08', "value": 56.38 },
    { "time": '2019-05-09', "value": 56.48 },
    { "time": '2019-05-10', "value": 56.91 },
    { "time": '2019-05-13', "value": 56.75 },
    { "time": '2019-05-14', "value": 56.55 },
    { "time": '2019-05-15', "value": 56.81 },
    { "time": '2019-05-16', "value": 57.38 },
    { "time": '2019-05-17', "value": 58.09 },
    { "time": '2019-05-20', "value": 59.01 },
    { "time": '2019-05-21', "value": 59.50 },
    { "time": '2019-05-22', "value": 59.25 },
    { "time": '2019-05-23', "value": 58.87 },
    { "time": '2019-05-24', "value": 59.32 },
    { "time": '2019-05-28', "value": 59.57 },
]

priceVolumeSeriesHistogram = [
    { "time": '2019-03-01', "value": 10942737.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-04', "value": 13674737.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-05', "value": 15749545.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-06', "value": 13935530.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-07', "value": 12644171.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-08', "value": 10646710.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-11', "value": 13627431.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-12', "value": 12812980.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-13', "value": 14168350.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-14', "value": 12148349.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-15', "value": 23715337.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-18', "value": 12168133.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-19', "value": 13462686.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-20', "value": 11903104.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-21', "value": 10920129.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-22', "value": 25125385.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-25', "value": 15463411.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-26', "value": 12316901.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-27', "value": 13290298.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-28', "value": 20547060.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-29', "value": 17283871.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-01', "value": 16331140.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-02', "value": 11408146.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-03', "value": 15491724.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-04', "value": 8776028.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-05', "value": 11497780.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-08', "value": 11680538.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-09', "value": 10414416.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-10', "value": 8782061.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-11', "value": 9219930.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-12', "value": 10847504.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-15', "value": 7741472.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-16', "value": 10239261.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-17', "value": 15498037.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-18', "value": 13189013.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-22', "value": 11950365.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-23', "value": 23488682.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-24', "value": 13227084.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-25', "value": 17425466.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-26', "value": 16329727.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-29', "value": 13984965.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-30', "value": 15469002.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-01', "value": 11627436.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-02', "value": 14435436.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-03', "value": 9388228.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-06', "value": 10066145.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-07', "value": 12963827.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-08', "value": 12086743.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-09', "value": 14835326.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-10', "value": 10707335.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-13', "value": 13759350.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-14', "value": 12776175.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-15', "value": 10806379.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-16', "value": 11695064.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-17', "value": 14436662.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-20', "value": 20910590.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-21', "value": 14016315.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-22', "value": 11487448.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-23', "value": 11707083.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-24', "value": 8755506.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-28', "value": 3097125.00, "color": 'rgba(0, 150, 136, 0.8)' }
]


_avg=[{"time": "2023-07-18", "value": 3162395.0625}, {"time": "2023-07-17", "value": 3480656.785714286}, {"time": "2023-07-16", "value": 3732523.066666667}, {"time": "2023-07-15", "value": 3696231.8571428573}, {"time": "2023-07-14", "value": 3788935.283950617}, {"time": "2023-07-13", "value": 3795865.316666667}, {"time": "2023-07-12", "value": 3121380.177777778}, {"time": "2023-07-11", "value": 2790823.294117647}, {"time": "2023-07-10", "value": 2692789.6923076925}, {"time": "2023-07-09", "value": 2815280.5833333335}, {"time": "2023-07-08", "value": 2816558.378378378}, {"time": "2023-07-07", "value": 2810661.2}, {"time": "2023-07-06", "value": 3062088.9545454546}, {"time": "2023-07-05", "value": 3203008.6818181816}, {"time": "2023-07-04", "value": 3111246.3846153845}, {"time": "2023-07-03", "value": 2714856.222222222}, {"time": "2023-07-02", "value": 3335712.763157895}, {"time": "2023-07-01", "value": 3836690.222222222}, {"time": "2023-06-30", "value": 3992298.42}, {"time": "2023-06-29", "value": 4395121.787234043}, {"time": "2023-06-28", "value": 3575398.435483871}, {"time": "2023-06-27", "value": 4049133.536585366}, {"time": "2023-06-26", "value": 4348968.434782608}, {"time": "2023-06-25", "value": 4100694.0857142857}, {"time": "2023-06-24", "value": 4667687.3513513515}, {"time": "2023-06-23", "value": 5184204.821428572}, {"time": "2023-06-22", "value": 4886640.160714285}, {"time": "2023-06-21", "value": 5097980.181818182}, {"time": "2023-06-20", "value": 5397879.375}, {"time": "2023-06-19", "value": 6158302.660194174}]
_vol=[{"time": "2023-07-18", "value": 101196642, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-17", "value": 97458390, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-16", "value": 111975692, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-15", "value": 206988984, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-14", "value": 306903758, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-13", "value": 1138759595, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-12", "value": 702310540, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-11", "value": 474439960, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-10", "value": 175031330, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-09", "value": 337833670, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-08", "value": 521063300, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-07", "value": 632398770, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-06", "value": 336829785, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-05", "value": 352330955, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-04", "value": 1213386090, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-03", "value": 733011180, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-02", "value": 633785425, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-07-01", "value": 517953180, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-30", "value": 998074605, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-29", "value": 1032853620, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-28", "value": 1108373515, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-27", "value": 830072375, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-26", "value": 1000262740, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-25", "value": 717621465, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-24", "value": 863522160, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-23", "value": 725788675, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-22", "value": 1368259245, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-21", "value": 841166730, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-20", "value": 863660700, "color": "rgba(255, 255, 255, 0.8)"}, {"time": "2023-06-19", "value": 634305174, "color": "rgba(255, 255, 255, 0.8)"}]

def clear_multi():
    st.session_state.multiselect_satyears = []
    st.session_state.multiselect_backgrounds = []
    st.session_state.multiselect_clothing = []
    st.session_state.multiselect_bodies = []
    st.session_state.multiselect_mouths = []
    st.session_state.multiselect_eyes = []
    return

past_30_days_avg_data =[]
past_30_days_vol_data =[]
with open('past_30_days_avg.json') as f:
    past_30_days_avg_data = json.load(f)

with open('past_30_days_vol.json') as f:
    past_30_days_vol_data = json.load(f)




with open('bitcoin_frogs_items.json') as f:
    frog_data = json.load(f)

filtered_frogs = []


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)






#st.metric(label="This is a very very very very very long sentence", value="70 °F")
#st.metric(label="This is a very very very very very long sentence", value="70 °F")



st.markdown(
    """
<style>
.sidebar .sidebar-content {
    color: #000000;
}
</style>
""",
    unsafe_allow_html=True,
)

# 属性选项
satyears =["2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
backgrounds = ["Brown", "Red", "Olive", "Grey", "Pink", "Dark Blue", "Orange", "Blue", "Green", "Light Blue", "Bitcoin Orange", "Black", "Yellow"]
clothing = ["Prison Jumpsuit", "Green Hoodie", "Businessman", "Bling", "Wizard Robe", "None", "Leather Jacket", "Leather Dust Coat", "Red Hoodie", "Elvis", "Jersey", "Orange Checkered", "Blue Jacket", "Fur Coat", "23 TShirt", "Black Vest", "Karate Outfit", "Black Hoodie", "Purple Checkered", "Kings Robes", "Vest and Shirt", "Ninja", "Clown", "Priest", "Red Overalls", "Grey Suit", "Blue Hoodie", "Hawaiian", "Hitman", "Yellow Hoodie", "Bowtie", "Bitcoin Shirt", "Gentlemans Suit", "Spartan"]
bodies = ["Spotted", "Electro", "Dark Red", "Green", "Tron"]
mouths = ["Bitcoin Pizza", "None", "Magicians Moustache", "Bubblegum", "Dictators Moustache", "Cigar", "Tongue Out", "Clown Nose", "Big Moustache", "Pipe"]
eyes = ["Dank Shades", "Happy", "Visor", "Monocle", "none", "Frown", "Powerful", "Golden Sunglasses", "Nakamoto Glasses", "Angry", "3D Glasses", "Purple Cosmic Eyes"]


#1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="RIBBIT PLUS",  # required
                options=["Home", "Projects", "Data","Filter","Weekly Report"],  # required
                icons=["house", "book", "bi bi-bar-chart","bi bi-funnel","bi bi-archive"],  # optional
                menu_icon="bi bi-arrow-up-left-square",  # optional
                default_index=0,  # optional
            )
            
            
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        st.title("Ribbit Plus")
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Data","Filter","Weekly Report"],  # required
            icons=["house", "book", "bi bi-bar-chart","bi bi-funnel","bi bi-archive"],  # optional
            menu_icon="bi bi-arrow-up-left-square",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"You have selected {selected}")
    # Row B
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
    
    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Heatmap')
        plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color="2e8eee",
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True)
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=stocks,
            theta='q2',
            color='company',
            legend='bottom', 
            use_container_width=True)
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Data":
    st.title("Bitcoin Frogs") 
    st.markdown('##### Items 10K  ·  Created Mar 2023  ·  Free Mint  ·  Chain Bitcoin') 
    #st.write('Items 10K  ·  Created Mar 2023  ·  Free Mint  ·  Chain Bitcoin') 
    st.write('Bitcoin Frogs are 10,000 pure digital collectibles that will remain on Bitcoin forever. No more will ever be created. Rarities of all traits within each layer are equal, allowing subjective appreciation of aesthetics and satoshi-based rarities to emerge.') 

    aa="""
    <style>
    div[data-testid="metric-container"] {
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 20px 20px 20px 20px;
    border-radius: 12px;
    color: rgb(255, 255, 255);
    }
    }
    </style>
    """

    st.markdown(aa, unsafe_allow_html=True)

    c1,c2,c3,c4,c5,c6 = st.columns(6)
    with c1:
        st.metric(label="total volume", value="453.2698")
    with c2:
        st.metric(label="floor price", value="0.027")
    with c3:
        st.metric(label="listed", value="972")
    with c4:
        st.metric(label="listed %", value="0.97%")
    with c5:
        st.metric(label="owners", value="4412")
    with c6:
        st.metric(label="unique owners", value="44.12%")
    #st.title(f"You have selected {selected}")




    priceVolumeChartOptions = {
        "height": 400,
        "localization": { 
            "dateFormat": "yyyy-MM-dd",
            },
        "rightPriceScale": {
            "scaleMargins": {
                "top": 0.2,
                "bottom": 0,
            },
            "borderVisible": False,
        },
        "overlayPriceScales": {
            "scaleMargins": {
                "top": 0.7,
                "bottom": 0,
            }
        },
        "layout": {
            "background": {
                "type": 'solid',
                "color": '#000000'
            },
            "textColor": '#d1d4dc',
        },
        "grid": {
            "vertLines": {
                "color": 'rgba(42, 46, 57, 0)',
            },
            "horzLines": {
                "color": 'rgba(42, 46, 57, 0.6)',
            }
        }
    }

    priceVolumeSeries = [
        {
            "type": 'Area',
            "data": _avg,
            "options": {
                "topColor": 'rgba(75,132,255, 0.56)',
                "bottomColor": 'rgba(75,132,255, 0.04)',
                "lineColor": 'rgba(75,132,255, 1)',
                "lineWidth": 2,
            }
        },
        {
            "type": 'Histogram',
            "data": _vol,
            "options": {
                "color": '#4b84ff',
                "priceFormat": {
                    "type": 'volume',
                },
                "priceScaleId": "" # set as an overlay setting,
            },
            "priceScale": {
                "scaleMargins": {
                    "top": 0.7,
                    "bottom": 0,
                }
            }
        }
    ]
    st.subheader("Price with Volume Series Chart sample")

    renderLightweightCharts([
        {
            "chart": priceVolumeChartOptions,
            "series": priceVolumeSeries
        }
    ], 'priceAndVolume')






if selected == "Filter":
    

    st.title("Filter")
    #st.markdown("<hr/>", unsafe_allow_html = True)
    #with st.expander("Condition",True):
    col1, col2 ,col3, col4 , col5 ,col6 = st.columns([0.75,1,1,1,1,1])

    with col1:
        desired_satyears = st.multiselect("Sat Year", satyears, key="multiselect_satyears")
    with col2:
    # 应用过滤器并获取最终结果
        desired_backgrounds = st.multiselect("Background", backgrounds, key="multiselect_backgrounds")
    with col3:
        desired_clothing = st.multiselect("Clothing", clothing, key="multiselect_clothing")
    with col4:
        desired_bodies = st.multiselect("Body", bodies, key="multiselect_bodies")
    with col5:
        desired_mouths = st.multiselect("Mouth", mouths, key="multiselect_mouths")
    with col6:
        desired_eyes = st.multiselect("Eyes", eyes, key="multiselect_eyes")


    column_value = st.slider("Column display quantity",help="Column display quantity", min_value=1, max_value=11, value=10, step=1)
    
    col_01,col_02,col_03 = st.columns([4,1,1])
    #with col_01:
        #sort_select = st.selectbox("Column display quantity", ("None","Inscription #: Low to High", "Inscription #: High to Low", "Sat blocktime #: Low to High","Sat blocktime #: High to Low"),label_visibility="hidden")
    
    with col_01:
    # 创建一个滑动条
        st.empty()
        #column_value = st.selectbox("Column display quantity", (1, 2, 3,4,5,6,7,8,9,10,11), index=9,label_visibility="hidden")
    
    #col_03,col_04 = st.columns([1,1])
    with col_02:
        clear_filter = st.button("Clear Filter", on_click=clear_multi,use_container_width=True)
    with col_03:
    # "Apply Filter" 按钮
        apply_filter = st.button("Apply Filter",use_container_width=True)   
   
   
    
    
    if apply_filter:
            # 根据条件过滤人物
            filtered_frogs = [frog for frog in frog_data if
                            (not desired_satyears or frog["sat_year"]  in desired_satyears) and
                            (not desired_backgrounds or frog["background"]  in desired_backgrounds) and
                            (not desired_bodies or frog["body"] in desired_bodies) and
                            (not desired_clothing or frog["clothing"] in desired_clothing) and  
                            (not desired_mouths or frog["mouth"] in desired_mouths) and
                            (not desired_eyes or frog["eyes"] in desired_eyes)]

            # 显示符合条件的人物
            #st.write("Filtered Bitcoin Frogs  :   [ " + str(len(filtered_frogs)) + " ] Frogs")
            st.write("Result  :   [ " + str(len(filtered_frogs)) + " ] Frogs")
            for frog in filtered_frogs:
                frog["image_url"] = 'https://ordiscan.com/content/'+str(frog["inscription_id"])
                frog["me_link"] = "https://magiceden.io/ordinals/item-details/" + str(frog["inscription_id"])
                #st.write(frog)
                #st.image('https://ordiscan.com/content/'+str(frog["inscription_id"]), caption=frog["item_name"],width=576/2)

        
            
            # 定义每列的宽度
            col_width = column_value
            
            # 间距的像素值
            #spacing = 200  

            # 创建网格布局
            cols = st.columns(col_width)
            # 显示图片
            for i, frog in enumerate(filtered_frogs):
                with cols[i % col_width]:
                    link_url = frog["me_link"]
                    link_name = frog["item_name"] 
                    caption = f"[{link_name}]({link_url})"
                    
                    #st.image(frog["image_url"],width=576/4)
                    
                    image = st.image(frog["image_url"],use_column_width = True)
                    st.markdown(caption, unsafe_allow_html=True)
                    # 顯示動態內容的標題


