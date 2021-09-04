import streamlit as st
import hashlib
import json
import requests
import configparser


def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

def get_proxy(config):
    verify = True
    proxies = None

    if config["proxy"].getboolean("proxy"):
        proxies = {
            "http": config["proxy"]["http"],
            "https": config["proxy"]["https"]
        }
        verify = False

    return proxies, verify

def sign_up_or_in(uri, email, password, config):
    headers = {"Content-type": "application/json"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    proxies, verify = get_proxy(config)

    result = requests.post(url=uri,
                           headers=headers,
                           data=data,
                           proxies=proxies,
                           verify=verify)
    return result.json()


def page(action):
    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    api_key = config["firebase_config"]["api_key"]

    if action == "up":
        title = "新規ユーザー登録"
        uri = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"
    if action == "in":
        title = "ログイン"
        uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={api_key}"


    st.title(title)
    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")

    is_button_pushed = st.button(title)
    if is_button_pushed:
        user_info = sign_up_or_in(uri, email, password, config)
        print(user_info)
        if "error" not in user_info.keys():
            st.session_state["idToken"] = user_info["idToken"]
            st.success(f"{title}しました")
        else:
            st.error(user_info["error"]["errors"][0]["message"])