import streamlit as st
import bs4

def page(news_dict):
    st.title("新着情報の一覧")
    for (key, news) in news_dict.items():
        st.write("\n\n")
        st.write(f"----- {key} -----")
        st.write("\n")
        form = type(news)
        if form == bs4.element.Tag:
            st.write(news.text)
        elif form in (list, bs4.element.ResultSet):
            for n in news:
                st.write(n.text)
        elif form == dict:
            for (i, n) in enumerate(news.values()):
                st.write(n.text)
        else:
            print("new type", form)