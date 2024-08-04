
# RStoolbox

## Installing and Loading the RSToolbox Package

```r
# Install the RSToolbox package
install.packages("RSToolbox")

# Load the RSToolbox package
library(RSToolbox)
```

## Reading and Writing Data

### Reading Raster Data

```r
# Read a raster file
raster <- raster("path/to/raster/file.tif")

# Read multiple raster files as a stack
stack <- stack(list.files(pattern="*.tif"))
```

### Writing Raster Data

```r
# Write a raster to a file
writeRaster(raster, "output_raster.tif", overwrite=TRUE)
```

## Preprocessing

### Normalizing Data

```r
# Normalize raster data
normalized <- normalize(raster)
```

### Principal Component Analysis (PCA)

```r
# Perform PCA on raster data
pca_result <- rasterPCA(raster)
```

### Image Enhancement

```r
# Enhance contrast of raster data
enhanced <- stretch(raster, minq=0.02, maxq=0.98)
```

## Classification

### Unsupervised Classification (K-means)

```r
# Perform K-means classification
kmeans_result <- unsuperClass(raster, nSamples=1000, nClasses=5)
```

### Supervised Classification (Random Forest)

```r
# Perform supervised classification using Random Forest
trainingData <- read.csv("path/to/training/data.csv")
rf_model <- superClass(raster, trainData=trainingData, responseCol="class", model="rf")
```

## Accuracy Assessment

### Confusion Matrix

```r
# Create a confusion matrix for classification results
referenceData <- read.csv("path/to/reference/data.csv")
conf_matrix <- validateMap(rf_model$map, valData=referenceData, responseCol="class")
```

### Overall Accuracy

```r
# Calculate overall accuracy
overall_acc <- conf_matrix$overallAccuracy
print(overall_acc)
```

## Change Detection

### Change Detection Using Difference

```r
# Perform change detection using difference
raster1 <- raster("path/to/raster1.tif")
raster2 <- raster("path/to/raster2.tif")
change <- raster2 - raster1
```

### Change Vector Analysis

```r
# Perform change vector analysis
cva_result <- cva(raster1, raster2)
```

## Visualization

### Plotting Rasters

```r
# Plot a single raster layer
plot(raster)

# Plot a raster stack
plot(stack)
```

### Plotting Classification Results

```r
# Plot classification map
plot(rf_model$map)

# Plot classification probability map
plot(rf_model$map$probability)
```

### Plotting PCA Results

```r
# Plot PCA results
plot(pca_result$map)
```

## Advanced Analysis

### Texture Analysis

```r
# Perform texture analysis
texture <- glcm(raster, window=c(3,3), statistics="mean")
```

### Spectral Indices

```r
# Calculate NDVI
ndvi <- spectralIndices(raster, red="band3", nir="band4", index="NDVI")
```

### Anomaly Detection

```r
# Perform anomaly detection
anomalies <- anomalyDetection(raster, method="mad")
```
