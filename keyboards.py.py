# keyboards.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import UPI_ID, UPI_NAME, PAYMENT_AMOUNT, SUPPORT_TELEGRAM_LINK
from links import PARISHRAM_LINKS, HUNKER_LINKS, PYQ_LINKS, QB_LINKS, TARGET_BATCH_DATA

# UPI भुगतान लिंक जनरेट करें
UPI_PAYMENT_URL = f"upi://pay?pa={UPI_ID}&pn={UPI_NAME.replace(' ', '%20')}&am={PAYMENT_AMOUNT}&cu=INR"

# --- 1. मुख्य मेनू ---
def get_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("💰 अभी ₹49 का भुगतान करें (Unlock All)", url=UPI_PAYMENT_URL)],
        [InlineKeyboardButton("1. 🔥 Hunker Batch Links", callback_data="show_hunker")],
        [InlineKeyboardButton("2. परिश्रम 2026 PW हिंदी Batch", url=PARISHRAM_LINKS["parishram_2026"])],
        [InlineKeyboardButton("3. परिश्रम 2.0 2026 हिंदी Batch", url=PARISHRAM_LINKS["parishram_2_0"])],
        [InlineKeyboardButton("4. 🎯 टारगेट बैच लिंक्स", callback_data="show_target")],
        [InlineKeyboardButton("5. 📝 PYQ लिंक्स", callback_data="show_pyq")],
        [InlineKeyboardButton("6. 📚 प्रश्न बैंक लिंक्स", callback_data="show_qbank")],
        [InlineKeyboardButton("📞 सपोर्ट के लिए संपर्क करें", url=SUPPORT_TELEGRAM_LINK)]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- 2. Hunker मेनू ---
def get_hunker_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇮🇳 Hunker Batch (हिंदी)", url=HUNKER_LINKS["hindi"]),
            InlineKeyboardButton("🇬🇧 Hunker Batch (English)", url=HUNKER_LINKS["english"])
        ],
        [InlineKeyboardButton("← मुख्य मेनू पर वापस जाएँ", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- 3. PYQ मेनू ---
def get_pyq_keyboard():
    keyboard = [
        [InlineKeyboardButton("⚛️ भौतिक विज्ञान", url=PYQ_LINKS["physics"])],
        [InlineKeyboardButton("🧪 रसायन विज्ञान", url=PYQ_LINKS["chemistry"])],
        [InlineKeyboardButton("🌱 जीव विज्ञान", url=PYQ_LINKS["biology"])],
        [InlineKeyboardButton("← मुख्य मेनू पर वापस जाएँ", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- 4. Question Bank मेनू ---
def get_qbank_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("⚛️ भौतिक विज्ञान", url=QB_LINKS["physics"]),
            InlineKeyboardButton("🧪 रसायन विज्ञान", url=QB_LINKS["chemistry"])
        ],
        [
            InlineKeyboardButton("🌱 जीव विज्ञान", url=QB_LINKS["biology"]),
            InlineKeyboardButton("🇮🇳 हिन्दी", url=QB_LINKS["hindi"])
        ],
        [InlineKeyboardButton("🇬🇧 अंग्रेजी", url=QB_LINKS["english"])],
        [InlineKeyboardButton("← मुख्य मेनू पर वापस जाएँ", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- 5. Target Batch (विषय चुनाव) ---
def get_target_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("⚛️ भौतिक विज्ञान (14 दिन)", callback_data="target_physics_menu")],
        [InlineKeyboardButton("🧪 रसायन विज्ञान (10 दिन)", callback_data="target_chemistry_menu")],
        [InlineKeyboardButton("🌱 जीव विज्ञान (14 दिन)", callback_data="target_biology_menu")],
        [InlineKeyboardButton("← मुख्य मेनू पर वापस जाएँ", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- 6. Target Batch (दिनों के लिंक्स) ---
def get_target_subject_keyboard(subject):
    """दिए गए विषय के लिए सभी Day बटनों को जनरेट करता है।"""
    
    data = TARGET_BATCH_DATA.get(subject)
    
    if not data:
        return get_target_menu_keyboard() 

    links = data["links"]
    days = data["days"] 
    
    keyboard = []
    current_row = []
    
    for i in range(1, days + 1):
        url = links[i]
        button = InlineKeyboardButton(f"Day {i}", url=url)
        
        current_row.append(button)
        
        # प्रति पंक्ति 4 बटन
        if len(current_row) == 4:
            keyboard.append(current_row)
            current_row = []
            
    if current_row:
        keyboard.append(current_row)
        
    # वापस विषय चुनाव मेनू पर जाने का बटन
    keyboard.append([InlineKeyboardButton("← विषय चुनाव पर वापस जाएँ", callback_data="show_target")])
    
    return InlineKeyboardMarkup(keyboard)