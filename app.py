from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# ✅ Simple UI Page
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps App - Vikas</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: #e2e8f0;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #38bdf8;
        }
        .box {
            background: #1e293b;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        .highlight {
            color: #22c55e;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚀 DevOps Learning App</h1>
        <p>Welcome to <span class="highlight">Vikas DevOps Project</span></p>
        <p>CI/CD Pipeline: <span class="highlight">Jenkins + Docker + Ansible + AWS</span></p>
        <p>Status: <span class="highlight">Running Successfully ✅</span></p>
        <p>Time: {{ time }}</p>
    </div>
</body>
</html>
"""

# ✅ Home Route (UI)
@app.route('/')
def home():
    return render_template_string(HTML_PAGE, time=datetime.datetime.now())

# ✅ GitHub Webhook Route
@app.route('/github-webhooks/', methods=['POST'])
def webhook():
    data = request.json
    print("📦 Webhook Received:", data)
    return "Webhook Received", 200

# ✅ Health Check (for DevOps)
@app.route('/health')
def health():
    return {"status": "healthy"}, 200

# ✅ IMPORTANT (fix for Docker)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)