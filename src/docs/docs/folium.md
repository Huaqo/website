
# Folium

## Installation
```bash
pip install folium
```

## Basic Usage

### Importing Folium
```python
import folium
```

### Creating a Basic Map
```python
# Create a map centered at a specific latitude and longitude
mymap = folium.Map(location=[latitude, longitude], zoom_start=10)

# Display the map
mymap.save("mymap.html")
mymap
```

## Map Configuration

### Map Tiles
```python
# Available map tiles: 'OpenStreetMap', 'Stamen Terrain', 'Stamen Toner', 'Stamen Watercolor', 'CartoDB positron', 'CartoDB dark_matter'
mymap = folium.Map(location=[latitude, longitude], tiles='Stamen Terrain', zoom_start=10)
```

### Map Options
```python
# Additional options like max_zoom, min_zoom, zoom_control, etc.
mymap = folium.Map(location=[latitude, longitude], zoom_start=10, max_zoom=18, min_zoom=5, zoom_control=True)
```

## Adding Markers

### Simple Marker
```python
folium.Marker(location=[latitude, longitude], popup='Marker Popup', tooltip='Click for more').add_to(mymap)
```

### Custom Marker Icons
```python
# Using a different icon
folium.Marker(location=[latitude, longitude], icon=folium.Icon(icon='cloud')).add_to(mymap)

# Custom icon colors: 'red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray'
folium.Marker(location=[latitude, longitude], icon=folium.Icon(color='red', icon='info-sign')).add_to(mymap)
```

## Adding Other Map Features

### Circle Marker
```python
folium.CircleMarker(location=[latitude, longitude], radius=50, popup='Circle Popup', color='#3186cc', fill=True, fill_color='#3186cc').add_to(mymap)
```

### Polyline
```python
folium.PolyLine(locations=[[lat1, lon1], [lat2, lon2], [lat3, lon3]], color='blue').add_to(mymap)
```

### Polygon
```python
folium.Polygon(locations=[[lat1, lon1], [lat2, lon2], [lat3, lon3], [lat4, lon4]], color='green', fill=True, fill_color='green').add_to(mymap)
```

## Advanced Features

### Adding a Layer Control
```python
folium.LayerControl().add_to(mymap)
```

### Adding GeoJSON Data
```python
# GeoJSON data can be loaded and added to the map
geojson_data = 'path_to_geojson_file.json'
folium.GeoJson(geojson_data).add_to(mymap)
```

### Adding a Choropleth Map
```python
folium.Choropleth(
    geo_data=geojson_data,
    data=your_data,  # DataFrame or Series with data
    columns=['Column1', 'Column2'],
    key_on='feature.properties.property_name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Your Legend'
).add_to(mymap)
```

### Adding a Heatmap
```python
from folium.plugins import HeatMap

heat_data = [[lat, lon] for lat, lon in zip(df['latitude'], df['longitude'])]
HeatMap(heat_data).add_to(mymap)
```

## Display and Save the Map
```python
# Display the map in a Jupyter Notebook
mymap

# Save the map to an HTML file
mymap.save('mymap.html')
```

## Examples

### Example 1: Simple Map with Marker
```python
import folium

mymap = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.Marker([45.5236, -122.6750], popup='Portland, OR').add_to(mymap)

mymap.save('simple_map.html')
```

### Example 2: Map with Circle Marker and Polyline
```python
import folium

mymap = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.CircleMarker([45.5236, -122.6750], radius=50, popup='The Waterfront', color='#3186cc', fill=True, fill_color='#3186cc').add_to(mymap)
folium.PolyLine(locations=[[45.5236, -122.6750], [45.5289, -122.6800]], color='blue').add_to(mymap)

mymap.save('map_with_circle_and_polyline.html')
```

For more details, refer to the [Folium documentation](https://python-visualization.github.io/folium/).
