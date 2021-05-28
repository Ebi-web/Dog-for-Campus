# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import bs4
import requests


def htmlOfKyomukaOfZengaku():
    urlToKyomukaOfZengaku = (
        "http://www2.he.tohoku.ac.jp/zengaku/zengaku_info_g.html"
    )
    responseFromKyomukaOfZengaku = requests.get(urlToKyomukaOfZengaku)
    soup = BeautifulSoup(responseFromKyomukaOfZengaku.content, "html.parser")
    return soup


def htmlOfAnnaiOfZengaku():
    urlToAnnaiOfZengaku = (
        "http://www2.he.tohoku.ac.jp/zengaku/zengaku_annai.html"
    )
    responseFromAnnaiOfZengaku = requests.get(urlToAnnaiOfZengaku)
    soup = BeautifulSoup(responseFromAnnaiOfZengaku.content, "html.parser")
    return soup


def main():
    return {
        "htmlOfKyomukaOfZengaku": htmlOfKyomukaOfZengaku(),
        "htmlOfAnnaiOfZengaku": htmlOfAnnaiOfZengaku(),
    }


if __name__ == "__main__":
    main()