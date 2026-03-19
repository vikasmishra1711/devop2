from flask import Flask, request

app = Flask(__name__)






print("vikash mishra")

@app.route('/github-webhooks/', methods=['POST'])
def webhook():
    print(request.json)
    return "OK", 200