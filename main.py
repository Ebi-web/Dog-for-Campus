from soupsieve import select
import streamlit as st
st.set_page_config(layout="wide")

import select_page as page1
import show_page as page2
import scraping_page as page3


pages = {
    "対象サイトの選択": page1.page,
    "新着情報一覧":  page2.page,
    "更新の実行": page3.page,
}



if not "news" in st.session_state:
    st.session_state["news"] = {}
if not "sites" in st.session_state:
    st.session_state["sites"] = {}

st.sidebar.title('ページの一覧')
selection = st.sidebar.radio("", list(pages.keys()))

if selection == "対象サイトの選択":
    is_scraping_list = pages[selection]()
elif selection == "新着情報一覧":
    pages[selection](st.session_state["news"])
elif selection == "更新の実行" :
    news_dict = pages[selection]()
    st.session_state["news"] = news_dict