# Dog-for-Campus
大学からのお知らせを見落としてた！大学関連のホームページがいくつもあって見に行くの面倒！
Dog for Campusに任せて時間とストレスを節約しましょう。監視するサイトを登録しておくだけで，更新された情報を
まとめておいてくれます。

対応予定の大学：東北大学(理学部)

# 環境構築

本プロジェクトのルートディレクトリで以下を実行
```Shell
docker-compose up --build -d
```

何かコマンドを実行する時:
```Shell
docker-compose exec web bash
```

# NOTE
使用技術(予定含む)：
フロントエンド
・Svelte
・Svelte Materialify
・HTML5,CSS3,JS

バックエンド
・PHP8
・MySQL

インフラ
・Firebase(認証周り)
・apache
・AWS Route53
・AWS ACM

使用ライブラリ(予定含む):
Guzzle : HTTP クライアント
PHP DOM Wrapper : DOM 操作
Chrome PHP : ヘッドレス Chrome 操作
WorkerPool : 並列処理
