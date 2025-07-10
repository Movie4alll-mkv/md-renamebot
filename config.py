import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", 6534707))
    API_HASH = os.environ.get("API_HASH" ,"4bcc61d959a9f403b2f20149cbbe627a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1430593323))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://nhere118:jSsmgEs1uEqnlbrZ@cluster0.rdkih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
