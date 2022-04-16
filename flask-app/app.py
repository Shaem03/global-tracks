from flask import Flask, request, jsonify
from Tracks import Tracks

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Welcome!"


@app.route('/track/<track_id>', methods=['GET'])
def get_track(track_id):
    tracks = Tracks()
    track_data = tracks.fetch(track_id=track_id)

    if track_data:
        response = jsonify(track_data), 200
    else:
        response = jsonify(message="Track not found"), 200

    return response


@app.route('/track', methods=['POST'])
def save():
    track_resource = request.json
    if track_resource:
        tracks = Tracks()
        saved_track = tracks.save(track_resource=track_resource)
        response = jsonify(saved_track), 201
    else:
        response = jsonify(message="Resource is Empty"), 400

    return response


@app.route('/track/recent', methods=['GET'])
def recent():
    tracks = Tracks()
    latest = tracks.recent()
    response = jsonify(latest), 200

    return response


@app.route('/track/filter/<name>', methods=['GET'])
def filter_by_name(name):
    tracks = Tracks()
    filtered_tracks = tracks.filter_by_name(name=name)
    response = jsonify(filtered_tracks), 200

    return response


@app.route('/artists', methods=['GET'])
def artists():
    tracks = Tracks()
    all_artists = tracks.artists()
    response = jsonify(all_artists), 200
    return response


if __name__ == '__main__':
    app.run(port=5000)
