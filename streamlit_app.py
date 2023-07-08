import streamlit as st

# 定義自定義 CSS 樣式
css = """
<style>
    /* 在這裡插入你的 CSS 樣式 */
    .my-column {
        background-color: lightblue;
        padding: 10px;
        border-radius: 5px;
    }
</style>
"""

# 在 Streamlit 中渲染自定義 CSS
st.markdown(css, unsafe_allow_html=True)

# 創建兩個 column
col_a, col_b = st.columns(2)

# 在 col A 中套用 CSS 樣式
with col_a:
    st.markdown('<div class="my-column">', unsafe_allow_html=True)
    st.multiselect("選擇項目", ["選項1", "選項2", "選項3"])
    st.multiselect("選擇項目", ["選項1", "選項2", "選項3"])
    st.multiselect("選擇項目", ["選項1", "選項2", "選項3"])
    st.multiselect("選擇項目", ["選項1", "選項2", "選項3"])
    st.markdown('</div>', unsafe_allow_html=True)

# 在 col B 中顯示文字
with col_b:
    st.write("這是 col B")
