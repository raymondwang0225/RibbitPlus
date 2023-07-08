import streamlit as st

# 定義觸發的函數
def on_link_click():
    st.write('連結被點擊了')
    # 在此處加入您希望觸發的 Streamlit 邏輯

# 顯示 Streamlit 按鈕，設定樣式為看起來像連結
link_style = '''
    background: none;
    border: none;
    padding: 0;
    color: blue;
    text-decoration: underline;
    cursor: pointer;
'''

if st.button('Home', help='連結', unsafe_allow_html=True, key='link_button', on_click=on_link_click):
    pass  # 無需執行任何操作，僅為確保按鈕顯示

# 透過 CSS 設定按鈕樣式
st.markdown(f'<style>{link_style}</style>', unsafe_allow_html=True)
