import streamlit as st
import scraping as sc
import select_page as sp

corr_dict = {
    "イベント(東北大学ホームページ)": "liTagsOfEventsOfHomePageFromToday",
    "ニュース":"htmlOfNewsOfHomePage",
    "在学生向け情報" :"htmlOfScienceFacultyForCurrentStudents",
    "セミナー": "liTagsOfSeminarsOfMathFacultyFromToday",
    "集中講義": "liTagsOfIntensiveLectureOfMathFaclutyFromToday",
    "談話会": "liTagsOfColloquiumOfMathFaclutyFromToday",
    "研究集会": "liTagsOfMeetingOfMathFaclutyFromToday",
    "お知らせ(物理学科・物理学専攻)": "liTagsOfNoticeOfPhysicsFaclutyFromToday",
    "イベント(物理学科・物理学専攻)": "liTagsOfEventsOfPhysicsFaclutyFromToday",
    "イベント紹介(学部1&2年生)": "liTagsOfEventsOfPhysicsFaclutyForFirstSecond",
    "イベント紹介(学部3&4年生)": "liTagsOfEventsOfPhysicsFaclutyForThirdFourth",
    "イベント紹介(大学院生)": "liTagsOfEventsOfPhysicsFaclutyForGraduates",
    "イベント紹介(大学院受験生)": "liTagsOfEventsOfPhysicsFaclutyForGraduateCandidates",
    "重要なお知らせ": "liTagsOfImportantsOfChemistryFacluty",
    "入試関連情報": "liTagsOfAdmissionsOfChemistryFacluty",
    "インフォメーション": "ddTagsOfExternalInformationOfGeoscienceFacluty",
    "お知らせ(ニュース)": "liTagsOfNewsOfEarthPhysicsMajor",
    "お知らせ(専攻内情報)": "liTagsOfInternalInfoOfEarthPhysicsMajor",
    "大学院入試説明会": "articleTagsOfEntranceBriefingOfEarthPhysicsMajor",
    "大学院入試案内": "articleTagsOfExamInfoOfEarthPhysicsMajor",
    "お知らせ(天文学教室)": "divTagsOfInfoOfAstronomicalMajor",
    "入試情報": "entryTagsOfExamInfoOfLifeScienceMajor",
    "最新情報": "entryTagsOfInternalInfoOfLifeScienceMajor",
    "教務課からのお知らせ": "zengaku_kyomuka_li_tags",
    "授業案内": "zengaku_guide_html",
}

def page():
    result_dict = {}

    st.title("対象サイトの情報更新")
    is_updated = st.button('更新を実行')
    if is_updated:
        for (key, bool) in st.session_state["sites"].items():
            if bool:
                result_dict[key] = sc.main()[corr_dict[key]]
        if result_dict == {}:
            st.warning('！対象サイトが選択されていません')
        else:
            st.write("更新を実行しました")
    return result_dict