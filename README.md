# Campus Dog
東北大学理学部生向けの情報ツール、Campus Dogを体験してみよう。
大学からのお知らせを見落としてた！大学関連のホームページがいくつもあって見に行くの面倒だし時間もかかる！
お知らせの収集はCampus Dogに任せて時間とストレスを節約しましょう。監視する大学関連サイトを登録しておけば，更新を
まとめて通知してくれます。

**Campus Dogは下記のバッジから使うことができます。 You can use the Campus Dog through the badge below. Click and try it!**
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/ebi-web/dog-for-campus/main/main.py)

対応している大学・学部：東北大学(理学部)

# 機能一覧

- 監視対象HP選択機能
- スクレイピング定期実行機能
- 更新検知時の通知機能
- スクレイピング手動実行機能

# 技術的なこだわり

- 従来ではスクレイピングのリクエストが来たら都度スクレイピングしていたため対象ページが多いと10秒以上レスポンスにかかっていた
- しかしAWS Lambdaで定期的にスクレイピングを行って結果を定期的にDynamoDBに溜めてスクレイピングのリクエストには溜めた結果を返すように設計し直したことでレスポンスタイムを常時1~2秒程度まで低減させた
- 今後はAWS Lambdaを中心としたサーバーレスアーキテクチャに挑戦する方針

# 使用技術

## フロントエンド・バックエンド
- Python3.8.8
- Streamlit 0.88.0
- Vue.js 3.x(予定)
- Nuxt.js(予定)
- Typescript (予定)

## インフラ
- Streamlit Sharing
- AWS IAM
- AWS Lambda
- AWS SNS
- AWS EventBridge
- AWS CloudWatch
- AWS Amplify(予定)
- AWS API Gateway(予定)
- AWS ACM(予定)
- AWS Route53(予定)

## CI/CD
- AWS CodeDeploy(予定)
- AWS CodePipeline(予定)
- AWS CodeCommit(予定)
- AWS CodeBuild(予定)

## データベース
- AWS DynamoDB

## モジュール
- BeautifulSoupなど

## その他
- Firebase Authentication

# NOTE/免責事項

<p>Campus-Dogは常に完全なHP情報を収集することを保証するものではありません。また、これにより生じたいかなる不利益についても開発者は責任を負いません。</p>
<p>Campus-Dogは「80%の大学生が求める情報を」「いつでも」「見やすく」提供することを追求します。そのため、収集する情報は「イベント」「お知らせ」といった大学コミュニティ内のジェネラルなものです。ごく一部の学生のみが興味を持つ情報(化学専攻の卓越研究員事業など)はCampus-Dogでは情報収集機能実装の優先度が低いか、収集されません。</p>
<p>Campus-DogはMITライセンスを採用します。</p>
<p>東北大学およびその関連団体とCampus Dog開発チームの間にはいかなる法的取り決めも存在しません。</p>

<div style="height:100px;width=100px">
<img src='https://dl.easyuploader.cloud/20210923154209_6d70706b.png'>
</div>
※Campus Dog開発チームには東北大学関係者が所属しています
