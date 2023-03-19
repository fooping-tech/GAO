# GAO Discord Bot

GAO は、Discord 上で DAO らしからぬ中央集権を匂わせる挙動を検出すると発言者に対して注意を促すためのカスタムボットです。GAO は、Python で書かれ、discord.py ライブラリを使用しています。

![icon](https://user-images.githubusercontent.com/4471301/226089972-23b5bda1-93e3-4391-b2ae-fba13de04ece.png)

## 動作環境

GAO を動作させるのに必要なライブラリ

- Python 3.6 以上
- discord.py 2.2.2
- pyserial 3.5

## インストール方法

このリポジトリをクローンまたはダウンロードしてください。
必要に応じて、仮想環境を作成してアクティブにします。
必要なパッケージをインストールします。

```
pip install discord.py
pip install pyserial
pip install python-dotenv
```

/img フォルダを作成し、
ボットのリプライで使用したい画像をフォルダ内に追加してください。

Discord の開発者ポータルで新しいアプリケーションを作成し、ボットを作成して、トークンを取得します。
https://discordpy.readthedocs.io/ja/latest/discord.html

.env ファイルを作成し、以下のように DISCORD_TOKEN,SERVER_ID,ROBOT_ID を設定してください。

```.env
DISCORD_TOKEN=[your access token]
SERVER_ID=[your server id]
ROBOT_ID=[your robot id (ex. '/dev/cu.usbserial-xxxxxxxxx')
```

## 起動方法

python bot.py を実行して、GAO ボットを起動します。
起動中はお使いの Discord サーバーでボットが動きます。

## GAO ボットの機能

1. DAO コミュニティの文化・価値判断軸の啓蒙

   - 文化啓蒙：
     DAO らしからぬ中央集権を匂わせる言動を検出すると発言者に対して注意を促すことができます。はじめは優しく DAO について教えてくれる GAO くんも仏の顔は三度まで！？ GAO くん robot が豹変するかも。貢献度が高いと GAO 君が褒めてくれるかも???
   - 判断軸：
     多様な文化や価値観を持つメンバーとのやり取りの中で実行の判断軸がぶれる場合は、会社の mission, vision, value（toyotaway など）を
     　ポップアップ表示により判断軸を啓蒙することができます。

1. セキュリティ対策

   - ハッカーが貼った不正なサイトリンクなどから、セキュリティ面でのリスクをポップアップし、リスクをリスクとして認識させることができます。
     　明らかに怪しいサイト URL は、GAO くんが激しい炎で一瞬で焼き尽くしてくれます。

1. 開発中
   - openAI API を用いて、DAO 内での出来事を 1 日、１週間等、定期的に自動でレポートを作成することができます。

### GAO がサポートするコマンドの一覧

- トヨタウェイ : T 社の Value 画像を表示します。
- ミッション : T 社の Mission 画像を表示します。
- ヴィジョン : T 社の Vision 画像を表示します。
- toyotaway : T 社の Value 画像(English)を表示します。
- mission : T 社の Mission 画像(English)を表示します。
- vision : T 社の Vision 画像(English)を表示します。

## 関連機能

GAO ロボットは以下のリポジトリを参照してください。

https://github.com/fukusuke007/GAO_ROBOT

## ライセンス

このプロジェクトは、MIT ライセンスの下で公開されています。詳細については、LICENSE ファイルを参照してください。
