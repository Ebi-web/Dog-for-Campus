import streamlit as st


def page():
    st.markdown("""
    # 使い方ガイド
    このアプリを訪れて頂きありがとうございます！
    ここでは本アプリ **「Campus Dog」**の使い方を簡単にご説明します。

    1. 画面左のメニューから「対象サイトの選択/サイト内容の取得」を選択

    - ここでは自分の関心のある大学Webページの項目を選択してください
    - ここで指定された項目をCampus Dogは収集します

    2. 「サイト内容の取得を実行」を押す

    - Webページの項目の選択が終わったら左上の「サイト内容の取得を実行」を押してください
    - Campus Dogがあなたに代わって指定された大学Webページの内容を収集してまとめます
    - 選択された項目の数により収集には時間がかかることがあります

    3. 結果を確認する

    - 画面左のメニューから「取得結果一覧」を選択して結果をご確認ください
    - 項目に何も表示されない場合は、お知らせが取得先のページになかったことを表します
    
    4. 「対象サイトの登録」から購読したいサイトを選択・登録しておけば、大学Webサイトの更新を登録されたメールアドレスにお知らせします。
    なお、対象サイトが登録された時点でユーザーがその対象サイトに関するメールの受信に同意したものとみなします。登録されたメールアドレスは、登録されたサイトの更新をユーザーに通知する以外の目的では使用されません。
    また、登録された対象サイトであってもユーザーは後からその登録を解除できます。Campus Dogは対象サイトの登録解除をもって、ユーザーがその対象サイトに関するメールの受信の同意を取り消したものとみなします。
    ※この機能は「新規登録」からユーザー登録をして頂いた方のみご利用頂けます。


    # アプリの概要

    ここでは簡単にアプリの概要を示します。

    |key|value|
    |:-------|-------:|
    |名前|Campus Dog|
    |できること|東北大学のWebページの情報を取得してまとめること|
    |嬉しいこと1|複数の大学Webページを自分で見回らなくていい|
    |嬉しいこと2|大学からの大切なお知らせを見落とさない|
    |嬉しいこと3|自分の関心のある大学Webページに絞って内容をまとめてくれる|
    |嬉しいこと4|完全無料である|
    |現在のバージョン|2.0.0|
    |公開日|2021年9月23日|

    # ユーザの皆様へ

    今後も下記のような継続的な機能追加やバージョンアップを予定しております。

    1.　大学ページの取得結果の表示件数を調整できる機能

    この他にもご意見やご要望は下記のTwitterアカウントまでDMを頂けると嬉しいです。
    今後の開発に役立てさせて頂きます。

    メイン開発者のTwitter: @eng_toshiaki

    # 一般の開発者の方へ

    Campus Dogでは一般の開発者の方のコントリビューションも歓迎しております。

    Githubリポジトリのリンク:https://github.com/Ebi-web/Dog-for-Campus

    また、Campus DogはMITライセンスを採用しております。

    # 免責事項

    1. Campus Dogが取得する情報は全て東北大学Webページの内容に基づいてはおりますが、取得結果の完全性を保証するものではありません。

    2. Campus Dogの使用に際して生じたいかなる損害についても開発チームは責任を負いません。

    3. また、Campus-Dogは「80%の大学生が求める情報を」「いつでも」「見やすく」提供することを追求します。そのため、収集する情報は「イベント」「お知らせ」といった大学コミュニティ内のジェネラルなものです。ごく一部の学生のみが興味を持つ情報(化学専攻の卓越研究員事業など)はCampus-Dogでは情報収集機能実装の優先度が低いです。""")
