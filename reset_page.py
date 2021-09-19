import streamlit as st
import json
import requests
import configparser


def reset(uri, email):
    headers = {"Content-type": "application/json"}
    data = json.dumps({"requestType": "PASSWORD_RESET", "email": email})
    proxies, verify = None, True

    result = requests.post(url=uri,
                           headers=headers,
                           data=data,
                           proxies=proxies,
                           verify=verify)
    return result.json()


def page():
    title_container = st.beta_container()
    title_container.title("パスワードの再設定")
    title_container = None

    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    api_key = config["firebase_config"]["api_key"]
    uri = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}"

    email = st.text_input("再設定用メールアドレス")
    send_button = st.button("上記メールアドレスへ再設定用リンクを送信")
    if send_button:
        res = reset(uri, email)
        if "error" in res:
            error = res["error"]["message"]
            if error == "EMAIL_NOT_FOUND":
                error_text = "このメールアドレスは登録されていません"
            elif error == "MISSING_EMAIL":
                error_text = "メールアドレスを入力してください"
            elif error == "INVALID_EMAIL":
                error_text = "このメールアドレスは無効です"
            else:
                error_text = error
            st.error(error_text)
        else:
            st.success("送信が完了しました")