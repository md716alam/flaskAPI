from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

store = [
    {
        "name":"My Store",
        "items":[
            {
                "name":"Chair",
                "price":15.99
            }
        ]
    }
]

@app.get("/store")
def get_store():
    print("dscjsdcsdcn")
    return {"store":store}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data['name'],"items":[]}
    store.append(new_store)
    return new_store , 201


# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    return "Welcome to the Flask app with Redis!"

@app.route('/set_cache', methods=['POST'])
def set_cache():
    """Set key-value pair in Redis."""
    data = request.json
    key = data.get("key")
    value = data.get("value")

    if not key or not value:
        return jsonify({"error": "Key and Value are required"}), 400
    
    redis_client.set(key, value, ex=60)  # Expiry time: 60 seconds
    return jsonify({"message": "Data cached successfully"})


@app.route('/get_cache/<key>', methods=['GET'])
def get_cache(key):
    """Retrieve value from Redis."""
    value = redis_client.get(key)
    if value is None:
        return jsonify({"message": "Cache miss"}), 404
    return jsonify({"key": key, "value": value})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
