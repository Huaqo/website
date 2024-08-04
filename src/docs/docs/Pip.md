
# Pip

## Installing Packages

```bash
# Install the latest version of a package
pip install package_name

# Install a specific version of a package
pip install package_name==1.0.0

# Install the latest version of a package within a range
pip install 'package_name>=1.0.0,<2.0.0'

# Install packages from a requirements file
pip install -r requirements.txt

# Install a package from a URL or local path
pip install https://example.com/package.tar.gz
pip install ./package_directory
pip install ./package_name.whl

# Install a package for a specific Python version
pip install --python /path/to/python package_name
```

## Upgrading Packages

```bash
# Upgrade a package to the latest version
pip install --upgrade package_name

# Upgrade all packages in a requirements file
pip install --upgrade -r requirements.txt
```

## Uninstalling Packages

```bash
# Uninstall a package
pip uninstall package_name

# Uninstall multiple packages
pip uninstall package_name1 package_name2

# Uninstall all packages in a requirements file
pip uninstall -r requirements.txt
```

## Listing Packages

```bash
# List installed packages
pip list

# List outdated packages
pip list --outdated

# List installed packages in a specific format
pip list --format=columns
pip list --format=freeze
pip list --format=json
```

## Package Information

```bash
# Show information about a package
pip show package_name

# Show the dependencies of a package
pip show --requires package_name
```

## Searching Packages

```bash
# Search for packages
pip search keyword

# Search for packages with specific options
pip search --index https://pypi.org/simple keyword
```

## Freezing and Unfreezing

```bash
# Freeze installed packages to a requirements file
pip freeze > requirements.txt

# Install packages from a frozen requirements file
pip install -r requirements.txt
```

## Configuring pip

```bash
# Set a default index URL
pip config set global.index-url https://pypi.org/simple

# Set a default trusted host
pip config set global.trusted-host pypi.org

# List all configurations
pip config list

# Remove a configuration
pip config unset global.index-url
```
