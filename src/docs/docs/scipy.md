
# SciPy

## Installation
```bash
pip install scipy
```

## Basic Usage

### Importing SciPy
```python
import scipy as sp
from scipy import stats, linalg, optimize, integrate, signal, fftpack
```

## Common Modules and Functions

### Statistics (`scipy.stats`)

#### Descriptive Statistics
```python
from scipy import stats

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Mean
mean = stats.tmean(data)

# Median
median = stats.tmedian(data)

# Mode
mode = stats.mode(data)

# Standard deviation
std_dev = stats.tstd(data)
```

#### Probability Distributions
```python
# Normal distribution
rv = stats.norm(loc=0, scale=1)
pdf = rv.pdf(0)  # Probability density function
cdf = rv.cdf(0)  # Cumulative distribution function
sample = rv.rvs(size=10)  # Random samples
```

### Linear Algebra (`scipy.linalg`)
```python
from scipy import linalg

# Create a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the determinant
det = linalg.det(A)

# Compute the inverse
inv = linalg.inv(A)

# Solve a linear system of equations
b = np.array([1, 2])
x = linalg.solve(A, b)
```

### Optimization (`scipy.optimize`)

#### Minimization
```python
from scipy import optimize

# Define a function
def f(x):
    return x**2 + 5*np.sin(x)

# Find the minimum
result = optimize.minimize(f, x0=0)
min_x = result.x
min_f = result.fun
```

#### Root Finding
```python
# Define a function
def f(x):
    return x**2 - 5

# Find the root
root = optimize.root(f, x0=2)
root_x = root.x
```

### Integration (`scipy.integrate`)
```python
from scipy import integrate

# Define a function
def f(x):
    return x**2

# Compute the definite integral
result, error = integrate.quad(f, 0, 1)

# Double integral
def f(x, y):
    return x*y

result, error = integrate.dblquad(f, 0, 1, lambda x: 0, lambda x: 1)
```

### Signal Processing (`scipy.signal`)
```python
from scipy import signal

# Create a signal
t = np.linspace(0, 1, 500, endpoint=False)
x = np.cos(2 * np.pi * 7 * t) + signal.square(2 * np.pi * 2 * t)

# Compute the spectrogram
frequencies, times, spectrogram = signal.spectrogram(x)
```

### Fast Fourier Transform (`scipy.fftpack`)
```python
from scipy import fftpack

# Create a signal
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Compute the FFT
yf = fftpack.fft(y)

# Compute the frequencies
xf = fftpack.fftfreq(len(x), x[1] - x[0])
```

## Example

### Complete Example
```python
import numpy as np
import scipy as sp
from scipy import stats, linalg, optimize, integrate, signal, fftpack
import matplotlib.pyplot as plt

# Statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mean = stats.tmean(data)
std_dev = stats.tstd(data)
print(f"Mean: {mean}, Std Dev: {std_dev}")

# Linear Algebra
A = np.array([[1, 2], [3, 4]])
det = linalg.det(A)
inv = linalg.inv(A)
print(f"Determinant: {det}, Inverse:\n{inv}")

# Optimization
def f(x):
    return x**2 + 5*np.sin(x)

result = optimize.minimize(f, x0=0)
print(f"Minimum at x: {result.x}, f(x): {result.fun}")

# Integration
def f(x):
    return x**2

result, error = integrate.quad(f, 0, 1)
print(f"Integral result: {result}, Error: {error}")

# Signal Processing
t = np.linspace(0, 1, 500, endpoint=False)
x = np.cos(2 * np.pi * 7 * t) + signal.square(2 * np.pi * 2 * t)
frequencies, times, spectrogram = signal.spectrogram(x)

plt.pcolormesh(times, frequencies, spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

# Fast Fourier Transform
x = np.linspace(0, 10, 100)
y = np.sin(x)
yf = fftpack.fft(y)
xf = fftpack.fftfreq(len(x), x[1] - x[0])

plt.plot(xf, np.abs(yf))
plt.title('FFT')
plt.show()
```

For more details, refer to the [SciPy documentation](https://docs.scipy.org/doc/scipy/).
