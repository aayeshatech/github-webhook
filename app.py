from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ GitHub Webhook Listener is Live!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    event = request.headers.get('X-GitHub-Event', 'ping')
    payload = request.json
    print(f"📥 Event: {event}")
    print(f"📦 Payload: {payload}")
    return '', 200

if __name__ == '__main__':
    # IMPORTANT for Render to bind to 0.0.0.0
    app.run(host='0.0.0.0', port=10000)
