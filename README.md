# ArXiv Telegram Bot

This is a Telegram bot that filters ArXiv newsletter items based on user-defined keywords. The user can add, list, and remove keywords that will be used to filter the newsletter.

## Features

- Add keywords to filter ArXiv newsletter.
- List all added keywords.
- Remove specific keywords.
- Automatically filter newsletter by pasting it into the chat.
- Uses a webhook for efficient updates from Telegram.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Create a `.env` file in the project root and add the following variables:

```env
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
WEBHOOK_URL=https://yourdomain.com/webhook
```

Replace `your-telegram-bot-token` with your actual Telegram bot token, and `https://yourdomain.com/webhook` with the actual URL where your bot will be hosted.

### Running the Bot

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/yourusername/arxiv-telegram-bot.git
   cd arxiv-telegram-bot
   ```

2. **Build and run the Docker container**:
   
   ```bash
   docker-compose up --build
   ```

This will build the Docker image and start the bot using the specified webhook URL.

### Usage

- Start the bot by sending `/start` in the Telegram chat.
- Add keywords using `/add <keyword>`.
- List keywords using `/list`.
- Remove keywords using `/remove <keyword>`.
- Paste the ArXiv newsletter directly into the chat to filter it based on your keywords.

### Deployment

Ensure that your server's public URL matches the `WEBHOOK_URL` in the `.env` file. Telegram will send updates to this URL, so it must be accessible over the internet.

### Notes

- The bot uses Flask to handle incoming webhook requests from Telegram.
- Docker is used to containerize the bot for easy deployment and scaling.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.