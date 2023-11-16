from flask import Flask, request, abort
import hmac, hashlib, os, subprocess, logging

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Verify the request signature
    signature = request.headers.get('X-Hub-Signature')
    if signature is None:
        abort(403)

    sha_name, signature = signature.split('=')
    if sha_name != 'sha1':
        abort(501)

    # Process the push event
    event = request.headers.get('X-GitHub-Event', 'No event type found')
    if event == 'push':
        hello_world()

    # Print the payload
    payload = request.get_json()
    print(payload)

    return '', 200

def hello_world():
    print("hello world")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)