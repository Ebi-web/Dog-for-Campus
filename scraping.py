# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
from datetime import date, datetime


def getCurrentDate():
    return datetime.now().strftime("%Y%m%d")


def getCurrentYear():
    currentYear = datetime.now().year
    return currentYear


def htmlOfNewsOfHomePage():
    urlToNewsOfHomePage = (
        "https://www.tohoku.ac.jp/japanese/" + str(getCurrentYear()) + "/cate_news/"
    )
    responseFromNewsOfHomePage = requests.get(urlToNewsOfHomePage)
    soup = BeautifulSoup(responseFromNewsOfHomePage.content, "html.parser")
    wholeNewsDivTag = soup.find("div", {"class": "tab-content"})
    liTags=wholeNewsDivTag.find_all("li")
    for home_li in liTags:
        for comment in home_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return liTags


def liTagsOfEventsOfHomePageFromToday():
    urlToEventsOfHomePage = (
        "https://www.tohoku.ac.jp/japanese/" + str(getCurrentYear()) + "/cate_event/"
    )
    responseFromEventsOfHomePage = requests.get(urlToEventsOfHomePage)
    soup = BeautifulSoup(responseFromEventsOfHomePage.content, "html.parser")
    eventsInAYear = soup.find("div", {"class": "tab-content"}).find_all(
        "div", {"class": "tab-pane"}
    )
    eventsFromTodayLiTags = []
    currentMonthAndDay = int(getCurrentDate()[4:8])
    for eventsInAMonth in eventsInAYear:
        liTags = eventsInAMonth.find_all("li")
        for liTag in liTags:
            monthAndDay = liTag.find("div", {"class": "date"}).text
            monthAndDay = int(monthAndDay[0:2] + monthAndDay[3:5])
            if currentMonthAndDay <= monthAndDay:
                eventsFromTodayLiTags.append(liTag)
    for event_li in eventsFromTodayLiTags:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return eventsFromTodayLiTags


