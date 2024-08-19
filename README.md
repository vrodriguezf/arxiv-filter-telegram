# ArXiv Telegram Bot

This is a Telegram bot that filters ArXiv newsletter items based on user-defined keywords. The user can add, list, and remove keywords that will be used to filter the newsletter.

## Features

- Add keywords to filter ArXiv newsletter.
- List all added keywords.
- Remove specific keywords.
- Automatically filter newsletter by pasting it into the chat.

## Setup

1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
```
3. Create the Telegram Bot. You'll need to create a bot on Telegram and get the token. You can do this by talking to the BotFather on Telegram. Once you have the token.
4. Create a `.env` file and add the variable `TELEGRAM_BOT_TOKEN`there with the token that you got.
5. Run the bot with `python bot.py`.