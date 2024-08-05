
# Leaflet

## Installation

### Including Leaflet in HTML
```html
<!-- Include Leaflet CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />

<!-- Include Leaflet JavaScript -->
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
```

## Basic Map Setup

### Creating a Basic Map
```html
<!-- Create a div where the map will be rendered -->
<div id="mapid" style="height: 600px;"></div>

<script>
  // Initialize the map and set its view to a specific location and zoom level
  var mymap = L.map('mapid').setView([latitude, longitude], zoomLevel);

  // Add a tile layer to the map (e.g., OpenStreetMap tiles)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(mymap);
</script>
```

## Adding Markers

### Simple Marker
```javascript
L.marker([latitude, longitude]).addTo(mymap)
  .bindPopup('Marker Popup')
  .openPopup();
```

### Circle Marker
```javascript
L.circle([latitude, longitude], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5,
  radius: 500
}).addTo(mymap).bindPopup('Circle Popup');
```

### Polygon
```javascript
var latlngs = [
  [lat1, lon1],
  [lat2, lon2],
  [lat3, lon3]
];
L.polygon(latlngs, {
  color: 'blue'
}).addTo(mymap).bindPopup('Polygon Popup');
```

## Layers and Controls

### Layer Groups
```javascript
var cities = L.layerGroup();

L.marker([lat1, lon1]).bindPopup('City 1').addTo(cities);
L.marker([lat2, lon2]).bindPopup('City 2').addTo(cities);

cities.addTo(mymap);
```

### Layer Control
```javascript
var baseMaps = {
  "OpenStreetMap": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }),
  "Stamen Watercolor": L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.jpg', {
    attribution: 'Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
  })
};

var overlayMaps = {
  "Cities": cities
};

L.control.layers(baseMaps, overlayMaps).addTo(mymap);
```

## Additional Features

### Adding a GeoJSON Layer
```javascript
var geojsonFeature = {
  "type": "Feature",
  "properties": {
    "name": "Coors Field",
    "amenity": "Baseball Stadium",
    "popupContent": "This is where the Rockies play!"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-104.99404, 39.75621]
  }
};

L.geoJSON(geojsonFeature).addTo(mymap);
```

### Adding a Heatmap
```html
<!-- Include Heatmap.js library -->
<script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>

<script>
  var heat = L.heatLayer([
    [lat1, lon1, intensity1],
    [lat2, lon2, intensity2]
  ], {radius: 25}).addTo(mymap);
</script>
```

### Adding a Scale
```javascript
L.control.scale().addTo(mymap);
```

## Example

### Complete Example
```html
<!DOCTYPE html>
<html>
<head>
  <title>Leaflet Map</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
  <style>
    #mapid { height: 600px; }
  </style>
</head>
<body>
  <div id="mapid"></div>
  <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
  <script>
    var mymap = L.map('mapid').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(mymap);

    L.marker([51.5, -0.09]).addTo(mymap)
      .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
      .openPopup();

    L.circle([51.508, -0.11], {
      color: 'red',
      fillColor: '#f03',
      fillOpacity: 0.5,
      radius: 500
    }).addTo(mymap).bindPopup('I am a circle.');

    var latlngs = [
      [51.509, -0.08],
      [51.503, -0.06],
      [51.51, -0.047]
    ];
    L.polygon(latlngs, {
      color: 'blue'
    }).addTo(mymap).bindPopup('I am a polygon.');

    L.control.scale().addTo(mymap);
  </script>
</body>
</html>
```

For more details, refer to the [Leaflet documentation](https://leafletjs.com/).
