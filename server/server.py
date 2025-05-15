import asyncio
import json
import random
import websockets
from datetime import datetime

# Constants
SYMBOL = "AAPL"
PRICE_BASE = 180.00
FREQ_MS = 2000  # Frequency in milliseconds
LEVELS = 20  # Orderbook depth

def generate_orderbook():
    asks = []
    bids = []
    for i in range(LEVELS):
        ask_price = round(PRICE_BASE + 0.1 * i + random.uniform(0.01, 0.05), 2)
        bid_price = round(PRICE_BASE - 0.1 * i - random.uniform(0.01, 0.05), 2)
        size = round(random.uniform(1, 10), 2)
        asks.append({ "price": ask_price, "size": size })
        bids.append({ "price": bid_price, "size": size })
    return {
        "symbol": SYMBOL,
        "timestamp": datetime.utcnow().isoformat(),
        "asks": asks,
        "bids": bids,
    }

async def stream_orderbook(websocket):
    while True:
        data = generate_orderbook()
        await websocket.send(json.dumps(data))
        await asyncio.sleep(FREQ_MS / 1000.0)

async def main():
    async with websockets.serve(stream_orderbook, "localhost", 8765):
        print("✅ WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
