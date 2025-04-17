# Webring API

A simple API for serving and navigating through a webring of personal websites.

## Setup

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Get all webring information
- `GET /sites` - List all sites in the webring
- `GET /neighbors/{github_name}` - Get left and right neighbors for navigation
- `GET /site/{github_name}` - Get details for a specific site

## Example

```bash
# Get navigation links for "Retro Web"
curl http://localhost:8000/neighbors/Retro%20Web
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