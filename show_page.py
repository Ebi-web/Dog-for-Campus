import streamlit as st


def page(news_dict):
    st.title("新着情報の一覧")
    for news in news_dict:
        st.write(news)