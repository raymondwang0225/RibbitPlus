import streamlit as st
import pandas as pd

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Ribbit Plus</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">Analytics</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Filter</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Weekly Report</a>
      </li>
      <li class="nav-item">
    <a class="nav-link" href="javascript: void(0);" onclick="triggerWeeklyReport()">Weekly Report</a>
</li>
<script>
    function triggerWeeklyReport() {
        // 呼叫 Streamlit 函數
        show_weekly_report()
    }
</script>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

'''
st.markdown('''# **Version Test**
A simple template
''')

st.header('**Version Test**')
'''
# 定義觸發的函數
def show_weekly_report():
    # 在此處加入您想要的內容變化
    st.write('這是 Weekly Report 的內容')

