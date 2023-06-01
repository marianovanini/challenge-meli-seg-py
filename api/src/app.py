from flask import Flask, request
import csv
import json
from datetime import date

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_data():

    sys_info = request.get_json()

    ip = request.remote_addr

    today = date.today().strftime('%Y-%m-%d')
    csv_filename = f'{ip}_{today}.csv'
    json_filename = f'{ip}_{today}.json'

    # Guardo la información en el archivo CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in sys_info.items():
            writer.writerow([key, value])

    # Guardo la información en el archivo JSON
    with open(json_filename, 'w') as jsonfile:
        json.dump(sys_info, jsonfile)

    return 'Data received and saved'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
