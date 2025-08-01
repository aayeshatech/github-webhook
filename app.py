from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])  # ← Must include 'POST'
def webhook():
    data = request.json
    print("✅ Webhook received:", data)
    return '', 200

@app.route('/')
def home():
    return "Webhook Listener is Live!"
