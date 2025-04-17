# Webring API

A simple API for serving and navigating through a webring of personal websites.

## Live Demo

The API is deployed and available at:
[https://physical-larine-lyeric2022-ae24427c.koyeb.app/](https://physical-larine-lyeric2022-ae24427c.koyeb.app/)

## Setup

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server locally
uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Get all webring information
- `GET /sites` - List all sites in the webring
- `GET /neighbors/{github_name}` - Get left and right neighbors for navigation
- `GET /site/{github_name}` - Get details for a specific site

## Example

```bash
# Get navigation links using the deployed API
curl https://physical-larine-lyeric2022-ae24427c.koyeb.app/neighbors/lyeric2022

# Or when testing locally
curl http://localhost:8000/neighbors/lyeric2022
```

## Contributing

To add your site to the webring:

1. Fork this repository
2. Edit `data.json` to add your site
3. Submit a pull request

## Data Format

Sites in `data.json` require:

- `id`: Unique number
- `name`: Your GitHub username/site name
- `url`: Your website URL