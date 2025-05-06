# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23476863")

API_HASH = os.environ.get("API_HASH", "69daa0835439c4211f34c2e9ad0acb5c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7722185407:AAEvgoIfp9buMXITMRJdEag9xe1nHGeUlAM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "New_Anime_Hindi_Dub_Series") 

         

DB_NAME = os.environ.get("DB_NAME", "haruto")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://haruto:<haruto@2025>@otakunexus.aaol7be.mongodb.net/?retryWrites=true&w=majority&appName=Otakunexus")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6617544956').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
