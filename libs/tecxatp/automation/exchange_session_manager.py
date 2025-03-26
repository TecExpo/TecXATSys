import requests
from datetime import datetime
import pytz

# Initialize TradingHours API credentials
API_KEY = 'your_tradinghours_api_key'
BASE_URL = 'https://api.tradinghours.com/v3'

def get_market_status(exchange_code):
    """
    Fetches the current market status for a given exchange.
    """
    endpoint = f"{BASE_URL}/market-status"
    params = {
        'api_key': API_KEY,
        'exchange': exchange_code
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data

def is_market_open(exchange_code):
    """
    Determines if the specified market is currently open.
    """
    status = get_market_status(exchange_code)
    return status['is_open']

def get_active_exchange(exchange_codes):
    """
    Iterates through a list of exchange codes and returns the first one that is open.
    """
    for code in exchange_codes:
        if is_market_open(code):
            return code
    return None

if __name__ == "__main__":
    # List of exchange codes to monitor
    exchanges = ['NSE', 'BSE', 'NYSE', 'NASDAQ', 'LSE', 'JPX', 'SSE', 'HKEX', 'Euronext', 'TSX', 'ASX', 'SGX']

    active_exchange = get_active_exchange(exchanges)
    if active_exchange:
        print(f"Trading on {active_exchange} (Market Open)")
        # Place your trading logic here
    else:
        print("No active exchange at the moment.")
