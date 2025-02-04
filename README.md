
[![Netlify Status](https://api.netlify.com/api/v1/badges/5eb69289-6fbf-4224-ba9f-1ae97d939ccd/deploy-status)](https://app.netlify.com/sites/joaquingottlebe/deploys)

# joaquingottlebe.netlify.app

This is my personal website. It's built with my custom static site generator.

# Build

```bash
python3 build.py && (cd src/docs && mkdocs build && cd -)
```

# Serve

```bash
(cd src/docs && mkdocs serve && cd -)
```
