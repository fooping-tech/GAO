# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ROBOT_ID = os.getenv('ROBOT_ID')