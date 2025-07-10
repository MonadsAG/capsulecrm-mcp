import os
import httpx
from fastapi import HTTPException
from typing import Optional

CAPSULECRM_ACCESS_TOKEN = os.getenv("CAPSULECRM_ACCESS_TOKEN")
if not CAPSULECRM_ACCESS_TOKEN:
    raise RuntimeError("CAPSULECRM_ACCESS_TOKEN environment variable not set")

BASE_URL = "https://api.capsulecrm.com/api/v2"

def get_headers():
    return {
        "Authorization": f"Bearer {CAPSULECRM_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

def request(method, endpoint, *, params=None, json=None):
    url = f"{BASE_URL}{endpoint}"
    headers = get_headers()
    with httpx.Client() as client:
        resp = client.request(method, url, headers=headers, params=params, json=json)
        if not resp.status_code // 100 == 2:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()

def filter_entities(entity: str, filter_obj, page: int = 1, per_page: int = 50, embed: Optional[str] = None):
    params = {"page": page, "perPage": per_page}
    if embed:
        params["embed"] = embed
    data = {"filter": filter_obj.dict(exclude_none=True)}
    endpoint = f"/{entity}/filters/results"
    return request("POST", endpoint, params=params, json=data) 