# mediathekviewweb_cli

Examples:

`mediathekviewweb_cli --title Tatort --station ARD | jq` returns

```json
[
  {
    "channel": "ARD",
    "topic": "Tatort",
    "title": "Tatort: Die Liebe, ein seltsames Spiel - Audiodeskription",
    "description": "Verena Schneider wird tot aufgefunden, der Verdacht fällt auf ihren Lebensgefährten Thomas Jacobi. Um ihn entdecken Batic und Leitmayr ein kompliziertes Geflecht von Liebesbeziehungen zu vielen Frauen, die offenbar nichts voneinander wussten.",
    "timestamp": 1632340800,
    "duration": 5393,
    "size": 905969664,
    "url_website": "https://www.ardmediathek.de/video/Y3JpZDovL3N3ci5kZS9hZXgvbzE1MzM3MzQ",
    "url_subtitle": "",
    "url_video": "https://pdodswr-a.akamaihd.net/swrfernsehen/tatort/1533734.l.mp4",
    "url_video_low": "https://pdodswr-a.akamaihd.net/swrfernsehen/tatort/1533734.ml.mp4",
    "url_video_hd": "https://pdodswr-a.akamaihd.net/swrfernsehen/tatort/1533734.xxl.mp4",
    "filmlisteTimestamp": "1632366960",
    "id": "eidpul2jdyBaEqF7d9Ac22+1vl2cn/NK0zT1gMqAEp4="
  },
...
```

`mediathekviewweb_cli --topic wilsberg --title Wahl | jq` returns

```json
[
  {
    "channel": "ZDF",
    "topic": "Wilsberg",
    "title": "Miss-Wahl",
    "description": "Bei einem Schönheitswettbewerb soll Wilsberg auf viele hübsche Mädchen aufpassen. Irgendjemand ist hinter einem der Models her und führt Böses im Schilde.",
    "timestamp": 1447879500,
    "duration": 5287,
    "size": 1601175552,
    "url_website": "https://www.zdf.de/serien/wilsberg/miss-wahl-102.html",
    "url_subtitle": "https://utstreaming.zdf.de/mtt/zdf/17/02/170201_miss_wahl_wil/14/F0106084_hoh_deu_Wilsberg_Miss_Wahl_120610.xml",
    "url_video": "https://rodlzdf-a.akamaihd.net/none/zdf/17/02/170201_miss_wahl_wil/14/170201_miss_wahl_wil_2328k_p35v13.mp4",
    "url_video_low": "https://rodlzdf-a.akamaihd.net/none/zdf/17/02/170201_miss_wahl_wil/14/170201_miss_wahl_wil_476k_p9v13.mp4",
    "url_video_hd": "https://rodlzdf-a.akamaihd.net/none/zdf/17/02/170201_miss_wahl_wil/14/170201_miss_wahl_wil_3328k_p36v13.mp4",
    "filmlisteTimestamp": "1628738160",
    "id": "3Ur1znPNTn84Q+MmBxuC+dt57sijKMvkpppnX24mDBo="
  }
]

```
