import streamlit as st

# 定義觸發的函數
def on_link_click():
    st.write('連結被點擊了')
    # 在此處加入您希望觸發的 Streamlit 邏輯

# 顯示 HTML 元素
html_code = '''
<li class="nav-item active">
    <a class="nav-link disabled" href="javascript:void(0);" onclick="triggerLinkClick()">Home <span class="sr-only">(current)</span></a>
</li>
<script>
    function triggerLinkClick() {
        // 呼叫 Streamlit 函數
        StreamlitApp._enqueueSctiptCall('on_link_click', [], {});
    }
</script>
'''
st.write(html_code, unsafe_allow_html=True)

# 呼叫觸發的函數
if 'on_link_click' in st.session_state:
    on_link_click()
    del st.session_state.on_link_click



