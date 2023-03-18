# GAO Discord Bot

GAOは、Discord上でDAOらしからぬ中央集権を匂わせる挙動を検出すると発言者に対して注意を促すためのカスタムボットです。GAOは、Pythonで書かれ、discord.pyライブラリを使用しています。

![icon](https://user-images.githubusercontent.com/4471301/226089972-23b5bda1-93e3-4391-b2ae-fba13de04ece.png)

## 動作環境

GAOを動作させるのに必要なライブラリ

* Python 3.6以上
* discord.py                        2.2.2
* pyserial                          3.5


## インストール方法

このリポジトリをクローンまたはダウンロードしてください。
必要に応じて、仮想環境を作成してアクティブにします。
必要なパッケージをインストールします。
```
pip install discord.py
pip install python-dotenv
```

ボットのリプライで使用したい画像を追加してください。

Discordの開発者ポータルで新しいアプリケーションを作成し、ボットを作成して、トークンを取得します。
https://discordpy.readthedocs.io/ja/latest/discord.html

.env ファイルを作成し、以下のようにDISCORD_TOKEN,SERVER_ID,ROBOT_IDを設定してください。

```.env
DISCORD_TOKEN=[your access token]
SERVER_ID=[your server id]
ROBOT_ID=[your robot id (ex. '/dev/cu.usbserial-xxxxxxxxx')
```
python bot.py を実行して、GAOボットを起動します。

GAOロボットは以下のリポジトリを参照してください。
https://github.com/fukusuke007/GAO_ROBOT

## 使い方
DAOっぽくないキーワードを検出すると、botがDAOっぽくないことを申し入れるコメントを投稿します。
以下は、GAOがサポートするコマンドの一覧です。

* トヨタウェイ : T社のValue画像を表示します。
* ミッション : T社のMission画像を表示します。
* ヴィジョン : T社のVision画像を表示します。
* toyotaway : T社のValue画像(English)を表示します。
* mission : T社のMission画像(English)を表示します。
* vision : T社のVision画像(English)を表示します。

## ライセンス

このプロジェクトは、MITライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。
