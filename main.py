import requests
from dotenv import load_dotenv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

#FOR THE FOLLOWING MAKE A .ENV FILE WITH CONTENTS LIKE: COIN_API_KEY=<api_key>
load_dotenv()
api_key = os.getenv("COIN_API_KEY")

WEBHOOK_URL = 'ENTER WEBHOOK URL HERE'

def get_prices():
    coins = ['bitcoin', 'ethereum', 'solana']
    params = {
        'ids' : ','.join(coins),
        'vs_currency' : 'usd',
        "x_cg_demo_api_key": api_key
    }
    url = f'https://api.coingecko.com/api/v3/coins/markets'
    req = requests.get(url, params=params)
    data = req.json()
    coin_dict = {}
    for coin in data:
        if 'id' in coin and 'price_change_percentage_24h' in coin:
            name = coin['id']
            value = coin['price_change_percentage_24h']
            coin_dict[name] = value
    ranked_list = sorted(coin_dict.items(), key=lambda item: item[1], reverse=True)
    current_time = datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S")
    message = '\n'.join([f"{i}. {coin.capitalize()}: {value:.2f}% recorded at {current_time}" for i, (coin, value) in enumerate(ranked_list, start=1)])
    return message


def send_webhook(message, webhook):
    data = {'content' : message}
    response = requests.post(webhook, json=data)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

def main():
    try:
        message = get_prices()
        send_webhook(message, WEBHOOK_URL)
    except Exception as e:
        print("Error in main", e)

if __name__ == '__main__':
    main()






    







