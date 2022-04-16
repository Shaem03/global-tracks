import os
import json
from datetime import datetime


class Tracks:

    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        # load all data from tracks.json on initialisation
        with open(f'{self.dir_path}/tracks/tracks.json') as all_tracks_data:
            self.all_tracks = json.load(all_tracks_data)

    def fetch(self, track_id):
        # find single track with id
        track_data = next((item for item in self.all_tracks if item["id"] == track_id), None)
        return track_data

    def save(self, track_resource):
        # if no last_play time is added by default will take the current datetime
        if "last_play" not in track_resource:
            date_time = datetime.now()
            track_resource["last_play"] = date_time.strftime("%Y-%m-%d %H:%M:%S")

        # open json file in read and write mode for modifying the data
        with open(f'{self.dir_path}/tracks/tracks.json', 'r+') as tracks_file:
            data = json.load(tracks_file)
            track_resource["id"] = str(int(data[-1]["id"]) + 1)
            data.append(track_resource)
            tracks_file.seek(0)
            # new track resource will be added to the json file
            json.dump(data, tracks_file)

        return track_resource

    def recent(self):
        # sort the tracks based on recently played
        self.all_tracks.sort(key=lambda item: item['last_play'], reverse=True)

        # fetching top 100 from the list of sorted tracks
        latest_played_tracks = self.all_tracks[:100]

        return latest_played_tracks

    def filter_by_name(self, name):
        # find the track tile starts with the name
        # both the title and name parameter are converted to lower case while searching
        filtered_tracks = [track for track in self.all_tracks if track['title'].lower().startswith(name.lower())]
        return filtered_tracks

    def artists(self):
        self.all_tracks.sort(key=lambda item: item['last_play'], reverse=True)

        # finding artists and no of tracks corresponding to them
        artists_data = {}
        for tracks in self.all_tracks:
            if tracks['artist'] in artists_data:
                artists_data[tracks['artist']] += 1
            else:
                artists_data[tracks['artist']] = 1

        # artists count and name are iterated to get last played and track title
        artist_list = []
        for artist_name, no_of_tracks in artists_data.items():
            recent_play_track = next(item for item in self.all_tracks if item["artist"] == artist_name)
            artist = {
                "name": artist_name,
                "recent_played_track": recent_play_track["title"],
                "last_played_on": recent_play_track["last_play"],
                "no_of_tracks": no_of_tracks
            }
            artist_list.append(artist)

        return artist_list
