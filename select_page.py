import streamlit as st
import scraping as sc
from dynamoDB import UserTable

def select():
    site_groups = {
        "東北大学ホームページ": ["ニュース", "イベント(東北大学ホームページ)"],
        "東北大学全学教育サイト": ["教務課からのお知らせ", "授業案内"],
        "理学部・理学研究科サイト": ["在学生向け情報"],
        "数学科・数学専攻サイト": ["セミナー", "集中講義", "談話会", "研究集会"],
        "物理学科・物理学専攻サイト": [
            "お知らせ(物理学科・物理学専攻)",
            "イベント(物理学科・物理学専攻)",
            "イベント紹介(学部1&2年生)",
            "イベント紹介(学部3&4年生)",
            "イベント紹介(大学院生)",
            "イベント紹介(大学院受験生)",
        ],
        "理学研究科・地球物理学専攻サイト": ["お知らせ(ニュース)", "お知らせ(専攻内情報)", "大学院入試説明会", "大学院入試案内"],
        "地球科学科・地学専攻サイト": ["インフォメーション"],
        "化学科・化学専攻サイト": ["重要なお知らせ", "入試関連情報"],
        "天文学教室サイト": ["お知らせ(天文学教室)"],
        "生命科学研究科サイト": ["最新情報", "入試情報"],
    }

    sites = 0
    for site_group in site_groups.values():
        sites += len(site_group)

    content_container = st.beta_container()
    with content_container:
        COLUMNS_NUM = 4
        content_columns = st.beta_columns(COLUMNS_NUM)
        current_index = 0
        ROWS_NUM = 3
        if st.session_state["is_signed_in"]:
            user_table = UserTable()
            site_index = 0
            new_binarry_num = 0
            try:
                registerd_binarry_num = user_table.get()["RegisteredBinaryNum"]
            except:
                registerd_binarry_num = 0
            for site_group_name, site_name_list in site_groups.items():
                with content_columns[current_index // ROWS_NUM]:
                    st.markdown("**" + site_group_name + "**")
                    current_index += 1
                    for site_name in site_name_list:
                        if str(registerd_binarry_num)[site_index:site_index+1] == "1":
                            registered_value = True
                        else:
                            registered_value = False
                        st.write("")
                        st.session_state["sites"][site_name] = st.checkbox(value=registered_value, label=site_name)
                        if st.session_state["sites"][site_name]:
                            new_binarry_num += 10**(site_index)
                        site_index += 1
            return new_binarry_num, sites

        else:
            st.session_state["sites"] = {}
            st.session_state["scraping_result_dict"] = {}
            for site_group_name, site_name_list in site_groups.items():
                with content_columns[current_index // ROWS_NUM]:
                    st.markdown("**" + site_group_name + "**")
                    current_index += 1
                    for site_name in site_name_list:
                        st.write("")
                        st.session_state["sites"][site_name] = st.checkbox(label=site_name)
        current_index = None

def page():
    target_to_function = {
        "イベント(東北大学ホームページ)": "liTagsOfEventsOfHomePageFromToday",
        "ニュース": "htmlOfNewsOfHomePage",
        "在学生向け情報": "htmlOfScienceFacultyForCurrentStudents",
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

    title_container = st.beta_container()
    title_container.title("対象サイトの選択/サイト内容の取得")
    is_button_pushed = st.button("サイト内容の取得を実行")

    flash_info_container = st.beta_container()

    select()

    if is_button_pushed:
        for (site_name, is_enabled) in st.session_state["sites"].items():
            if is_enabled:
                st.session_state["scraping_result_dict"][site_name] = sc.main()[
                    target_to_function[site_name]
                ]()
        with flash_info_container:
            if st.session_state["scraping_result_dict"] == {}:
                st.warning("対象サイトを選択してください")
            else:
                st.info("左側のメニューから取得結果一覧を押してください")
