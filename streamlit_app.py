import streamlit as st

# 定義自訂的 CSS 樣式
custom_css = """
<style>
    /* 在這裡插入你的自訂 CSS 樣式 */
    .colA {
        background-color: lightblue;
        padding: 10px;
        border-radius: 5px;
    }
</style>
"""

# 在 Streamlit 中渲染自訂的 CSS 樣式
st.markdown(custom_css, unsafe_allow_html=True)

# 創建兩個列
colA, colB = st.columns(2)

# 在 colA 中添加內容
with colA:
    # 這裡的內容將套用自訂 CSS 樣式
    st.write("這是 colA 中的內容")

# 在 colB 中添加內容
with colB:
    # 這裡的內容將保持預設樣式
    st.write("這是 colB 中的內容")
