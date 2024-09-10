import requests
import telepot
import time
import os
from datetime import datetime

url = 'https://reg.devoxx.be/api/v2/public/event/2024/ticket-categories'

bot = telepot.Bot(os.getenv("TOKEN"))
chat_id = os.getenv("CHAT_ID")


def check_tickets():
    try:
        response = requests.get(url).json()

        ticket_categories = response.get("ticketCategories", [])

        target_category_id = 46

        for category in ticket_categories:
            if category.get("id") == target_category_id:
                maximum_saleable_tickets = category.get("maximumSaleableTickets")
                if maximum_saleable_tickets > 0:
                    message = f"Category ID {target_category_id} has {maximum_saleable_tickets} tickets available!"
                    bot.sendMessage(chat_id, message)
                    print(f"{datetime.now()} - Notification sent to Telegram")
                else:
                    print(f"{datetime.now()} - No tickets available for category ID 46")
                break
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    while True:
        check_tickets()
        time.sleep(10)