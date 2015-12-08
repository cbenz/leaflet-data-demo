var positionsUrl = 'http://localhost:5000/map/dummy_positions.csv';

function parseJSON(response) {
  return response.json();
}

function fetchPositions(url) {
  return fetch(positionsUrl).then(parseJSON).then(function(data) {
    return data.data;
  });
}

function renderTrips(map, id, latlngs) {
  var polyline = L.polyline(latlngs, {color: 'blue'});
  var animatedMarker = L.animatedMarker(polyline.getLatLngs());

  map.addLayer(animatedMarker);
  polyline.addTo(map);
  var popup = L.popup().setContent('<p>Trip ID = ' + id + '</p>');
  polyline.bindPopup(popup);
}

function getLatLngs(positions) {
  return positions.map(function(position) {
    return [position.latitude, position.longitude];
  });
}


// Initialize map.

var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osmTileLayer = new L.TileLayer(osmUrl, {minZoom: 0, maxZoom: 18, attribution: osmAttrib});
var map = L.map('map');
map.addLayer(osmTileLayer);

fetchPositions(positionsUrl).then(function(positionsById) {
  var ids = Object.keys(positionsById);
  var all_latlngs = [];
  for (id in ids) {
    var positions = positionsById[id];
    var latlngs = getLatLngs(positions);
    renderTrips(map, id, latlngs);
    var all_latlngs = all_latlngs.concat(latlngs);
  }
  var bounds = L.latLngBounds(all_latlngs)
  map.fitBounds(bounds);
})
