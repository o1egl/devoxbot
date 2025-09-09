# DevoxBot

A small Python service that polls a Devoxx ticket categories API endpoint and sends a Telegram message when a target category has available tickets.

## Required environment variables

- TOKEN: Telegram bot token
- CHAT_ID: Telegram chat ID (recipient)
- URL: Ticket categories API endpoint to poll
- TARGET_CATEGORY_ID: Integer ID of the ticket category to watch

The application exits with an error if any of these variables are missing or invalid.

## Quick start (Docker)

```bash
# Run the bot (replace values accordingly)
docker run --rm \
  -e TOKEN=123456:ABCDEFyourTelegramBotToken \
  -e CHAT_ID=123456789 \
  -e URL='https://reg.devoxx.be/api/v2/public/event/dvbe25/ticket-categories' \
  -e TARGET_CATEGORY_ID='63' \
  ghcr.io/o1egl/devoxbot:latest
```

## Docker Compose example

```yaml
services:
  devoxbot:
    image: ghcr.io/o1egl/devoxbot:latest
    restart: unless-stopped
    environment:
      TOKEN: ${TOKEN}
      CHAT_ID: ${CHAT_ID}
      URL: https://reg.devoxx.be/api/v2/public/event/dvbe25/ticket-categories
      TARGET_CATEGORY_ID: "63"
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export TOKEN=123456:ABCDEFyourTelegramBotToken
export CHAT_ID=123456789
export URL='https://reg.devoxx.be/api/v2/public/event/dvbe25/ticket-categories'
export TARGET_CATEGORY_ID=63

python main.py
```
