# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import bs4
import requests
import time
import math


def getCurrentYear():
    START_OF_TIME_MODULE = 1970
    SECONDS_PER_A_YEAR = 31536000
    currentYear = str(
        math.floor(START_OF_TIME_MODULE + (time.time() / SECONDS_PER_A_YEAR))
    )
    return currentYear


def htmlOfNewsOfHomePage():
    urlToNewsOfHomePage = (
        "https://www.tohoku.ac.jp/japanese/" + getCurrentYear() + "/cate_news/"
    )
    responseFromNewsOfHomePage = requests.get(urlToNewsOfHomePage)
    soup = BeautifulSoup(responseFromNewsOfHomePage.content, "html.parser")
    return soup


def htmlOfEventsOfHomePage():
    urlToEventsOfHomePage = (
        "https://www.tohoku.ac.jp/japanese/" + getCurrentYear() + "/cate_event/"
    )
    responseFromEventsOfHomePage = requests.get(urlToEventsOfHomePage)
    soup = BeautifulSoup(responseFromEventsOfHomePage.content, "html.parser")
    return soup


def main():
    return {
        "htmlOfEventsOfHomePage": htmlOfEventsOfHomePage(),
        "htmlOfNewsOfHomePage": htmlOfNewsOfHomePage(),
    }


if __name__ == "__main__":
    main()
