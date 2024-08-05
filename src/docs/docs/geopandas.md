
# GeoPandas

## Installation
```bash
pip install geopandas
```

## Basic Usage

### Importing GeoPandas
```python
import geopandas as gpd
```

### Reading Spatial Data
```python
# Read a shapefile
gdf = gpd.read_file('path_to_shapefile.shp')

# Read a GeoJSON file
gdf = gpd.read_file('path_to_geojson.geojson')
```

### Viewing Data
```python
# Display the first few rows
print(gdf.head())

# Display basic information
print(gdf.info())

# Display the coordinate reference system
print(gdf.crs)
```

## Geometric Operations

### Accessing Geometry
```python
# Access the geometry column
geometry = gdf.geometry

# Get the centroid of geometries
centroids = gdf.centroid

# Get the bounds of geometries
bounds = gdf.bounds
```

### Creating Geometries
```python
from shapely.geometry import Point, LineString, Polygon

# Create a point
point = Point(x, y)

# Create a line
line = LineString([(x1, y1), (x2, y2), (x3, y3)])

# Create a polygon
polygon = Polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])
```

### Spatial Operations
```python
# Buffer geometries
buffered = gdf.buffer(distance)

# Union of geometries
union = gdf.unary_union

# Intersection of geometries
intersection = gdf.intersection(other)

# Difference of geometries
difference = gdf.difference(other)
```

## Spatial Relationships
```python
# Check if geometries intersect
intersects = gdf.intersects(other)

# Check if geometries are within another geometry
within = gdf.within(other)

# Check if geometries contain another geometry
contains = gdf.contains(other)
```

## Coordinate Reference Systems (CRS)
```python
# Set the CRS
gdf = gdf.set_crs('EPSG:4326')

# Reproject to another CRS
gdf = gdf.to_crs('EPSG:3857')
```

## Plotting

### Basic Plotting
```python
# Plot the geodataframe
gdf.plot()
```

### Plotting with Matplotlib
```python
import matplotlib.pyplot as plt

# Create a plot with specific size
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the geodataframe
gdf.plot(ax=ax, color='blue', edgecolor='black')

# Show the plot
plt.show()
```

## Example

### Complete Example
```python
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

# Create a GeoDataFrame from scratch
data = {'Name': ['Location1', 'Location2'],
        'Coordinates': [Point(1, 1), Point(2, 2)]}
gdf = gpd.GeoDataFrame(data, geometry='Coordinates')

# Set the coordinate reference system
gdf = gdf.set_crs('EPSG:4326')

# Print information about the GeoDataFrame
print(gdf.info())

# Plot the GeoDataFrame
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, color='blue', edgecolor='black')
plt.show()
```

For more details, refer to the [GeoPandas documentation](https://geopandas.org/).
