
import os

# Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8480511759:AAEHhSJRxyUBGuKdpxVP8LGr_zmmrA5IpZE")

# Your API ID & Hash
API_ID = int(os.environ.get("API_ID", "22451491"))
API_HASH = os.environ.get("API_HASH", "28e74942125f7e4968398ea651cd417b")

# Your Owner / Admin Id For Broadcast 
ADMINS = [int(id) for id in os.environ.get("ADMINS", "6574393060,5360305806").split(",")]

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted2")

# Log Channel to Track New Users 
LOG_CHANNEL = -1002741915396  # replace with your log channel id

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then False
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Keep-Alive URL
KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "")


# Rexbots
# Don't Remove Credit 🥺
# Telegram Channel @RexBots_Official
