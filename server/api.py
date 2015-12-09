import csv
import os

from flask import Flask, jsonify
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)
app.debug = True

script_dir = os.path.realpath(os.path.dirname(__file__))


def csv_row_to_json_item(csv_row):
    return {
        'id': int(csv_row['id']),
        'timestamp': int(csv_row['timestamp']),
        'latitude': float(csv_row['latitude']),
        'longitude': float(csv_row['longitude']),
        }


@app.route("/positions.json")
def positions():
    csv_file_path = os.path.join(script_dir, 'dummy_positions.csv')
    with open(csv_file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_rows = list(reader)
    positions_json = [
        csv_row_to_json_item(row)
        for row in csv_rows
        ]
    positions_by_id = {}
    for position_json in positions_json:
        positions_by_id.setdefault(position_json['id'], []).append(position_json)
    return jsonify({'data': positions_by_id})


if __name__ == "__main__":
    app.run()
