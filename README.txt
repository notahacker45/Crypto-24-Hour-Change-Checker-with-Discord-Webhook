Crypto Price Tracker Webhook

A simple Python script that fetches cryptocurrency price changes and posts a ranked summary to a webhook (e.g., Discord).

Features
- Fetches price change percentages for Bitcoin, Ethereum, and Solana using the CoinGecko API.
- Sends a nicely formatted message to a Discord (or other) webhook.
- Timestamped messages in your local timezone.
- Easy to configure with a `.env` file for API keys and webhook URLs.

Installation
1. Clone the repository:
git clone https://github.com/yourusername/owenpy.git
cd owenpy

2. (Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

Configuration
1. Create a `.env` file in the project root:
COIN_API_KEY=your_coin_api_key_here
WEBHOOK_URL=your_webhook_url_here

2. Make sure `.env` is ignored by Git.

Usage
Run the script:
python main.py

Dependencies
- requests
- python-dotenv

License
MIT License

Notes
- Do not commit your `.env` file to GitHub.
- You can modify the list of coins or webhook format in main.py.
