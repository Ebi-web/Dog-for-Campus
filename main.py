import streamlit as st
st.set_page_config(layout="wide")

import select_page as page1
import show_page as page2
import scraping_page as page3

query_params = st.experimental_get_query_params()
pages = {
    "対象サイトの選択": page1.page,
    "新着情報一覧":  page2.page,
    "更新の実行": page3.page,
}

if not "activity" in query_params:
    query_params["activity"] = []

st.sidebar.title('ページの一覧')
selection = st.sidebar.radio("" ,list(pages.keys()))
if selection == "対象サイトの選択":
    is_scraping_list = pages[selection]()
elif selection == "新着情報一覧":
    pages[selection](query_params["activity"])
elif selection == "更新の実行" :
    st.experimental_set_query_params(activity=pages[selection]())