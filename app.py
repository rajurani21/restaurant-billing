from flask import Flask, request, render_template, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Place HTML in templates/index.html

@app.route('/save', methods=['POST'])
def save_bill():
    data = request.get_json()
    filename = "bills.csv"

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            data['customer'],
            data['date'],
            '; '.join(f"{item['item']} x{item['qty']} = ₹{item['price']}" for item in data['items']),
            data['total']
        ])
    return jsonify({"status": "success", "message": "Bill saved successfully."})


if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

