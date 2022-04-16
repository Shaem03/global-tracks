# REST API Global Python Task

This is simple application to provide API's to perform simple task for the `tracks.json`

The entire application is contained within the `app.py` and `Tracks.py` file.

`test.py` runs a simple unit test for the API

## Install

    cd flask-app

    pip install -r requirements.txt

## Run the app
    
    cd flask-app

    python app.py
    
###OR
    
    docker-compose up --build   

## Run the tests
    
    cd flask-app

    python test.py

# REST API

The REST API to the created are described below. 

`base_url = http://127.0.0.1:5000`

## Fetch a single track

Fetches single track with track id

### Request

`GET /track/<track_id>`

    curl -i -H 'Accept: application/json' --request GET 'http://127.0.0.1:5000/track/221'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.9.8
    Date: Fri, 15 Apr 2022 15:21:39 GMT
    Content-Type: application/json
    Content-Length: 115

    {
        "artist": "Cheryl Cole",
        "duration": "209",
        "id": "221",
        "last_play": "2017-09-15 07:13:34",
        "title": "Crazy Stupid Love"
    }

## Create a new track

Create new track, id are auto incremented.

Note:

- Key `last_play` is optional
- default value of `last_play` take as current datetime
- format "YYYY-MM-DD HH:MM:SS"

### Request

`POST /track`

    curl -i -H 'Accept: application/json' --request POST 'http://127.0.0.1:5000/track' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "title": "November Rain",
        "artist": "Guns N Roses",
        "duration": "556",
        "last_play": "2018-05-17 13:56:07" // optional
    }'

### Response

    HTTP/1.1 201 CREATED
    Server: Werkzeug/2.1.1 Python/3.9.8
    Date: Fri, 15 Apr 2022 19:37:12 GMT
    Content-Type: application/json
    Content-Length: 113
    
    {
        "artist":"Guns N Roses",
        "duration":"556",
        "id":"7729",
        "last_play":"2022-04-15 23:20:20",
        "title":"November Rain"
    }

## Recent Tracks

Fetch the first 100 most recently played tracks (most recent first).

### Request

`GET /track/recent`

    curl -i -H 'Accept: application/json' --request GET 'http://127.0.0.1:5000/track/recent'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.9.8
    Date: Fri, 15 Apr 2022 17:59:43 GMT
    Content-Type: application/json
    Content-Length: 11568

    [
        {
            "artist": "Guns N Roses",
            "duration": "556",
            "id": "7729",
            "last_play": "2022-04-15 23:20:20",
            "title": "November Rain"
        },
        {
            "artist": "Bob Sinclar / Gary Nesta Pine",
            "duration": "172",
            "id": "394",
            "last_play": "2018-05-17 16:59:11",
            "title": "Love Generation"
        },
        ...
        ...
    ]

## Filter tracks by name

Fetch all tracks containing the name.

### Request

`GET /track/filter/<name>`

    curl -i -H 'Accept: application/json' --request GET 'http://127.0.0.1:5000/track/filter/ghost'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.9.8
    Date: Fri, 15 Apr 2022 19:29:15 GMT
    Content-Type: application/json
    Content-Length: 224

    [
        {
            "artist": "Ella Henderson",
            "duration": "211",
            "id": "205",
            "last_play": "2018-02-26 06:18:17",
            "title": "GHOST"
        },
        {
            "artist": "Ray Parker Junior",
            "duration": "240",
            "id": "283",
            "last_play": "2018-05-16 07:25:43",
            "title": "Ghostbusters"
        }
    ]

## Fetch Artists

Fetch a list of artists. List contains artist total number of tracks and recently played track title and datetime.

### Request

`GET /artists`

    curl -i -H 'Accept: application/json' --request GET 'http://127.0.0.1:5000/artists'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.9.8
    Date: Fri, 15 Apr 2022 19:32:47 GMT
    Content-Type: application/json
    Content-Length: 190076

    [
        {
            "last_played_on": "2022-04-15 23:20:20",
            "name": "Guns N Roses",
            "no_of_tracks": 3,
            "recent_played_track": "November Rain"
        },
        {
            "last_played_on": "2018-05-17 16:59:11",
            "name": "Bob Sinclar / Gary Nesta Pine",
            "no_of_tracks": 1,
            "recent_played_track": "Love Generation"
        }
        ...
        ...
    ]