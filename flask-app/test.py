import json

try:
    from app import app
    import unittest
except Exception as e:
    print(f"Error while import {e}")


class TestApp(unittest.TestCase):
    track_resource = {
        "title": "November Rain",
        "artist": "Guns N Roses",
        "duration": "333"
    }
    track_id = 87
    name = "good"
    artist_payload_keys = ["last_played_on",
                           "name",
                           "no_of_tracks",
                           "recent_played_track"]

    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status = response.status_code
        self.assertEqual(status, 200)

    def test_get_track(self):
        tester = app.test_client(self)
        response = tester.get(f"/track/{self.track_id}")
        status = response.status_code
        self.assertEqual(status, 200)
        self.assertEqual(int(response.json["id"]), self.track_id)

    def test_save(self):
        tester = app.test_client(self)
        response = tester.post("/track", data=json.dumps(self.track_resource), content_type='application/json')
        status = response.status_code

        self.assertEqual(status, 201)
        self.assertLessEqual(self.track_resource.items(), response.json.items())

    def test_recent_tracks(self):
        tester = app.test_client(self)
        response = tester.get(f"/track/recent")

        status = response.status_code
        self.assertEqual(status, 200)
        self.assertEqual(len(response.json), 100)

    def test_filter_by_name(self):
        tester = app.test_client(self)
        response = tester.get(f"/track/filter/{self.name}")

        status = response.status_code
        self.assertEqual(status, 200)
        self.assertIn(self.name, response.json[0]["title"].lower())

    def test_artists(self):
        tester = app.test_client(self)
        response = tester.get(f"/artists")

        status = response.status_code
        self.assertEqual(status, 200)
        self.assertListEqual(list(response.json[0].keys()), self.artist_payload_keys)


if __name__ == '__main__':
    unittest.main()
