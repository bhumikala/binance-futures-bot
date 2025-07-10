# Binance Futures Trading Bot

This is a simplified Python bot built for the Binance USDT-M Futures Testnet.
It can place Market, Limit, and Stop-Market orders using user inputs via command-line interface.

> Submitted as part of the Junior Python Developer – Crypto Trading Bot hiring task.

#Features

- Connects to Binance Futures Testnet
- Places BUY and SELL orders
- Supports Market, Limit, and Stop-Market order types
- Secure API handling using `.env`
- Logs API responses and errors to `bot.log`

How to Run the Bot

1. Install required libraries
pip install -r requirements.txt

2.Create a .env file in the same folder:
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_secret_here

3.Run the bot
python run_bot.py

You’ll be asked to input:
Symbol (e.g., BTCUSDT)
Side (BUY or SELL)
Order Type (MARKET / LIMIT / STOP_MARKET)
Quantity
(Optional: price or stop price)

binance-futures-bot/
├basic_bot.py         # Bot logic
├run_bot.py           # CLI interface
├utils.py             # Loads API keys
├requirements.txt     # Dependencies
├.gitignore           # Ignores .env and logs
├bot.log              # Auto-generated log
└README.md            # Project description

Security Notes
API keys are loaded from a .env file and not uploaded to GitHub.
All trading is done on Binance Testnet, not real funds.
