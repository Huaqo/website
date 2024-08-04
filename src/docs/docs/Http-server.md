
# http-server

## Installation

```bash
# Install http-server globally  brew install http-server
```

## Basic Usage

```bash
# Start a server in the current directory
http-server

# Start a server in a specific directory
http-server /path/to/directory

# Specify the port (default is 8080)
http-server -p 8080

# Specify the host (default is 0.0.0.0)
http-server -a 127.0.0.1

# Specify the default file (default is index.html)
http-server -d false -c-1

# Enable gzip compression
http-server --gzip

# Enable Brotli compression
http-server --brotli

# Specify cache time (in seconds)
http-server -c 3600

# Show help
http-server -h
```

## Advanced Usage

```bash
# Run server as a background service
http-server &

# Serve over HTTPS
http-server -S -C /path/to/cert.pem -K /path/to/key.pem

# Serve with CORS headers
http-server --cors

# Proxy requests
http-server --proxy http://localhost:8080?

# Disable directory listings
http-server --no-dotfiles

# Disable logging
http-server -s
```

## Example

```bash
# Start a server on port 8000 with gzip compression and default index.html
http-server -p 8000 --gzip -c-1

# Start a server in a specific directory on port 3000 with CORS enabled
http-server /path/to/directory -p 3000 --cors

# Start a secure server on port 443
http-server -p 443 -S -C /path/to/cert.pem -K /path/to/key.pem
```

## Configuration File

You can create a configuration file named `http-server.json` to store your settings:

```json
{
  "port": 8080,
  "host": "127.0.0.1",
  "defaultFile": "index.html",
  "gzip": true,
  "brotli": true,
  "cache": 3600,
  "showDir": true,
  "autoIndex": true,
  "ext": "html",
  "logFn": function (req, res, error) { console.log(`${req.method} ${req.url}`); },
  "proxy": "http://localhost:8080?",
  "cors": true,
  "noDotfiles": false,
  "https": {
    "cert": "/path/to/cert.pem",
    "key": "/path/to/key.pem"
  }
}
```

To use the configuration file:

```bash
http-server -c http-server.json
```

