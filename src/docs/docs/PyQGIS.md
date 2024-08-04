
# PyQGIS

## Getting Started

### Importing QGIS Modules

```python
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
```

### Initializing QGIS Application

```python
from qgis.core import QgsApplication

QgsApplication.setPrefixPath("/path/to/qgis/installation", True)
qgs = QgsApplication([], False)
qgs.initQgis()
```

### Exiting QGIS Application

```python
qgs.exitQgis()
```

## Loading Layers

### Loading a Vector Layer

```python
vector_layer = QgsVectorLayer("/path/to/vector.shp", "layer name", "ogr")
if not vector_layer.isValid():
    print("Layer failed to load!")
```

### Loading a Raster Layer

```python
raster_layer = QgsRasterLayer("/path/to/raster.tif", "layer name")
if not raster_layer.isValid():
    print("Layer failed to load!")
```

### Adding a Layer to the Map

```python
QgsProject.instance().addMapLayer(vector_layer)
QgsProject.instance().addMapLayer(raster_layer)
```

## Layer Operations

### Accessing Layer Fields

```python
fields = vector_layer.fields()
for field in fields:
    print(field.name(), field.typeName())
```

### Iterating Over Features

```python
for feature in vector_layer.getFeatures():
    print(feature.id(), feature.attributes())
```

### Selecting Features by Attribute

```python
expression = QgsExpression("attribute_name = 'value'")
request = QgsFeatureRequest(expression)
features = vector_layer.getFeatures(request)
for feature in features:
    print(feature.id(), feature.attributes())
```

## Geometry Operations

### Creating a Point Geometry

```python
from qgis.core import QgsPointXY, QgsGeometry

point = QgsPointXY(10, 10)
geometry = QgsGeometry.fromPointXY(point)
```

### Creating a Line Geometry

```python
line = [QgsPointXY(10, 10), QgsPointXY(20, 20)]
geometry = QgsGeometry.fromPolylineXY(line)
```

### Creating a Polygon Geometry

```python
polygon = [[QgsPointXY(10, 10), QgsPointXY(20, 20), QgsPointXY(20, 10), QgsPointXY(10, 10)]]
geometry = QgsGeometry.fromPolygonXY(polygon)
```

## Spatial Operations

### Buffer

```python
buffer = geometry.buffer(10, 5)
```

### Intersection

```python
intersection = geometry1.intersection(geometry2)
```

### Difference

```python
difference = geometry1.difference(geometry2)
```

## CRS (Coordinate Reference System)

### Setting a Layer CRS

```python
crs = QgsCoordinateReferenceSystem("EPSG:4326")
vector_layer.setCrs(crs)
```

### Transforming Coordinates

```python
from qgis.core import QgsCoordinateTransform, QgsProject

transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem("EPSG:4326"), QgsCoordinateReferenceSystem("EPSG:3857"), QgsProject.instance())
transformed_point = transform.transform(QgsPointXY(10, 10))
```

## Map Rendering

### Creating a Map Canvas

```python
from qgis.gui import QgsMapCanvas

canvas = QgsMapCanvas()
canvas.setCanvasColor(Qt.white)
canvas.setExtent(vector_layer.extent())
canvas.setLayers([vector_layer])
canvas.show()
```

### Saving Map as Image

```python
from qgis.gui import QgsMapRendererCustomPainterJob

image = QImage(QSize(800, 600), QImage.Format_ARGB32_Premultiplied)
image.fill(Qt.white)

painter = QPainter(image)
renderer = QgsMapRendererCustomPainterJob(canvas.mapSettings(), painter)
renderer.start()
renderer.waitForFinished()
painter.end()

image.save("/path/to/map.png", "png")
```

## Plugins

### Loading a Plugin

```python
from qgis.utils import loadPlugin, startPlugin

loadPlugin("plugin_name")
startPlugin("plugin_name")
```

### Accessing Plugin Methods

```python
plugin_instance = qgis.utils.plugins["plugin_name"]
plugin_instance.method_name()
```
