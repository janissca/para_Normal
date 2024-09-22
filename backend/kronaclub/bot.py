import os
import telebot
import requests


class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def get_chat_id(self, message):
        self.chat_id = message.chat.id
        self.login = message.from_user.username
        self.bot.send_message(self.chat_id, f"Спасибо за подписку {self.login}! Ваш ID: {self.chat_id}")
        requests.post("http://127.0.0.1:8000/api/v1/telegram/", data={'telegram_id': self.chat_id, 'telegram_login': self.login})

    def send_message(self, chat_id, text):
        if chat_id:
            self.bot.send_message(self.chat_id, text)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.get_chat_id(message)

        self.bot.infinity_polling()


if __name__ == "__main__":
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    bot = TelegramBot(token)
    bot.run()
