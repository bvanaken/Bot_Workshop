from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def send_buttons(update, context, text, buttons):
    button_list = [InlineKeyboardButton(button_text, callback_data=button_text)
                   for button_text in buttons]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text,
                             parse_mode="markdown",
                             reply_markup=InlineKeyboardMarkup([button_list]))


def hide_buttons(update, context, text=None):
    reply_markup = []

    context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
        text=update.effective_message.text if text is None else text,
        reply_markup=InlineKeyboardMarkup(reply_markup)
    )
