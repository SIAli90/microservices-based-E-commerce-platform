from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": ["order1", "order2", "order3"]})

if __name__ == '__main__':
    app.run(port=5002)
