import streamlit as st

# 定义触发的函数
def on_link_click():
    st.write('链接被点击了')
    # 在此处添加您希望触发的 Streamlit 逻辑

# 在 Streamlit 上显示 Markdown 链接
link_text = 'Home'
link_url = 'javascript: void(0);'
markdown_link = f'<a href="{link_url}" onclick="event.preventDefault(); triggerLinkClick();">{link_text}</a>'
st.markdown(markdown_link, unsafe_allow_html=True)

# 调用触发的函数
if 'on_link_click' in st.session_state:
    on_link_click()
    del st.session_state.on_link_click
