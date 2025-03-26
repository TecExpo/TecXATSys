import pytz
from datetime import datetime, time

# Define exchange trading hours and time zones
EXCHANGES = {
    "NSE": {"timezone": "Asia/Kolkata", "open": time(9, 15), "close": time(15, 30)},
    "BSE": {"timezone": "Asia/Kolkata", "open": time(9, 15), "close": time(15, 30)},
    "NYSE": {"timezone": "America/New_York", "open": time(9, 30), "close": time(16, 0)},
    "NASDAQ": {"timezone": "America/New_York", "open": time(9, 30), "close": time(16, 0)},
    "LSE": {"timezone": "Europe/London", "open": time(8, 0), "close": time(16, 30)},
    "JPX": {"timezone": "Asia/Tokyo", "open": time(9, 0), "close": time(15, 0)},
    "SSE": {"timezone": "Asia/Shanghai", "open": time(9, 30), "close": time(15, 0)},
    "HKEX": {"timezone": "Asia/Hong_Kong", "open": time(9, 30), "close": time(16, 0)},
    "Euronext": {"timezone": "Europe/Paris", "open": time(9, 0), "close": time(17, 30)},
    "TSX": {"timezone": "America/Toronto", "open": time(9, 30), "close": time(16, 0)},
    "ASX": {"timezone": "Australia/Sydney", "open": time(10, 0), "close": time(16, 0)},
    "SGX": {"timezone": "Asia/Singapore", "open": time(9, 0), "close": time(17, 0)},
}

def get_local_time(timezone):
    """Returns the current time in the given timezone."""
    tz = pytz.timezone(timezone)
    return datetime.now(tz).time()

def is_market_open(exchange):
    """Checks if the given exchange is currently open."""
    info = EXCHANGES.get(exchange)
    if not info:
        return False
    local_time = get_local_time(info["timezone"])
    return info["open"] <= local_time <= info["close"]

def get_active_exchange():
    """Finds the currently active exchange based on session timings."""
    for exchange, details in EXCHANGES.items():
        if is_market_open(exchange):
            return exchange
    return None

if __name__ == "__main__":
    active_exchange = get_active_exchange()
    if active_exchange:
        print(f"Trading on {active_exchange} (Market Open)")
    else:
        print("No active exchange at the moment.")
