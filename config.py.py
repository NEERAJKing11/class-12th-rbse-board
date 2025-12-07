# config.py

import os

# BOT_TOKEN को Render Environment Variables से लिया जाएगा।
# सुनिश्चित करें कि आपने Render पर BOT_TOKEN को अपनी असली वैल्यू दी है।
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# भुगतान और संपर्क जानकारी
UPI_ID = "7726933135@fam"
UPI_NAME = "Kamlesh kumawat"
PAYMENT_AMOUNT = "49" 
SUPPORT_TELEGRAM_LINK = "https://t.me/RoyalKing_7X4"

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN is not set in environment variables.")
    # यह बॉट को क्रैश होने से रोकेगा अगर टोकन सेट नहीं है