def htmlOfScienceFacultyForCurrentStudents():
    url = "https://www.sci.tohoku.ac.jp/student/post.html"
    responseFromThePage = requests.get(url)
    soup = BeautifulSoup(responseFromThePage.content, "html.parser")
    emergencies = soup.find("div", {"id": "emg_re"})
    updatedNotices = soup.find("div", {"class": "pagebody"}).find_all("li")
    returningHtmls = [emergencies] + updatedNotices
    for comment in emergencies(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    for updatedNotice in updatedNotices:
        for comment in updatedNotice(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return returningHtmls


def liTagsOfSeminarsOfMathFacultyFromToday():
    url = "http://www.math.tohoku.ac.jp/research/seminar.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    seminarLiTags = soup.find_all("li", {"id": True})
    liTagsSeminarsFromToday = []
    currentDate = int(getCurrentDate())
    for seminarLiTag in seminarLiTags:
        dateOfSeminar = int(seminarLiTag["id"][:8])
        if currentDate <= dateOfSeminar:
            liTagsSeminarsFromToday.append(seminarLiTag)
    for seminar_li in liTagsSeminarsFromToday:
        for comment in seminar_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return liTagsSeminarsFromToday


def liTagsOfIntensiveLectureOfMathFaclutyFromToday():
    url = "http://www.math.tohoku.ac.jp/research/intensive.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    intensiveLecturesLiTags = soup.find_all("li", {"id": True})
    liTagsIntensiveLecturesFromToday = []
    for intensiveLecturesLiTag in intensiveLecturesLiTags:
        try:
            dateOfIntensiveLecture = int(intensiveLecturesLiTag["id"][:8])
        except:
            dateOfIntensiveLecture = int(intensiveLecturesLiTag["id"][:6] + "01")
        if currentDate <= dateOfIntensiveLecture:
            liTagsIntensiveLecturesFromToday.append(intensiveLecturesLiTag)
    for event_li in liTagsIntensiveLecturesFromToday:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return liTagsIntensiveLecturesFromToday


def liTagsOfColloquiumOfMathFaclutyFromToday():
    url = "http://www.math.tohoku.ac.jp/research/colloquium.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    colloquiumLiTags = soup.find_all("li", {"id": True})
    liTagsColloquiumFromToday = []
    for colloquiumLiTag in colloquiumLiTags:
        dateOfColloquium = int(colloquiumLiTag["id"][:8])
        if currentDate <= dateOfColloquium:
            liTagsColloquiumFromToday.append(colloquiumLiTag)
    for colloquium_li in liTagsColloquiumFromToday:
        for comment in colloquium_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return liTagsColloquiumFromToday


def liTagsOfMeetingOfMathFaclutyFromToday():
    url = "http://www.math.tohoku.ac.jp/research/meeting.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    meetingLiTags = soup.find_all("li", {"id": True})
    liTagsMeetingFromToday = []
    for meetingLiTag in meetingLiTags:
        dateOfMeeting = int(meetingLiTag["id"][:8])
        if currentDate <= dateOfMeeting:
            liTagsMeetingFromToday.append(meetingLiTag)    
    return liTagsMeetingFromToday


def liTagsOfNoticeOfPhysicsFaclutyFromToday():
    url = "http://www.phys.tohoku.ac.jp/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    noticeLiTags = soup.find_all("li", {"class": "info_jp clearfix"})
    for notice_li in noticeLiTags:
        for comment in notice_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return noticeLiTags


def liTagsOfEventsOfPhysicsFaclutyFromToday():
    url = "http://www.phys.tohoku.ac.jp/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    eventLiTags = soup.find_all("li", {"class": "event_jp clearfix"})
    for event_li in eventLiTags:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForFirstSecond():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-3"}).find_all("li")
    for event_li in eventLiTags:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForThirdFourth():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-4"}).find_all("li")
    for event_li in eventLiTags:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForGraduates():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-5"}).find_all("li")
    for event_li in eventLiTags:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-2"}).find_all("li")
    for event_li in eventLiTags:
        for comment in event_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return eventLiTags


def liTagsOfImportantsOfChemistryFacluty():
    url = "http://www.chem.tohoku.ac.jp/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    importantsLiTags = soup.find("div", {"class": "info_inner"}).find_all("li")
    for important_li in importantsLiTags:
        for comment in important_li(text=lambda text: isinstance(text, Comment)):   # important
            comment.extract()
    return importantsLiTags


def liTagsOfAdmissionsOfChemistryFacluty():
    url = "http://www.chem.tohoku.ac.jp/entrance/admissions/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    admissionLiTags = soup.find("div", {"class": "admissions"}).find_all("li")
    for admission_li in admissionLiTags:
        for comment in admission_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return admissionLiTags


def ddTagsOfExternalInformationOfGeoscienceFacluty():
    url = "http://www.es.tohoku.ac.jp/JP/information/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    informationLiTags = soup.find("div", {"id": "sectionInformation"}).find_all("dd")
    for info_li in informationLiTags:
        for comment in info_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return informationLiTags


def liTagsOfNewsOfEarthPhysicsMajor():
    url = "http://www.gp.tohoku.ac.jp/information/news.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    newsLiTags = soup.find("section", {"class": "info-list"}).find_all("li")
    returningNewsLiTags = []
    for newsLiTag in newsLiTags:
        newsLiTag.find("script").extract()
        returningNewsLiTags.append(newsLiTag)
    for return_news_li in returningNewsLiTags:
        for comment in return_news_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return returningNewsLiTags


def liTagsOfInternalInfoOfEarthPhysicsMajor():
    url = "http://www.gp.tohoku.ac.jp/information/internal.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    internalInfoLiTags = soup.find("section", {"class": "info-list"}).find_all("li")
    returningInfoLiTags = []
    for internalInfoLiTag in internalInfoLiTags:
        internalInfoLiTag.find("script").extract()
        returningInfoLiTags.append(internalInfoLiTag)
    for return_info_li in returningInfoLiTags:
        for comment in return_info_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return returningInfoLiTags


def articleTagsOfEntranceBriefingOfEarthPhysicsMajor():
    url = "http://www.gp.tohoku.ac.jp/entrance-exams/entrance-exams-briefing.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    briefingArticleTags = soup.find_all("article")
    for briefingArticleTag in briefingArticleTags:
        for comment in briefingArticleTag(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return briefingArticleTags


def articleTagsOfExamInfoOfEarthPhysicsMajor():
    url = "http://www.gp.tohoku.ac.jp/entrance-exams/entrance-exams-top.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    examInfoArticleTags = soup.find_all("article")
    for examInfoArticleTag in examInfoArticleTags:
        for comment in examInfoArticleTag(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return examInfoArticleTags


def divTagsOfInfoOfAstronomicalMajor():
    url = "https://www.astr.tohoku.ac.jp/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    infoDivTags = soup.find_all("div", {"class": "newsbx"})
    for infoDivTag in infoDivTags:
        for comment in infoDivTag(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return infoDivTags

def entryTagsOfExamInfoOfLifeScienceMajor():
    url = "https://www.lifesci.tohoku.ac.jp/admission/rss.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    entryTagsExamInfo = soup.find_all("entry")
    for entry_exam_tag in entryTagsExamInfo:
        for comment in entry_exam_tag(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return entryTagsExamInfo


def entryTagsOfInternalInfoOfLifeScienceMajor():
    url = "https://www.lifesci.tohoku.ac.jp/oncampus/rss.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    entryTagsInternalInfo = soup.find_all("entry")
    for entry_internal_tag in entryTagsInternalInfo:
        for comment in entry_internal_tag(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return entryTagsInternalInfo


def zengaku_kyomuka_li_tags():
    zengaku_kyomuka_url = "http://www2.he.tohoku.ac.jp/zengaku/zengaku_info_g.html"
    zengaku_kyomuka_res = requests.get(zengaku_kyomuka_url)
    soup = BeautifulSoup(zengaku_kyomuka_res.content, "html.parser")
    zengaku_kyomuka_content = soup.select_one("#content_box")
    zengaku_kyomuka_li = zengaku_kyomuka_content.select("li")
    for zenkyo_each_li in zengaku_kyomuka_li:
        for comment in zenkyo_each_li(text=lambda text: isinstance(text, Comment)):
            comment.extract()
    return zengaku_kyomuka_li


def zengaku_guide_html():
    zengaku_guide_url = "http://www2.he.tohoku.ac.jp/zengaku/zengaku_annai.html"
    zengaku_guide_res = requests.get(zengaku_guide_url)
    soup = BeautifulSoup(zengaku_guide_res.content, "html.parser")
    zengaku_guide_content = soup.select_one("#content_box")
    zengaku_guide_index = zengaku_guide_content.select_one("#page-index3")
    for comment in zengaku_guide_index(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    return zengaku_guide_index


def main():
    return {
        "liTagsOfEventsOfHomePageFromToday": liTagsOfEventsOfHomePageFromToday,
        "htmlOfNewsOfHomePage": htmlOfNewsOfHomePage,
        "htmlOfScienceFacultyForCurrentStudents": htmlOfScienceFacultyForCurrentStudents,
        "liTagsOfSeminarsOfMathFacultyFromToday": liTagsOfSeminarsOfMathFacultyFromToday,
        "liTagsOfIntensiveLectureOfMathFaclutyFromToday": liTagsOfIntensiveLectureOfMathFaclutyFromToday,
        "liTagsOfColloquiumOfMathFaclutyFromToday": liTagsOfColloquiumOfMathFaclutyFromToday,
        "liTagsOfMeetingOfMathFaclutyFromToday": liTagsOfMeetingOfMathFaclutyFromToday,
        "liTagsOfNoticeOfPhysicsFaclutyFromToday": liTagsOfNoticeOfPhysicsFaclutyFromToday,
        "liTagsOfEventsOfPhysicsFaclutyFromToday": liTagsOfEventsOfPhysicsFaclutyFromToday,
        "liTagsOfEventsOfPhysicsFaclutyForFirstSecond": liTagsOfEventsOfPhysicsFaclutyForFirstSecond,
        "liTagsOfEventsOfPhysicsFaclutyForThirdFourth": liTagsOfEventsOfPhysicsFaclutyForThirdFourth,
        "liTagsOfEventsOfPhysicsFaclutyForGraduates": liTagsOfEventsOfPhysicsFaclutyForGraduates,
        "liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates": liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates,
        "liTagsOfImportantsOfChemistryFacluty": liTagsOfImportantsOfChemistryFacluty,
        "liTagsOfAdmissionsOfChemistryFacluty": liTagsOfAdmissionsOfChemistryFacluty,
        "ddTagsOfExternalInformationOfGeoscienceFacluty": ddTagsOfExternalInformationOfGeoscienceFacluty,
        "liTagsOfNewsOfEarthPhysicsMajor": liTagsOfNewsOfEarthPhysicsMajor,
        "liTagsOfInternalInfoOfEarthPhysicsMajor": liTagsOfInternalInfoOfEarthPhysicsMajor,
        "articleTagsOfEntranceBriefingOfEarthPhysicsMajor": articleTagsOfEntranceBriefingOfEarthPhysicsMajor,
        "articleTagsOfExamInfoOfEarthPhysicsMajor": articleTagsOfExamInfoOfEarthPhysicsMajor,
        "divTagsOfInfoOfAstronomicalMajor": divTagsOfInfoOfAstronomicalMajor,
        "entryTagsOfExamInfoOfLifeScienceMajor": entryTagsOfExamInfoOfLifeScienceMajor,
        "entryTagsOfInternalInfoOfLifeScienceMajor": entryTagsOfInternalInfoOfLifeScienceMajor,
        "zengaku_kyomuka_li_tags": zengaku_kyomuka_li_tags,
        "zengaku_guide_html": zengaku_guide_html,
    }


if __name__ == "__main__":
    main()
