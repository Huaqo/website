
[![Netlify Status](https://api.netlify.com/api/v1/badges/e247c197-a620-489c-a5c8-4d7c55c5ec06/deploy-status)](https://app.netlify.com/sites/huaqo/deploys)

# joaquingottlebe.com

This is my personal website. It's built with my custom static site generator.

# Build

```bash
python3 build.py && (cd src/docs && mkdocs build && cd -)
```

# Serve docs

```bash
(cd src/docs && mkdocs serve && cd -)
```