import os
import re
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# A dictionary to store keywords for each user
user_keywords = {}

# Function to start the bot and set a welcome message
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome! Use /add to add keywords, /list to list keywords, /remove to remove a keyword, and /filter to filter ArXiv newsletters.')

# Function to add keywords
def add_keyword(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    keyword = ' '.join(context.args).lower()

    if user_id not in user_keywords:
        user_keywords[user_id] = []

    if keyword and keyword not in user_keywords[user_id]:
        user_keywords[user_id].append(keyword)
        update.message.reply_text(f'Keyword "{keyword}" added.')
    else:
        update.message.reply_text('Please provide a valid keyword or the keyword already exists.')

# Function to list all keywords for the user
def list_keywords(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    keywords = user_keywords.get(user_id, [])
    
    if keywords:
        update.message.reply_text(f'Your keywords: {", ".join(keywords)}')
    else:
        update.message.reply_text('You have no keywords. Use /add to add some.')

# Function to remove a keyword
def remove_keyword(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    keyword = ' '.join(context.args).lower()

    if user_id in user_keywords and keyword in user_keywords[user_id]:
        user_keywords[user_id].remove(keyword)
        update.message.reply_text(f'Keyword "{keyword}" removed.')
    else:
        update.message.reply_text('Keyword not found.')

# Function to split the newsletter into individual papers
def split_newsletter(newsletter: str):
    papers = newsletter.split('------------------------------------------------------------------------------\n\\')
    return papers

# Function to filter papers based on keywords
def filter_papers(papers, keywords):
    filtered_papers = []
    for paper in papers:
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', paper, re.IGNORECASE):
                filtered_papers.append(paper)
                break
    return filtered_papers

# Function to filter the newsletter
def filter_newsletter(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    keywords = user_keywords.get(user_id, [])
    
    if not keywords:
        update.message.reply_text('You have no keywords. Use /add to add some.')
        return
    
    newsletter = context.args[0]  # Assuming the entire newsletter text is passed as an argument
    papers = split_newsletter(newsletter)
    filtered_papers = filter_papers(papers, keywords)

    if filtered_papers:
        for paper in filtered_papers:
            update.message.reply_text(paper)
    else:
        update.message.reply_text('No papers found matching your keywords.')

# Main function to handle bot commands
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add", add_keyword))
    dp.add_handler(CommandHandler("list", list_keywords))
    dp.add_handler(CommandHandler("remove", remove_keyword))
    dp.add_handler(CommandHandler("filter", filter_newsletter))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
