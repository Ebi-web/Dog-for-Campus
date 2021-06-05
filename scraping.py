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
    return wholeNewsDivTag


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
    return eventsFromTodayLiTags


def htmlOfScienceFacultyForCurrentStudents():
    url = "https://www.sci.tohoku.ac.jp/student/post.html"
    responseFromThePage = requests.get(url)
    soup = BeautifulSoup(responseFromThePage.content, "html.parser")
    emergencies = soup.find("div", {"id": "emg_re"})
    updatedNotices = soup.find("div", {"class": "pagebody"})
    returningHtmls = {"emergencies": emergencies, "updateNoticies": updatedNotices}
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
    return liTagsSeminarsFromToday


def liTagsOfIntensiveLectureOfMathFaclutyFromToday():
    url = "http://www.math.tohoku.ac.jp/research/intensive.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    intensiveLecturesLiTags = soup.find_all("li", {"id": True})
    liTagsIntensiveLecturesFromToday = []
    for intensiveLecturesLiTag in intensiveLecturesLiTags:
        dateOfIntensiveLecture = int(intensiveLecturesLiTag["id"][:8])
        if currentDate <= dateOfIntensiveLecture:
            liTagsIntensiveLecturesFromToday.append(intensiveLecturesLiTag)
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
    return noticeLiTags


def liTagsOfEventsOfPhysicsFaclutyFromToday():
    url = "http://www.phys.tohoku.ac.jp/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    eventLiTags = soup.find_all("li", {"class": "event_jp clearfix"})
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForFirstSecond():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-3"}).find_all("li")
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForThirdFourth():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-4"}).find_all("li")
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForGraduates():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-5"}).find_all("li")
    return eventLiTags


def liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates():
    url = "http://www.phys.tohoku.ac.jp/event-information/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    eventLiTags = soup.find("div", {"id": "evtabs-2"}).find_all("li")
    return eventLiTags


def liTagsOfImportantsOfChemistryFacluty():
    url = "http://www.chem.tohoku.ac.jp/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    importantsLiTags = soup.find("div", {"class": "info_inner"}).find_all("li")
    return importantsLiTags


def liTagsOfAdmissionsOfChemistryFacluty():
    url = "http://www.chem.tohoku.ac.jp/entrance/admissions/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currentDate = int(getCurrentDate())
    admissionLiTags = soup.find("div", {"class": "admissions"}).find_all("li")
    return admissionLiTags


def ddTagsOfExternalInformationOfGeoscienceFacluty():
    url = "http://www.es.tohoku.ac.jp/JP/information/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    informationLiTags = soup.find("div", {"id": "sectionInformation"}).find_all("dd")
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
    return entryTagsExamInfo


def entryTagsOfInternalInfoOfLifeScienceMajor():
    url = "https://www.lifesci.tohoku.ac.jp/oncampus/rss.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    entryTagsInternalInfo = soup.find_all("entry")
    return entryTagsInternalInfo


def main():
    return {
        "liTagsOfEventsOfHomePageFromToday": liTagsOfEventsOfHomePageFromToday(),
        "htmlOfNewsOfHomePage": htmlOfNewsOfHomePage(),
        "htmlOfScienceFacultyForCurrentStudents": htmlOfScienceFacultyForCurrentStudents(),
        "liTagsOfSeminarsOfMathFacultyFromToday": liTagsOfSeminarsOfMathFacultyFromToday(),
        "liTagsOfIntensiveLectureOfMathFaclutyFromToday": liTagsOfIntensiveLectureOfMathFaclutyFromToday(),
        "liTagsOfColloquiumOfMathFaclutyFromToday": liTagsOfColloquiumOfMathFaclutyFromToday(),
        "liTagsOfMeetingOfMathFaclutyFromToday": liTagsOfMeetingOfMathFaclutyFromToday(),
        "liTagsOfNoticeOfPhysicsFaclutyFromToday": liTagsOfNoticeOfPhysicsFaclutyFromToday(),
        "liTagsOfEventsOfPhysicsFaclutyFromToday": liTagsOfEventsOfPhysicsFaclutyFromToday(),
        "liTagsOfEventsOfPhysicsFaclutyForFirstSecond": liTagsOfEventsOfPhysicsFaclutyForFirstSecond(),
        "liTagsOfEventsOfPhysicsFaclutyForThirdFourth": liTagsOfEventsOfPhysicsFaclutyForThirdFourth(),
        "liTagsOfEventsOfPhysicsFaclutyForGraduates": liTagsOfEventsOfPhysicsFaclutyForGraduates(),
        "liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates": liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates(),
        "liTagsOfImportantsOfChemistryFacluty": liTagsOfImportantsOfChemistryFacluty(),
        "liTagsOfAdmissionsOfChemistryFacluty": liTagsOfAdmissionsOfChemistryFacluty(),
        "ddTagsOfExternalInformationOfGeoscienceFacluty": ddTagsOfExternalInformationOfGeoscienceFacluty(),
        "liTagsOfNewsOfEarthPhysicsMajor": liTagsOfNewsOfEarthPhysicsMajor(),
        "liTagsOfInternalInfoOfEarthPhysicsMajor": liTagsOfInternalInfoOfEarthPhysicsMajor(),
        "articleTagsOfEntranceBriefingOfEarthPhysicsMajor": articleTagsOfEntranceBriefingOfEarthPhysicsMajor(),
        "articleTagsOfExamInfoOfEarthPhysicsMajor": articleTagsOfExamInfoOfEarthPhysicsMajor(),
        "divTagsOfInfoOfAstronomicalMajor": divTagsOfInfoOfAstronomicalMajor(),
        "entryTagsOfExamInfoOfLifeScienceMajor": entryTagsOfExamInfoOfLifeScienceMajor(),
        "entryTagsOfInternalInfoOfLifeScienceMajor": entryTagsOfInternalInfoOfLifeScienceMajor(),
    }


if __name__ == "__main__":
    main()