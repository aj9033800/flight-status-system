from flask import Flask, jsonify
from flight_service import get_flight_status

app = Flask(__name__)

@app.route('/api/flight/status')
def flight_status():
    status = get_flight_status()
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)
