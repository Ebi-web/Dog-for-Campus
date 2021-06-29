import streamlit as st
import scraping as sc
import select_page as sp

def page():
    result_dict = {}

    st.title("対象サイトの情報更新")
    is_updated = st.button('更新を実行')
    if is_updated:
        result_dict = sc.main()
        st.write("更新を実行しました")
    return result_dict