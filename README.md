<img src='https://www.tohoku.ac.jp/japanese/share/img/logo_header.png'>

# CAMPUS-DOG
情強大学生を支える情報ツール、Campus-Dogを体験してみよう。
大学からのお知らせを見落としてた！大学関連のホームページがいくつもあって見に行くの面倒だし時間もかかる！
お知らせの収集はCAMPUS-DOGに任せて時間とストレスを節約しましょう。監視する大学関連サイトを選ぶだけで，更新された情報を
まとめて通知してくれます。

対応予定の大学・学部：東北大学(理学部)

# 機能一覧

- 監視対象HP選択機能
- スクレイピング定期実行機能
- 更新検知時の通知機能
- スクレイピング手動実行機能

# 使用技術

## フロントエンド・バックエンド
- Vue.js 3 (SPA化する予定)
- Typescript (予定)
- Python3.8.8
- Django

## インフラ
- AWS Amplify
- AWS API Gateway
- AWS IAM
- AWS Lambda
- AWS ACM
- AWS Route53

## CI/CD
- AWS CodeDeploy(予定)
- AWS CodePipeline(予定)
- AWS CodeCommit(予定)
- AWS CodeBuild(予定)

## データベース
- AWS DynamoDB

## モジュール
- BeautifulSoupなど

## Linter
- black

# NOTE/免責事項

<p>Campus-Dogは常に完全なHP情報を収集することを保証するものではありません。また、これにより生じたいかなる不利益についても開発者は責任を負いません。</p>
<p>Campus-Dogは「80%の大学生が求める情報を」「いつでも」「見やすく」提供することを追求します。そのため、収集する情報は「イベント」「お知らせ」といった大学コミュニティ内のジェネラルなものです。ごく一部の学生のみが興味を持つ情報(化学専攻の卓越研究員事業など)はCampus-Dogでは情報収集機能実装の優先度が低いか、収集されません。</p>
<p>Campus-DogはMITライセンスを採用します。</p>
<p>東北大学およびその関連団体と主たる開発者(Ebi-web)の間にはいかなる金銭的取り決めも存在しません。また、Ebi-webは東北大学当局との間にいかなる関係もありません。</p>

