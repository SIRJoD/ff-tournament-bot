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
import telebot
import threading
from flask import Flask

# Your bot token
bot = telebot.TeleBot("7727916729:AAF6yCG8kNhw1GZyYomCXvgPPsao_O_bSc4")

# Start polling in a thread
def run_bot():
    bot.polling(non_stop=True)

# Fake web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# Run both in parallel
threading.Thread(target=run_bot).start()
threading.Thread(target=run_flask).start()

bot.polling()
