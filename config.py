from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10611700"))
API_HASH = getenv("API_HASH", "361289d28136f05d1767bbdc6959f6fa")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","MUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "Musicanes1_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "N_B_1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "N_B_10")
chanel_bot = getenv("chanel_bot", "N_B_10
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/30c291bae8a73cf534d4a.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/0ec205b01aa7c2faf47a3.mp4")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5341342370").split()))
