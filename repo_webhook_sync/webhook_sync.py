from flask import Flask, request, abort
import hmac, hashlib, os, subprocess, logging

app = Flask(__name__)
WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET')
SOURCE_REPO_PATH = os.path.join(os.getcwd(), 'source_repo')
TARGET_REPO_PATH = os.path.join(os.getcwd(), 'target_repo')
SOURCE_GITHUB_TOKEN = os.environ['SOURCE_GITHUB_PAT']
TARGET_GITHUB_TOKEN = os.environ['TARGET_GITHUB_PAT']
# Fill out ghes hostname and org/repo
SOURCE_REPO_URL = f'https://{SOURCE_GITHUB_TOKEN}@< ghes hostname >/< org/repo >'
# Fill out org/repo
TARGET_REPO_URL = f'https://x-access-token:{TARGET_GITHUB_TOKEN}@github.com/< org/repo >'

@app.route('/webhook', methods=['POST'])
def webhook():
    # Verify the request signature
    signature = request.headers.get('X-Hub-Signature')
    if signature is None:
        abort(403)

    sha_name, signature = signature.split('=')
    if sha_name != 'sha1':
        abort(501)

    mac = hmac.new(WEBHOOK_SECRET.encode(), msg=request.data, digestmod=hashlib.sha1)
    if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
        abort(403)

    # Process the push event
    event = request.headers.get('X-GitHub-Event', 'No event type found')
    if event == 'push':
        sync_repos()

    return '', 200

def sync_repos():
    # Clone the source repository if it doesn't exist
    if not os.path.exists(SOURCE_REPO_PATH):
        subprocess.run(['git', 'clone', SOURCE_REPO_URL, SOURCE_REPO_PATH])
        logging.info('Cloned source repository')

    # Pull the latest changes from the source repository
    subprocess.run(['git', 'pull'], cwd=SOURCE_REPO_PATH)
    logging.info('Pulled latest changes from source repository')

    # Clone the target repository if it doesn't exist
    if not os.path.exists(TARGET_REPO_PATH):
        subprocess.run(['git', 'clone', TARGET_REPO_URL, TARGET_REPO_PATH])
        logging.info('Cloned target repository')

    # Push the changes to the target repository
    subprocess.run(['git', 'push', '--force', TARGET_REPO_URL], cwd=SOURCE_REPO_PATH)
    logging.info('Pushed changes to target repository')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)