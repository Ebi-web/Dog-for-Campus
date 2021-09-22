import streamlit as st
import userGuide as page1
import sign_up_in as page2
import reset_page as page3
import register_page as page4
import select_page as page5
import show_page as page6


st.set_page_config(layout="wide")

def margin(num):
    for i in range(num):
        st.write("")
def header(is_signed_in, header_dict):
    COLUMNS_NUM = 3
    columns = st.columns(COLUMNS_NUM)
    with columns[0]:
        st.subheader(f"ようこそ、{st.session_state['name']}さん")
    if is_signed_in:
        with columns[1]:
            def sign_out():
                del st.session_state["email"]
                del st.session_state["name"]
                st.session_state["page"] = 0
                st.session_state["counter"] += 1
                st.session_state["header_dict"] = {
                    "message": "ログアウトしました",
                    "style": "info"
                }
            st.button("ログアウト", on_click=sign_out)
    if header_dict:
        if header_dict["style"] == "success":
            st.success(header_dict["message"])
        elif header_dict["style"] == "error":
            st.error(header_dict["message"])
        elif header_dict["style"] == "warning":
            st.warning(header_dict["message"])
        elif header_dict["style"] == "info":
            st.info(header_dict["message"])
        st.session_state["header_dict"] = None
    margin(3)

pages = {
    "ヘルプ": page1.page,
    "新規登録": page2.page,
    "ログイン": page2.page,
    "パスワードの再設定": page3.page,
    "対象サイトの登録": page4.page,
    "対象サイトの選択/サイト内容の取得": page5.page,
    "取得結果一覧": page6.page,
}

if "name" not in st.session_state:
    st.session_state["name"] = "ゲスト"
if "sites" not in st.session_state:
    st.session_state["sites"] = {}
if "scraping_result_dict" not in st.session_state:
    st.session_state["scraping_result_dict"] = {}
if "email" not in st.session_state:
    st.session_state["is_signed_in"] = False
    del pages["対象サイトの登録"]
else:
    st.session_state["is_signed_in"] = True
if "page" not in st.session_state:
    st.session_state["page"] = 0
if "is_register_opened" not in st.session_state:
    st.session_state["is_register_opened"] = False
if "is_reset_opened" not in st.session_state:
    st.session_state["is_reset_opened"] = False
if "header_dict" not in st.session_state:
    st.session_state["header_dict"] = None
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

st.sidebar.title("ページの一覧")
page_index = st.session_state["page"]
counter = str(st.session_state["counter"])
selection = st.sidebar.radio("", list(pages.keys()), index=page_index, key=counter)


header(st.session_state["is_signed_in"], st.session_state["header_dict"])
if selection == "新規登録":
    pages[selection]("up")
elif selection == "ログイン":
    pages[selection]("in")
else:
    pages[selection]()