import streamlit as st
import json
import requests
from select_page import select
from dynamoDB import UserTable


def sign_up_or_in(uri, email, password):
    headers = {"Content-type": "application/json"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    proxies, verify = None, True

    result = requests.post(url=uri,
                           headers=headers,
                           data=data,
                           proxies=proxies,
                           verify=verify)
    return result.json()

def page(action):
    api_key = "AIzaSyBT1i08BZdSTu5-plDvilnFaWqh73NIU9k"

    if action == "up":
        title = "新規ユーザー登録"
        uri = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"
        sign = "すでにアカウントをお持ちの方"
        button_label = "ログインページへ"
        to_page_index = 2
    if action == "in":
        title = "ログイン"
        uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={api_key}"
        sign = "アカウントをお持ちでない方"
        button_label = "新規ユーザー登録ページへ"
        to_page_index = 1


    st.title(title)
    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")
    if action == "up":
        password2 = st.text_input("パスワード（確認用）", type="password")
    else:
        password2 = password
    def sign_in():
        if password == password2:
            user_info = sign_up_or_in(uri, email, password)
            if "error" not in user_info.keys():
                st.session_state["email"] = email
                st.session_state["name"] = email.split("@")[0]
                st.session_state["header_dict"] = {
                    "message": f"{title}しました",
                    "style": "success"
                }
                if action == "up":
                    st.session_state["page"] = 1
                    st.session_state["is_register_opened"] = True
                else:
                    st.session_state["page"] = 0
                    st.session_state["counter"] += 1
            else:
                error = user_info["error"]["errors"][0]["message"]
                if error == "EMAIL_EXISTS":
                    error_text = "このメールアドレスはすでに登録されています"
                elif error == "WEAK_PASSWORD : Password should be at least 6 characters":
                    error_text = "パスワードが短すぎます（6文字以上）"
                elif error == "INVALID_EMAIL":
                    error_text = "このメールアドレスは無効です"
                elif error == "MISSING_PASSWORD":
                    error_text = "パスワードを入力してください"
                elif error == "EMAIL_NOT_FOUND":
                    error_text = "アカウントが登録されていません"
                elif error == "INVALID_PASSWORD":
                    error_text = "パスワードが間違っています"
                elif error == "USER_DISABLED":
                    error_text = "このユーザーアカウントが停止されています"
                else:
                    error_text = error
                st.session_state["header_dict"] = {
                    "message": error_text,
                    "style": "error"
                }
        else:
            st.session_state["header_dict"] = {
                "message": "パスワードが一致していません",
                "style": "error"
            }
    st.button(title, on_click=sign_in)
    if st.session_state["is_register_opened"]:
        for i in range(3):
            st.write("")
        st.session_state["page"] = 1
        st.session_state["counter"] += 1
        title_container = st.beta_container()
        title_container.title("対象サイトの登録")
        title_container = None
        new_binarry_num, sites = select()
        register_button = st.button("対象サイトの登録")
        if register_button:
            user_table = UserTable()
            new_binarry_num = str(new_binarry_num).zfill(sites)[::-1]
            item = {
                "Mail": email,
                "RegisteredBinaryNum": new_binarry_num
            }
            user_table.put(item)
            st.session_state["is_register_opened"] = False

    
    def change_page(page_index):
        st.session_state["page"] = page_index
        st.session_state["counter"] += 1
    ROW = 3
    for i in range(ROW):
        st.write("")
    COLUMNS_NUM = 3
    columns = st.beta_columns(COLUMNS_NUM)
    with columns[0]:
        st.write(sign)
    with columns[1]:
        st.button(button_label, on_click=change_page, kwargs={"page_index": to_page_index})

    if action == "in":
        with columns[0]:
            st.write("パスワードをお忘れの方")
        with columns[1]:
            TO_PAGE_INDEX = 3
            st.button("パスワードの再設定ページへ", on_click=change_page, kwargs={"page_index": TO_PAGE_INDEX})