from requests.sessions import session
import streamlit as st

st.set_page_config(layout="wide")

import userGuide as page1
import select_page as page2
import show_page as page3

pages = {
    "ヘルプ":page1.page,
    "対象サイトの選択/サイト内容の取得": page2.page,
    "取得結果一覧": page3.page,
}

if "scraping_result_dict" not in st.session_state:
    st.session_state["scraping_result_dict"] = {}
if "sites" not in st.session_state:
    st.session_state["sites"] = {}

st.sidebar.title("ページの一覧")
selection = st.sidebar.radio("", list(pages.keys()))

if selection == "対象サイトの選択/サイト内容の取得":
    pages[selection]()
elif selection == "取得結果一覧":
    pages[selection]()
elif selection == "ヘルプ":
    pages[selection]()
