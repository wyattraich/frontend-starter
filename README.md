# Perpetuity – AI Coding Challenge (Frontend Engineer)

Welcome to the Perpetuity coding challenge.

This is a **45-minute, AI-assisted pair coding interview**. Use any tools you'd like — Copilot, ChatGPT, docs, or Stack Overflow. The goal is not to memorize APIs but to **reason through and build a composable vertical slice** of our system.

---

## 🧠 Objective

Implement a simple **real-time orderbook view and trade entry screen** , based on the design you shared in the last round. Focus on the core functionality — no need to polish or complete every feature.

---

## 🧱 Scope

### ✅ Part 1: Orderbook Visualization

There is a python server in the server folder

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

Use any framework to subscribe to this websocket and display the data

### ✅ Part 2: Trade Entry screen

Build a basic component to allow users to submit market orders (no API needed)

As discussed in the system design portion, the inputs for a user should be $ amount, leverage 1-100x, long/short
