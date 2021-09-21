import streamlit as st
from select_page import select
from dynamoDB import UserTable



def page():
    title_container = st.beta_container()
    title_container.title("対象サイトの登録")
    title_container = None
    new_binarry_num, sites = select()
    register_button = st.button("対象サイトの登録")
    if register_button:
        user_table = UserTable()
        new_binarry_num = str(new_binarry_num).zfill(sites)[::-1]
        item = {
            "Mail": st.session_state["email"],
            "RegisteredBinaryNum": new_binarry_num
        }
        user_table.update(item)