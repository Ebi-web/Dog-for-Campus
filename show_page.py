import streamlit as st
import bs4


def page():
    st.title("取得結果一覧")
    if True not in st.session_state["sites"].values():
        st.warning("内容を取得したいサイトを選択してください")
    elif st.session_state["scraping_result_dict"] == {}:
        st.warning("サイト内容の取得を再実行してください")
    else:
        for (key, news) in st.session_state["scraping_result_dict"].items():
            st.write("\n\n")
            st.write("-----" + key + "-----")
            st.write("\n")
            form = type(news)
            if form == bs4.element.Tag:
                st.write(news.text)
            elif form in (list, bs4.element.ResultSet):
                current_index = 1
                for n in news:
                    st.write(n.text)
            elif form == dict:
                for n in news.values():
                    st.write(n.text)
            else:
                print("new type", form)
