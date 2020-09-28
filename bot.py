import logging
import random

from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler

import news_api
import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

TOKEN = "FILL_IN"


def start_bot():
    # 1. Build Updater
    updater = Updater(token=TOKEN, use_context=True)

    # 2. Message Dispatcher
    dispatcher = updater.dispatcher

    message_handler = MessageHandler(Filters.all, say_hello)
    dispatcher.add_handler(message_handler)

    button_handler = CallbackQueryHandler(button_reaction)
    dispatcher.add_handler(button_handler)

    # 3. Start Polling
    updater.start_polling()
    logger.info("Waiting for messages...")


def say_hello(update, context):
    logger.info(update)

    context.bot.send_message(chat_id=update.message.chat.id, text="Hallo!")

    utils.send_buttons(update, context, text="Wähle aus diesen Kategorien:",
                       buttons=["Science", "Technology", "Business"])


def button_reaction(update, context):
    message = update.effective_message
    category = update.callback_query.data

    context.bot.send_message(chat_id=message.chat.id, text=f"{category}!")

    top_headlines = news_api.get_api().get_top_headlines(category=f"{category.lower()}", country='de')

    article = random.sample(top_headlines["articles"], k=1)[0]

    title = article["title"]
    description = article["description"]
    url = article["url"]

    context.bot.send_message(chat_id=message.chat.id,
                             text=f"*{title}*\n\n{description}\n\n{url}",
                             parse_mode="markdown")

    utils.send_buttons(update, context, text="Wähle aus diesen Kategorien:",
                       buttons=["Science", "Technology", "Business"])


start_bot()
