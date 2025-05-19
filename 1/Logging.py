from flask import Flask, request

app = Flask(__name__)
log_store = {}


@app.route('/log', methods=['POST'])
def store_message():
    data = request.json
    if data["id"] in log_store:
        return {"status": "Duplicate ignored"}

    log_store[data["id"]] = data["msg"]
    print(f"Received message: {data['msg']}")
    return {"status": "Logged"}


@app.route('/log', methods=['GET'])
def get_logs():
    return {"logs": list(log_store.values())}, 200


if __name__ == '__main__':
    app.run(port=8001)
