import streamlit as st
st.set_page_config(layout="wide")

from select_page import page1
from show_page import page2
from scraping_page import page3


pages = {
    "対象サイトの選択": page1,
    "新着情報一覧":  page2,
    "更新の実行": page3,
}
st.sidebar.title('ページの一覧')
selection = st.sidebar.radio("" ,list(pages.keys()))
if selection == 1:
    is_scraping_list = pages[selection]()
else :
    pages[selection]()