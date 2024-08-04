
# Geospatial Data Abstraction Library (GDAL)

## Installing and Loading the GDAL Package

### Installing GDAL

Before using GDAL in R, you need to install the GDAL library on your system. The installation process may vary depending on your operating system.

#### macOS

Install GDAL using Homebrew:

```sh
brew install gdal
```

### Installing and Loading the `rgdal` Package in R

```r
# Install the rgdal package
install.packages("rgdal")

# Load the rgdal package
library(rgdal)
```

## Reading and Writing Raster Data

### Reading Raster Data

```r
# Read a raster file
raster <- readGDAL("path/to/raster/file.tif")
print(raster)
```

### Writing Raster Data

```r
# Write a raster to a file
writeGDAL(raster, "output_raster.tif")
```

## Reading and Writing Vector Data

### Reading Vector Data

```r
# Read a shapefile
vector <- readOGR(dsn = "path/to/vector/folder", layer = "shapefile_name")
print(vector)
```

### Writing Vector Data

```r
# Write a shapefile
writeOGR(vector, dsn = "output_folder", layer = "output_shapefile", driver = "ESRI Shapefile")
```

## Coordinate Reference Systems (CRS)

### Checking CRS

```r
# Check the CRS of a raster
crs(raster)

# Check the CRS of a vector
crs(vector)
```

### Setting CRS

```r
# Set the CRS of a raster
crs(raster) <- CRS("+proj=longlat +datum=WGS84")

# Set the CRS of a vector
crs(vector) <- CRS("+proj=longlat +datum=WGS84")
```

### Reprojecting Data

```r
# Reproject a raster
reprojected_raster <- projectRaster(raster, crs = CRS("+proj=utm +zone=33 +datum=WGS84"))

# Reproject a vector
reprojected_vector <- spTransform(vector, CRS("+proj=utm +zone=33 +datum=WGS84"))
```

## Raster Calculations

### Basic Calculations

```r
# Arithmetic operations
r1 <- readGDAL("raster1.tif")
r2 <- readGDAL("raster2.tif")

r_sum <- r1 + r2
r_diff <- r1 - r2
r_prod <- r1 * r2
r_div <- r1 / r2
```

### Cell Statistics

```r
# Summary statistics
mean_value <- cellStats(raster, stat = 'mean')
max_value <- cellStats(raster, stat = 'max')
min_value <- cellStats(raster, stat = 'min')

# Cell-based statistics
cell_mean <- calc(raster, fun = mean)
cell_sum <- calc(raster, fun = sum)
```

### Zonal Statistics

```r
# Zonal statistics
zones <- readGDAL("zones.tif")
zonal_mean <- zonal(raster, zones, fun = "mean")
```

## Spatial Operations

### Resampling Rasters

```r
# Resample a raster
resampled_raster <- resample(raster, raster, method = "bilinear")
```

### Aggregating Rasters

```r
# Aggregate a raster
aggregated_raster <- aggregate(raster, fact = 2, fun = mean)
```

### Masking Rasters

```r
# Mask a raster with another raster or vector
masked_raster <- mask(raster, mask_layer)
```

### Cropping Rasters

```r
# Crop a raster
cropped_raster <- crop(raster, extent(0, 5, 0, 5))
```

## Visualization

### Plotting Rasters

```r
# Plot a raster
plot(raster)
```

### Plotting Vectors

```r
# Plot a vector
plot(vector)
```

### Overlaying Rasters and Vectors

```r
# Overlay a vector on a raster plot
plot(raster)
plot(vector, add = TRUE)
```
