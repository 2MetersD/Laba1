import requests
import uuid
from flask import Flask, request

app = Flask(__name__)

LOGGING_SERVICE_URL = "http://localhost:8001/log"
MESSAGES_SERVICE_URL = "http://localhost:8002/message"
MAX_RETRIES = 5

def send_with_retry(payload):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(LOGGING_SERVICE_URL, json=payload, timeout=5)
            if response.status_code == 200:
                return {"status": "Message sent", "id": payload["id"]}
        except requests.exceptions.RequestException:
            print(f"Retry attempt {attempt + 1} failed.")
    return {"status": "Failed to send message"}

@app.route('/send', methods=['POST'])
def send_message():
    msg = request.json.get('msg', '')
    msg_id = str(uuid.uuid4())
    payload = {"id": msg_id, "msg": msg}
    return send_with_retry(payload)

@app.route('/receive', methods=['GET'])
def receive_messages():
    log_response = requests.get(LOGGING_SERVICE_URL).json()
    msg_response = requests.get(MESSAGES_SERVICE_URL).text
    return {"logs": log_response["logs"], "message": msg_response}

if __name__ == '__main__':
    app.run(port=8000)
