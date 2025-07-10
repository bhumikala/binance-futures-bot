from basic_bot import BasicBot
from utils import load_keys

def main():
    print("🔹 Binance Futures Testnet Bot 🔹")

    api_key, api_secret = load_keys()
    bot = BasicBot(api_key, api_secret)

    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (BUY / SELL): ").upper()
    order_type = input("Order Type (MARKET / LIMIT / STOP_MARKET): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    stop_price = None

    if order_type == 'LIMIT':
        price = input("Enter limit price: ")
    if order_type == 'STOP_MARKET':
        stop_price = input("Enter stop price: ")

    bot.place_order(symbol, side, order_type, quantity, price, stop_price)

if __name__ == "__main__":
    main()
