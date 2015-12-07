# leaflet-data-demo
Experimentation around Leaflet and displaying data

## Client-side steps

- use Leaflet hosted version from CDN (http://leafletjs.com/download.html)
- create index.html
- open it with file:///path/to/leaflet-data-demo/src/index.html
- quick start guides: [leaflet](http://leafletjs.com/examples/quick-start.html) and [switch2osm](https://switch2osm.org/using-tiles/getting-started-with-leaflet/)

## Server-side steps

```
cd server
pip install --user -r requirements.txt
python api.py
```

To test:

```
curl http://localhost:5000/
```
