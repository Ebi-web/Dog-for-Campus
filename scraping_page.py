import streamlit as st

def page3():
    st.title("対象サイトの情報の更新")
    left_column, right_column = st.beta_columns(2)
    update = left_column.button('更新を実行')