
# Random Forest

## Awesome links

- [R](../languages/r.md)
- [Documentation ->](https://www.stat.berkeley.edu/~breiman/RandomForests/)

## Installation
```r
install.packages("randomForest")
install.packages("raster")
install.packages("rgdal")
install.packages("sp")
```

## Basic Usage

### Loading the Packages
```r
library(randomForest)
library(raster)
library(rgdal)
library(sp)
```

## Loading and Preprocessing Data

### Load Raster Data
```r
# Load a raster file
raster_data <- stack("path_to_raster_file.tif")
```

### Load Vector Data
```r
# Load a shapefile
vector_data <- readOGR("path_to_shapefile.shp")
```

### Extracting Values for Training
```r
# Ensure the CRS match
vector_data <- spTransform(vector_data, crs(raster_data))

# Extract raster values using shapefile
training_data <- extract(raster_data, vector_data, df = TRUE)
training_data$target <- vector_data$target_column  # Assuming target column in shapefile
```

## Training a Random Forest Model

### Training the Model
```r
# Ensure the target variable is a factor
training_data$target <- as.factor(training_data$target)

# Train the Random Forest model
set.seed(123)
rf_model <- randomForest(target ~ ., data = training_data, ntree = 500, mtry = 3)
```

### Viewing the Model Summary
```r
print(rf_model)
```

## Model Evaluation

### Prediction on Raster Data
```r
# Predict on the entire raster dataset
predicted_raster <- predict(raster_data, rf_model, type = "response")
```

### Save the Predicted Raster
```r
# Save the predicted raster
writeRaster(predicted_raster, "predicted_raster.tif", format = "GTiff", overwrite = TRUE)
```

### Variable Importance
```r
importance(rf_model)
varImpPlot(rf_model)
```

## Example Workflow

### Complete Example
```r
# Load necessary libraries
library(randomForest)
library(raster)
library(rgdal)
library(sp)

# Load the raster dataset
raster_data <- stack("path_to_raster_file.tif")

# Load the shapefile
vector_data <- readOGR("path_to_shapefile.shp")

# Ensure CRS match
vector_data <- spTransform(vector_data, crs(raster_data))

# Extract raster values using shapefile
training_data <- extract(raster_data, vector_data, df = TRUE)
training_data$target <- vector_data$target_column  # Assuming target column in shapefile

# Ensure the target variable is a factor
training_data$target <- as.factor(training_data$target)

# Train the Random Forest model
set.seed(123)
rf_model <- randomForest(target ~ ., data = training_data, ntree = 500, mtry = 3)

# Print the model summary
print(rf_model)

# Predict on the entire raster dataset
predicted_raster <- predict(raster_data, rf_model, type = "response")

# Save the predicted raster
writeRaster(predicted_raster, "predicted_raster.tif", format = "GTiff", overwrite = TRUE)

# Variable importance
importance(rf_model)
varImpPlot(rf_model)
```

For more details, refer to the [randomForest package documentation](https://cran.r-project.org/web/packages/randomForest/randomForest.pdf) and the [raster package documentation](https://cran.r-project.org/web/packages/raster/raster.pdf).
