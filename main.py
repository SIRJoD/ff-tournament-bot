import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("7727916729:AAF6yCG8kNhw1GZyYomCXvgPPsao_O_bSc4")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/GIVIWAYS"),
        InlineKeyboardButton("TOURNAMENT", url="https://falconfreefiretournament.netlify.app/")
    )

    with open("ff.png.jpg", "rb") as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=(
                "🇮🇳 *Welcome to India's most trusted Free Fire Tournament!*\n\n"
                "• Join channel for updates 📢\n"
                "• Click the second button to participate 🎮"
            ),
            parse_mode="Markdown",
            reply_markup=markup
        )

bot.polling()
