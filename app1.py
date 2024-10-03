from flask import Flask, request, jsonify

app = Flask(_name_)

# Default route to test if the server is running
@app.route('/')
def hello_world():
    return 'Hello, World!'

# New route to handle the GitHub webhook
@app.route('/github-webhook/', methods=['POST'])
def github_webhook():
    if request.method == 'POST':
        payload = request.json  # Get the JSON payload sent by GitHub
        if payload:
            print(payload)  # Debug: print the payload to your terminal or log file
            return jsonify({'status': 'success', 'message': 'Webhook received!'}), 200
        else:
            return jsonify({'status': 'failed', 'message': 'No payload received!'}), 400

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
