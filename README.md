# Example Bot from "Build your own bot"-Workshop
Build a simple Python Telegram Bot that displays top news headlines.

We use the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) wrapper and the [NewsAPI.org Python client](https://newsapi.org/docs/client-libraries/python).

## Getting Started

1. Create a new bot with Telegram's BotFather (https://t.me/BotFather)

2. Insert the bot's token in `bot.py`.

3. Register at https://newsapi.org to get your personalized token.

4. Insert NewsAPI token in `news_api.py`.

5. Set up virtual environment and activate it:
```
virtualenv -p python3.7 env
. env/bin/activate
```
6. Install dependencies:
`pip install python-telegram-bot newsapi-python`

7. Run Chatbot:
`python bot.py`

Have fun with your bot!
