import requests
import telepot
import time
import os
from datetime import datetime

url = os.getenv("URL")
if not url:
    raise ValueError("URL environment variable is required")

token = os.getenv("TOKEN")
if not token:
    raise ValueError("TOKEN environment variable is required")

chat_id = os.getenv("CHAT_ID")
if not chat_id:
    raise ValueError("CHAT_ID environment variable is required")

target_category_id_str = os.getenv("TARGET_CATEGORY_ID")
if not target_category_id_str:
    raise ValueError("TARGET_CATEGORY_ID environment variable is required")
try:
    target_category_id = int(target_category_id_str)
except ValueError:
    raise ValueError(f"Invalid TARGET_CATEGORY_ID: {target_category_id_str}")


bot = telepot.Bot(token)

def check_tickets():
    try:
        response = requests.get(url).json()

        ticket_categories = response.get("ticketCategories", [])

        for category in ticket_categories:
            if category.get("id") == target_category_id:
                maximum_saleable_tickets = category.get("maximumSaleableTickets")
                if maximum_saleable_tickets > 0:
                    message = f"Category ID {target_category_id} has {maximum_saleable_tickets} tickets available!"
                    bot.sendMessage(chat_id, message)
                    print(f"{datetime.now()} - Notification sent to Telegram")
                else:
                    print(f"{datetime.now()} - No tickets available for category ID {target_category_id}")
                break
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    while True:
        check_tickets()
        time.sleep(10)
