#coding:utf-8
import streamlit as st

# 页面设置
st.set_page_config(
    page_title = "overload",   
    page_icon = "random",        
    layout = "centered",         
    initial_sidebar_state = "auto",  
)

# 去掉右上角目录按钮
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown('笑寒是猪')