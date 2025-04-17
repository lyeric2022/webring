from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI(title="Webring API")

# Data models
class Site(BaseModel):
    id: int
    name: str  # This will be used as the GitHub username
    url: str
    description: Optional[str] = None
    owner: Optional[str] = None
    joinedDate: Optional[str] = None

class Webring(BaseModel):
    name: str
    description: str
    sites: List[Site]
    lastUpdated: str

# Load data function
def load_webring_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            return Webring(**data)
    except Exception as e:
        print(f"Error loading webring data: {e}")
        return None

# Load initial data
webring = load_webring_data()

@app.get("/", response_model=Webring)
def get_webring():
    """Get all webring information"""
    return webring

@app.get("/sites")
def get_all_sites():
    """Get all sites in the webring"""
    return {"sites": webring.sites}

@app.get("/neighbors/{github_name}")
def get_neighbors(github_name: str):
    """Get the left and right neighbors for a site by GitHub name"""
    # Find the site in the webring by name
    site_index = next((i for i, site in enumerate(webring.sites) if site.name.lower() == github_name.lower()), None)
    
    if site_index is None:
        raise HTTPException(status_code=404, detail=f"Site with GitHub name '{github_name}' not found in webring")
    
    # Calculate left (previous) and right (next) indices
    left_index = (site_index - 1) % len(webring.sites)
    right_index = (site_index + 1) % len(webring.sites)
    
    # Return the neighbors with just name and url
    return {
        "current": {
            "name": webring.sites[site_index].name,
            "url": webring.sites[site_index].url
        },
        "left": {
            "name": webring.sites[left_index].name,
            "url": webring.sites[left_index].url
        },
        "right": {
            "name": webring.sites[right_index].name,
            "url": webring.sites[right_index].url
        }
    }

@app.get("/site/{github_name}")
def get_site(github_name: str):
    """Get a specific site by GitHub name"""
    site = next((site for site in webring.sites if site.name.lower() == github_name.lower()), None)
    if site is None:
        raise HTTPException(status_code=404, detail=f"Site with GitHub name '{github_name}' not found")
    return site