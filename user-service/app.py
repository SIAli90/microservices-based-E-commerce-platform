from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["user1", "user2", "user3"]})

if __name__ == '__main__':
    app.run(port=5001)
