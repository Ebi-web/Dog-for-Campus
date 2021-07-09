import streamlit as st


def page():

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

    title_container = st.beta_container()
    title_container.title("データ取得対象サイトの選択")
    title_container = None

    content_container = st.beta_container()

    with content_container:
        COLUMNS_NUM = 4
        content_columns =st.beta_columns(COLUMNS_NUM)
        current_index = 0
        ROWS_NUM=3
        for site_group_name, site_name_list in site_groups.items():
            with content_columns[current_index//ROWS_NUM]:
                st.markdown("**"+site_group_name+"**")
                current_index += 1
                for site_name in site_name_list:
                    st.checkbox(site_name)
                    st.write("")
        current_index=None

