from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("TradingBotLogger")
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler("bot.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type='MARKET', quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type='LIMIT', timeInForce='GTC',
                    quantity=quantity, price=price
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type='STOP_MARKET',
                    stopPrice=stop_price, closePosition=False, quantity=quantity
                )
            else:
                raise ValueError("Unsupported order type")

            self.logger.info(f"ORDER SUCCESS: {order}")
            print("Order Placed Successfully")
            return order

        except Exception as e:
            self.logger.error(f"ORDER FAILED: {e}")
            print(f" Order Failed: {e}")
