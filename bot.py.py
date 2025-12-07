# bot.py

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, PAYMENT_AMOUNT
from keyboards import (
    get_main_menu_keyboard, get_hunker_keyboard, get_pyq_keyboard, 
    get_qbank_keyboard, get_target_menu_keyboard, get_target_subject_keyboard
)

# लॉगिंग सेटअप
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- मैसेज टेक्स्ट ---
MAIN_MENU_TEXT = f"""
*RBSE Class 12th Target Batch*

🛑 *एक्सेस प्रतिबंधित (Access Restricted)* ⚠️
सभी 6 बैचों और सामग्री को अनलॉक करने के लिए **केवल ₹{PAYMENT_AMOUNT} का एक बार भुगतान करें**।

---
📚 सभी बैच/सामग्री (All Batches/Content)
नीचे दिए गए किसी भी बटन को दबाएँ या भुगतान करें।
"""

# --- कमांड हैंडलर ---
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start कमांड को संभालता है और मुख्य मेनू भेजता है।"""
    if update.message:
        await update.message.reply_text(
            MAIN_MENU_TEXT, 
            reply_markup=get_main_menu_keyboard(), 
            parse_mode='Markdown'
        )

# --- कॉल बैक क्वेरी हैंडलर (जब कोई बटन दबाता है) ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Inline Keyboard के सभी बटन प्रेस को संभालता है।"""
    query = update.callback_query
    await query.answer() # बटन प्रेस की पुष्टि करें

    data = query.data

    if data == "main_menu":
        # मुख्य मेनू पर वापस जाएँ
        await query.edit_message_text(
            MAIN_MENU_TEXT,
            reply_markup=get_main_menu_keyboard(),
            parse_mode='Markdown'
        )

    elif data == "show_hunker":
        text = "🔥 Hunker Batch Links (हिंदी / English)\n\n🛑 कृपया भुगतान करके एक्सेस अनलॉक करें।"
        await query.edit_message_text(text, reply_markup=get_hunker_keyboard(), parse_mode='Markdown')
        
    elif data == "show_pyq":
        text = "📝 पिछले वर्ष के प्रश्न पत्र (PYQ) लिंक्स\n\n🛑 कृपया भुगतान करके एक्सेस अनलॉक करें।"
        await query.edit_message_text(text, reply_markup=get_pyq_keyboard(), parse_mode='Markdown')

    elif data == "show_qbank":
        text = "📚 प्रश्न बैंक लिंक्स (Question Bank)\n\n🛑 कृपया भुगतान करके एक्सेस अनलॉक करें।"
        await query.edit_message_text(text, reply_markup=get_qbank_keyboard(), parse_mode='Markdown')
        
    elif data == "show_target":
        # Target Subject Selection Menu दिखाएँ
        text = "🎯 Target Batch Links (RBSE 12th)\n\n🛑 कृपया भुगतान करके एक्सेस अनलॉक करें।\n\nकृपया विषय चुनें:"
        await query.edit_message_text(text, reply_markup=get_target_menu_keyboard(), parse_mode='Markdown')

    elif data.endswith("_menu"):
        # Target Subject Days Menu दिखाएँ (e.g., target_physics_menu)
        subject = data.split("_")[1]
        subject_name_map = {"physics": "⚛️ भौतिक विज्ञान", "chemistry": "🧪 रसायन विज्ञान", "biology": "🌱 जीव विज्ञान"}
        
        text = f"🎯 {subject_name_map.get(subject, subject.capitalize())} - सभी दिन के लिंक्स\n\n🛑 कृपया भुगतान करके एक्सेस अनलॉक करें।"
        await query.edit_message_text(
            text, 
            reply_markup=get_target_subject_keyboard(subject), 
            parse_mode='Markdown'
        )
        

def main() -> None:
    """बॉट को शुरू करता है।"""
    # BOT_TOKEN चेक करें (Render पर यह सेट होना चाहिए)
    if not BOT_TOKEN:
        logger.error("Stopping bot: BOT_TOKEN is missing.")
        return

    # Application को BOT_TOKEN से बनाएं
    application = Application.builder().token(BOT_TOKEN).build()

    # कमांड हैंडलर जोड़ें
    application.add_handler(CommandHandler("start", start_command))

    # Callback Query हैंडलर जोड़ें
    application.add_handler(CallbackQueryHandler(button_handler))

    # बॉट को पोलिंग मोड में चलाएं
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()