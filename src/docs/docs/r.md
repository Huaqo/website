
# R

## Awesome links

- [Download and install ->](https://cran.uni-muenster.de/bin/macosx/)
- Libraries:
    - [orfeo_toolbox](../geodev/orfeo_toolbox.md)
    - [random_forest](../geodev/random_forest.md)
    - [rstoolbox](../geodev/rstoolbox.md)
    - [terra](../geodev/terra.md)

## CLI

Enter R mode with:

```bash
R
```

Run scripts:

```r
Rscript script.R
```

## Dependency management

List all installed:

```r
installed.packages()
```

Install:

```r
install.packages(c("ggplot2", "dplyr", "tidyr"))
```

## Basic Syntax

### Variables

```r
# Assigning a value to a variable
x <- 10
y <- "Hello, World!"

# Printing a variable
print(x)
print(y)
```

### Data Types

```r
# Numeric
num <- 42

# Integer
int <- as.integer(42)

# Character
char <- "Hello"

# Logical
bool <- TRUE

# Vector
vec <- c(1, 2, 3, 4, 5)

# List
lst <- list(1, "a", TRUE, 1.23)

# Matrix
mat <- matrix(1:9, nrow=3, ncol=3)

# Data Frame
df <- data.frame(
  ID = c(1, 2, 3),
  Name = c("Alice", "Bob", "Charlie"),
  Age = c(25, 30, 35)
)
```

### Operators

```r
# Arithmetic Operators
a <- 10
b <- 5
sum <- a + b
diff <- a - b
prod <- a * b
quot <- a / b
mod <- a %% b

# Relational Operators
gt <- a > b
lt <- a < b
eq <- a == b

# Logical Operators
and <- TRUE & FALSE
or <- TRUE | FALSE
not <- !TRUE
```

## Control Structures

### Conditional Statements

```r
# If-Else Statement
if (x > 0) {
  print("Positive")
} else if (x < 0) {
  print("Negative")
} else {
  print("Zero")
}
```

### Loops

```r
# For Loop
for (i in 1:5) {
  print(i)
}

# While Loop
count <- 1
while (count <= 5) {
  print(count)
  count <- count + 1
}

# Repeat Loop
repeat {
  print(count)
  count <- count + 1
  if (count > 5) {
    break
  }
}
```

## Functions

### Defining and Calling Functions

```r
# Defining a Function
my_function <- function(a, b) {
  return(a + b)
}

# Calling a Function
result <- my_function(10, 5)
print(result)
```

## Apply Functions

### Using apply, lapply, sapply

```r
# apply
mat <- matrix(1:9, nrow=3, ncol=3)
apply(mat, 1, sum)  # Sum of each row

# lapply
lst <- list(a = 1:5, b = 6:10)
lapply(lst, sum)

# sapply
sapply(lst, sum)
```

## Data Manipulation

### Using dplyr

```r
# Installing and loading dplyr
install.packages("dplyr")
library(dplyr)

# Data Frame
df <- data.frame(
  ID = c(1, 2, 3),
  Name = c("Alice", "Bob", "Charlie"),
  Age = c(25, 30, 35)
)

# Selecting Columns
df %>% select(Name, Age)

# Filtering Rows
df %>% filter(Age > 25)

# Mutating (Adding) Columns
df %>% mutate(Age_in_10_Years = Age + 10)

# Summarizing Data
df %>% summarise(Mean_Age = mean(Age))

# Grouping Data
df %>% group_by(Name) %>% summarise(Mean_Age = mean(Age))
```

## Plotting

### Using ggplot2

```r
# Installing and loading ggplot2
install.packages("ggplot2")
library(ggplot2)

# Basic Plot
ggplot(data = df, aes(x = Name, y = Age)) +
  geom_point()

# Line Plot
ggplot(data = df, aes(x = Name, y = Age, group = 1)) +
  geom_line()

# Bar Plot
ggplot(data = df, aes(x = Name, y = Age)) +
  geom_bar(stat = "identity")
```

### Saving a Plots to PNG

To save a plot as a PNG file in R, you can use the png() function to open a PNG graphics device, and dev.off() to close the device after plotting. Below is a brief example:

```r
# Open a PNG device
png("plot_output.png", width=800, height=600)

# Generate the plot
plot(data.df$wavelength, 
     mean, 
     xlab="Wellenlaenge (nm)", ylab="Reflexion (%)", 
     type="l", col=col1, lwd=3, 
     ylim= c(0,1), xlim=c(400,1050),
     main=paste("Baum ", baum.id, ", Provenienz ", prov, sep=""))
lines(data.df$wavelength, unlist(data.df[white]), type="l", col=col2, lwd=3)

# Add a legend
legend("bottomright", legend=c(paste("Baum ", baum.id, ", Provenienz ", prov, sep=""), "Referenz"),
       text.col=c(col1, col2), pch=c("-"), col=c(col1, col2), lwd=3)

# Close the PNG device
dev.off()
```

## Reading and Writing Data

### CSV Files

```r
# Reading a CSV file
df <- read.csv("data.csv")

# Writing to a CSV file
write.csv(df, "output.csv", row.names = FALSE)
```

### Excel Files

```r
# Installing and loading readxl
install.packages("readxl")
library(readxl)

# Reading an Excel file
df <- read_excel("data.xlsx")

# Installing and loading writexl
install.packages("writexl")
library(writexl)

# Writing to an Excel file
write_xlsx(df, "output.xlsx")
```

## Miscellaneous

### Getting Help

```r
# Help on a function
help(mean)
?mean

# Search for a topic
help.search("mean")
```

### Session Management

```r
# List objects in the environment
ls()

# Remove an object
rm(x)

# Clear the workspace
rm(list = ls())
```
