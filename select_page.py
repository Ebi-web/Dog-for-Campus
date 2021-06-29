import streamlit as st

def page():

    sites = {
        "東北大学ホームページ ニュース（0）": 0,
        "東北大学ホームページ イベント（0）": 0,
        "東北大学全学教育サイト 教務課からのお知らせ（１）": 1,
        "東北大学全学教育サイト 授業案内（1）": 1,
        "理学部・理学研究科サイト 在学生向け情報（2）": 2,
        "数学科・数学専攻サイト セミナー（3）": 3,
        "数学科・数学専攻サイト 集中講義（3）": 3,
        "数学科・数学専攻サイト 談話会（3）": 3,
        "数学科・数学専攻サイト 研究集会（3）": 3,
        "物理学科・物理学専攻サイト お知らせ（4）": 4,
        "物理学科・物理学専攻サイト イベント（4）": 4,
        "物理学科・物理学専攻サイト イベント紹介（学部1・2年生）（4）": 4,
        "物理学科・物理学専攻サイト イベント紹介（学部3・4年生）（4）": 4,
        "物理学科・物理学専攻サイト イベント紹介（大学院生）（4）": 4,
        "物理学科・物理学専攻サイト 大学院受験生（大学院受験生）（4）": 4,
        "化学科・化学専攻サイト 重要なお知らせ（7）": 7,
        "化学科・化学専攻サイト 入試関連情報（7）": 7,
        "地球科学科・地学専攻サイト インフォメーション（6）": 6,
        "理学研究科・地球物理学専攻サイト お知らせ ニュース（5）": 5,
        "理学研究科・地球物理学専攻サイト お知らせ 専攻内情報（5）": 5,
        "理学研究科・地球物理学専攻サイト 大学院入試説明会（5）": 5,
        "理学研究科・地球物理学専攻サイト 大学院入試案内（5）": 5,
        "天文学教室サイト お知らせ（8）": 8,
        "生命科学研究科サイト 最新情報（9）": 9,
        "生命科学研究科サイト 入試情報（9）": 9,
    }

    title_continer = st.beta_container()
    containers = [st.beta_container() for i in range(4)]
    columns = list()
    for (i, container) in enumerate(containers):
        columns.append(container.beta_columns(3))
    is_scraping_dict = {}
    large_is_scraping_dict = {}
    title_continer.title("対象サイトの選択")
    former_group = -1
    for site, group in sites.items():
        with columns[group//3][group % 3]:
            if group != former_group:
                st.write("")
                st.write("")
                large_is_scraping_dict[group] = (st.checkbox(str(group) + ". " + site.split(" ")[0]))
                former_group = group
            is_scraping_dict[site]=st.checkbox("----" + site.split(" ")[1])
        
    for is_scraping_li in zip(large_is_scraping_dict, is_scraping_dict):
        pass