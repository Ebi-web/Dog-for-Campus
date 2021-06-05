# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests



def zengaku_kyomuka_li_tags():
    zengaku_kyomuka_url = "http://www2.he.tohoku.ac.jp/zengaku/zengaku_info_g.html"
    zengaku_kyomuka_res = requests.get(zengaku_kyomuka_url)
    soup = BeautifulSoup(zengaku_kyomuka_res.content, "html.parser")
    zengaku_kyomuka_content = soup.select_one("#content_box")
    zengaku_kyomuka_li = zengaku_kyomuka_content.select("li")
    return zengaku_kyomuka_li

def zengaku_guide_html():
    zengaku_guide_url = "http://www2.he.tohoku.ac.jp/zengaku/zengaku_annai.html"
    zengaku_guide_res = requests.get(zengaku_guide_url)
    soup = BeautifulSoup(zengaku_guide_res.content, "html.parser")
    zengaku_guide_content = soup.select_one("#content_box")
    zengaku_guide_index = zengaku_guide_content.select_one("#page-index3")
    return zengaku_guide_index

def main():
    return {
        "zengaku_kyomuka_li_tags": zengaku_kyomuka_li_tags(),
        "zengaku_guide_html": zengaku_guide_html(),
    }


if __name__ == "__main__":
    print(main())