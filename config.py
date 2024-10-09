from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
      API_ID = int(getenv("API_ID", "28776072"))
      AS_COPY = True if getenv("AS_COPY", False) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7291479898:AAEOcnAWa15wcBoVY2pH13PRmdPl3r6TSco")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002261985371:-1002487385156").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
