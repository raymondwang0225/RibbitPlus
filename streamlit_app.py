import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plost
import json;




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

def callback_filter():
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
if selected == "Filter":
    

    st.title("Filter")
    #st.markdown("<hr/>", unsafe_allow_html = True)
    with st.expander("Condition",True):
        col1, col2 ,col3, col4 , col5 ,col6 = st.columns([0.75,1,1,1,1,1])
    
        with col1:
            desired_satyears = st.multiselect("Sat Year", satyears)
        
        
        with col2:
        # 应用过滤器并获取最终结果
            desired_backgrounds = st.multiselect("Background", backgrounds,on_change= callback_filter)
        with col3:
            desired_clothing = st.multiselect("Clothing", clothing,on_change= callback_filter)
        with col4:
            desired_bodies = st.multiselect("Body", bodies,on_change= callback_filter)
        with col5:
            desired_mouths = st.multiselect("Mouth", mouths,on_change= callback_filter)
        with col6:
            desired_eyes = st.multiselect("Eyes", eyes,on_change= callback_filter)

    
    col_01,col_02,col_03 = st.columns([5,1.5,1.5])
    with col_01:
        text_input = st.text_input(
        "Enter some text 👇",
        label_visibility="hidden",
        placeholder="Search by name or trait",)
        
    with col_02:
        sort_select = st.selectbox("Column display quantity", ("None","Inscription #: Low to High", "Inscription #: High to Low", "Sat blocktime #: Low to High","Sat blocktime #: High to Low"),label_visibility="hidden")
    
    with col_03:
    # 创建一个滑动条
    #column_value = st.slider("Column display quantity", min_value=1, max_value=11, value=10, step=1)
        column_value = st.selectbox("Column display quantity", (1, 2, 3,4,5,6,7,8,9,10,11),label_visibility="hidden")
