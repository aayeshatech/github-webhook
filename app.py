from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "GitHub Webhook is Live!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        event = request.headers.get('X-GitHub-Event', 'ping')
        payload = request.json
        print(f"🔔 GitHub Event: {event}")
        print(f"📦 Payload: {payload}")
        return '', 200
    else:
        abort(400)
