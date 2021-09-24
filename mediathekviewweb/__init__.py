import websocket
import requests
import json


def query_mediathekview(
    max_hits=20,
    offset=0,
    min_length=None,
    max_length=None,
    query=None,
    stations=None,
    topics=None,
    titles=None,
    descriptions=None,
):

    token = "Nm1StTN"

    session_id = _gets_session_id(token)

    requests.post(
        f"https://mediathekviewweb.de/socket.io/?EIO=4&transport=polling&={token}&sid={session_id}",
        data="40",
    )

    requests.get(
        f"https://mediathekviewweb.de/socket.io/?EIO=4&transport=polling&={token}&sid={session_id}"
    )

    ws_connection = websocket.create_connection(
        f"wss://mediathekviewweb.de/socket.io/?EIO=4&transport=websocket&sid={session_id}"
    )
    _probe(ws_connection)
    _probe(ws_connection)
    ws_connection.send("5")

    query_data = _create_query_data(
        max_hits,
        offset,
        min_length,
        max_length,
        query,
        stations,
        topics,
        titles,
        descriptions,
    )
    ws_connection.send(f"420{json.dumps(query_data)}")
    while True:
        resp = ws_connection.recv()
        if resp:
            break
    return json.loads(resp[resp.index("[") :])


def _create_query_data(
    max_hits=20,
    offset=0,
    min_length=None,
    max_length=None,
    query=None,
    stations=None,
    topics=None,
    titles=None,
    descriptions=None,
):
    queries = []
    if query:
        queries.append(
            {
                "fields": ["topic", "title"],
                "query": query,
            }
        )

    for station in stations or []:
        queries.append(
            {
                "fields": ["channel"],
                "query": station.lower(),
            },
        )
    for topic in topics or []:
        queries.append(
            {
                "fields": ["topic"],
                "query": topic.lower(),
            },
        )

    for title in titles or []:
        queries.append(
            {
                "fields": ["title"],
                "query": title.lower(),
            },
        )

    for description in descriptions or []:
        queries.append(
            {
                "fields": ["description"],
                "query": description.lower(),
            },
        )

    query_control = {
        "queries": queries,
        "sortBy": "timestamp",
        "sortOrder": "desc",
        "size": max_hits,
        "offset": offset,
    }
    if min_length:
        query_control["duration_min"] = min_length
    if max_length:
        query_control["duration_max"] = max_length

    return [
        "queryEntries",
        query_control,
    ]


def _gets_session_id(token):
    r = requests.get(
        f"https://mediathekviewweb.de/socket.io/?EIO=4&transport=polling&={token}"
    )

    # remove non json part from response
    r_text = r.text
    sid = json.loads(r_text[r_text.index("{") :])["sid"]

    return sid


def _probe(ws_connection):
    ws_connection.send("2probe")
    while True:
        resp = ws_connection.recv()
        if resp == "3probe":
            break
