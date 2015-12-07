import csv
import os

from flask import Flask, jsonify
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)
app.debug = True

script_dir = os.path.realpath(os.path.dirname(__file__))


def csv_row_to_position(csv_row):
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
        rows = [
            csv_row_to_position(row)
            for row in reader
            ]
    # print request.args
    positions_by_id = {}
    for row in rows:
        positions_by_id.setdefault(row['id'], []).append(row)
    return jsonify({'data': positions_by_id})


if __name__ == "__main__":
    app.run()
