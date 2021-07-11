from requests.sessions import session
import streamlit as st

st.set_page_config(layout="wide")

import select_page as page1
import show_page as page2

pages = {
    "対象サイトの選択/サイト内容の取得": page1.page,
    "取得結果一覧": page2.page,
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
