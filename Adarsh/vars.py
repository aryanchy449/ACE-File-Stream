# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID',"23080322"))
    API_HASH = str(getenv('API_HASH',"b3611c291bf82d917637d61e4a136535"))
    BOT_TOKEN = str(getenv('BOT_TOKEN',"6931048916:AAEiwn5cej-PVBw95cqsGskW-BEGx95o4jY"))
    SESSION_NAME = str(getenv('SESSION_NAME', 'F2LxBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL',"-1002072662567"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', "https://miniature-gae-telegram-bots-7a6a60ef.koyeb.app/"))
    OWNER_ID = int(getenv('OWNER_ID', 6214889840))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME',"aryanchy449"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN',"https://miniature-gae-telegram-bots-7a6a60ef.koyeb.app/")) if not ON_HEROKU or getenv('FQDN',""https://miniature-gae-telegram-bots-7a6a60ef.koyeb.app/) else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
