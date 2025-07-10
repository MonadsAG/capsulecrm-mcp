import httpx
from fastapi import HTTPException
from .utils import request
from .models import Milestone

def list_milestones(page: int = 1, per_page: int = 50) -> list[Milestone]:
    data = request("GET", "/milestones", params={"page": page, "perPage": per_page})
    return [Milestone(**milestone) for milestone in data.get("milestones", [])] 