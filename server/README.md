# Orderbook WebSocket Mock Server

This project generates and streams synthetic orderbook data over a WebSocket, simulating a live feed for use in frontend interviews or UI prototyping.

## 🔧 Features
- Publishes fake orderbook data for a given symbol (default: `AAPL`)
- Sends updates every 250ms
- Randomized bid/ask prices and sizes

## 🛠️ Requirements
- Python 3.8+
- `websockets` library

## 📦 Setup

```bash
pip install -r requirements.txt
python server.py
```

The server will start at: `ws://localhost:8765`

## 📡 Example Message

```json
{
  "symbol": "AAPL",
  "timestamp": "2025-05-15T19:48:32.123Z",
  "asks": [{ "price": 180.12, "size": 3.21 }, ...],
  "bids": [{ "price": 179.98, "size": 6.44 }, ...]
}
```

## 👤 For Use In

This is a great mock backend to test real-time frontends, especially in interviews for trading UIs, dashboards, or consumer financial applications.
