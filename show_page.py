import streamlit as st
import bs4
import re
import datetime as dt
from dateutil.relativedelta import relativedelta


def page():
    st.title("取得結果一覧")
    ranges = ["1週間", "1か月", "半年", "1年", "全て"]
    range_text = st.selectbox("表示期間", ranges)
    range_convert = {
        "1週間": relativedelta(weeks=1), 
        "1か月": relativedelta(months=1),
        "半年": relativedelta(months=6), 
        "1年": relativedelta(years=1), 
        "全て": relativedelta(years=1000)
    }
    r = range_convert[range_text]
    today = dt.datetime.today()
    if True not in st.session_state["sites"].values():
        st.warning("内容を取得したいサイトを選択してください")
    elif st.session_state["scraping_result_dict"] == {}:
        st.warning("サイト内容の取得を再実行してください")
    else:
        for (key, news) in st.session_state["scraping_result_dict"].items():
            ex = st.beta_expander(key)
            form = type(news)
            if form == bs4.element.Tag:
                ex.markdown(">" + news.text)
            elif form in (list, bs4.element.ResultSet, dict):
                if form == dict:
                    news = news.values()
                for n in news:
                    try:
                        try:
                            date_text = re.search(r"[0-9]{4}.[0-9]{1,2}.[0-9]{1,2}", n.text).group()
                        except:
                            date_text = re.search(r"[0-9]{2}.[0-9]{2}", n.text).group()
                            date_text = str(today.year) + "." + date_text
                        try:
                            date = dt.datetime.strptime(date_text, "%Y.%m.%d")
                        except:
                            date = dt.datetime.strptime(date_text, "%Y/%m/%d")
                        if today - r < date:
                                ex.markdown(">" + n.text)
                    except:
                        ex.markdown(">" + n.text)
                        print("!", end="")
            else:
                print("new type", form)
