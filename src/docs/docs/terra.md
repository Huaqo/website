
# Terra

## Awesome links

- [R](../languages/r.md)
- [Documentation ->](https://rspatial.github.io/terra/)

## Installing and Loading the terra Package

```r
# Install the terra package
install.packages("terra")

# Load the terra package
library(terra)
```

## Working with Rasters

### Reading Raster Data

```r
# Read a raster file
r <- rast("path/to/raster/file.tif")

# Print raster information
print(r)
```

### Creating Raster Data

```r
# Create an empty raster with specific dimensions
r <- rast(nrows=100, ncols=100, xmin=0, xmax=10, ymin=0, ymax=10)

# Assign values to the raster
values(r) <- runif(ncell(r))
```

### Writing Raster Data

```r
# Write a raster to a file
writeRaster(r, "output_raster.tif", overwrite=TRUE)
```

## Raster Calculations

### Basic Calculations

```r
# Arithmetic operations
r1 <- rast("raster1.tif")
r2 <- rast("raster2.tif")

r_sum <- r1 + r2
r_diff <- r1 - r2
r_prod <- r1 * r2
r_div <- r1 / r2
```

### Cell Statistics

```r
# Summary statistics
mean_value <- global(r, "mean")
max_value <- global(r, "max")
min_value <- global(r, "min")

# Cell-based statistics
cell_mean <- app(r, mean)
cell_sum <- app(r, sum)
```

### Zonal Statistics

```r
# Zonal statistics
zones <- rast("zones.tif")
zonal_mean <- zonal(r, zones, fun="mean")
```

## Vector Data

### Reading Vector Data

```r
# Read a vector file
v <- vect("path/to/vector/file.shp")

# Print vector information
print(v)
```

### Creating Vector Data

```r
# Create a point vector
points <- vect(matrix(c(1, 2, 3, 4, 5, 6), ncol=2), type="points")

# Create a line vector
lines <- vect(matrix(c(1, 2, 3, 4, 5, 6), ncol=2), type="lines")

# Create a polygon vector
polygons <- vect(matrix(c(1, 2, 3, 4, 5, 6), ncol=2), type="polygons")
```

### Writing Vector Data

```r
# Write a vector to a file
writeVector(v, "output_vector.shp", overwrite=TRUE)
```

## Raster-Vector Interactions

### Extracting Raster Values

```r
# Extract raster values at vector locations
values <- extract(r, v)
```

### Rasterizing Vectors

```r
# Rasterize a vector
r <- rasterize(v, r, field="attribute_name")
```

### Vectorizing Rasters

```r
# Convert raster to vector
v <- as.polygons(r)
```

## Spatial Operations

### Reprojecting Data

```r
# Reproject a raster
r_proj <- project(r, "EPSG:4326")

# Reproject a vector
v_proj <- project(v, "EPSG:4326")
```

### Resampling Rasters

```r
# Resample a raster
r_resample <- resample(r, r, method="bilinear")
```

### Aggregating Rasters

```r
# Aggregate a raster
r_agg <- aggregate(r, fact=2, fun="mean")
```

### Masking Rasters

```r
# Mask a raster with another raster or vector
r_masked <- mask(r, mask_layer)
```

### Cropping Rasters

```r
# Crop a raster
r_cropped <- crop(r, extent(0, 5, 0, 5))
```

## Visualization

### Plotting Rasters

```r
# Plot a raster
plot(r)
```

### Plotting Vectors

```r
# Plot a vector
plot(v)
```

### Overlaying Rasters and Vectors

```r
# Overlay a vector on a raster plot
plot(r)
plot(v, add=TRUE)
```
