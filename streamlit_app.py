import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


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
                options=["Home", "Projects", "Contact","Filter","Weekly Report"],  # required
                icons=["house", "book", "envelope","bi bi-chat-square-dots-fill","bi bi-archive"],  # optional
                menu_icon="bi bi-arrow-up-left-square",  # optional
                default_index=0,  # optional
            )
            
            
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        st.title("Ribbit Plus")
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
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
if selected == "Contact":
    st.title(f"You have selected {selected}")
if selected == "Filter":
    

    st.title("Filter")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.multiselect("Background", backgrounds)
        st.multiselect("Clothing", clothing)    
        st.multiselect("Body", bodies)
        st.multiselect("Mouth", mouths)
        st.multiselect("Eyes", eyes)
        # 创建一个滑动条
        column_value = st.sidebar.slider("Column display quantity", min_value=1, max_value=11, value=10, step=1)
        # "Apply Filter" 按钮
        apply_filter = st.sidebar.button("Apply Filter")   
    with col2:
        if apply_filter:
            st.write("2222222")

                       
    
       
            
    

               
   
