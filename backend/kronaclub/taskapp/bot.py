import os
import telebot


def send_message_telegram(chat_id, text):
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    bot = telebot.TeleBot(token)
    if chat_id:
        bot.send_message(chat_id, text)
