import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5935022610:AAEcec2VplFyjPUZeH_hncHHMauwcPy57fM")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "e8b351fa-93ca-416c-b52c-589e38d9f6a3")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS", "2109516065").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","linkshortfybot")