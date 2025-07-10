import os
import sys
import httpx
import logging
from fastapi import HTTPException
from typing import Optional

logger = logging.getLogger("capsulecrm-mcp.api")

# Get API token from environment
CAPSULECRM_ACCESS_TOKEN = os.getenv("CAPSULECRM_ACCESS_TOKEN")
if not CAPSULECRM_ACCESS_TOKEN:
    logger.error("CAPSULECRM_ACCESS_TOKEN environment variable not set")
    raise RuntimeError("CAPSULECRM_ACCESS_TOKEN environment variable not set")

BASE_URL = "https://api.capsulecrm.com/api/v2"

def get_headers():
    """Get HTTP headers for CapsuleCRM API requests."""
    return {
        "Authorization": f"Bearer {CAPSULECRM_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "CapsuleCRM-MCP/1.0"
    }

def request(method: str, endpoint: str, *, params=None, json=None, timeout: int = 30):
    """
    Make authenticated HTTP request to CapsuleCRM API.
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE)
        endpoint: API endpoint path
        params: Query parameters
        json: JSON body data
        timeout: Request timeout in seconds
        
    Returns:
        JSON response data
        
    Raises:
        HTTPException: On API errors or network issues
    """
    url = f"{BASE_URL}{endpoint}"
    headers = get_headers()
    
    try:
        with httpx.Client(timeout=timeout) as client:
            logger.debug(f"Making {method} request to {url}")
            resp = client.request(method, url, headers=headers, params=params, json=json)
            
            # Log response for debugging
            logger.debug(f"Response status: {resp.status_code}")
            
            if not (200 <= resp.status_code < 300):
                error_detail = f"CapsuleCRM API error: {resp.status_code}"
                try:
                    error_data = resp.json()
                    if "message" in error_data:
                        error_detail = f"CapsuleCRM API error: {error_data['message']}"
                except:
                    error_detail = f"CapsuleCRM API error: {resp.text}"
                
                logger.error(f"API request failed: {error_detail}")
                raise HTTPException(status_code=resp.status_code, detail=error_detail)
            
            return resp.json()
            
    except httpx.TimeoutException:
        logger.error(f"Request timeout for {method} {url}")
        raise HTTPException(status_code=408, detail="Request timeout - CapsuleCRM API is not responding")
    except httpx.NetworkError as e:
        logger.error(f"Network error for {method} {url}: {e}")
        raise HTTPException(status_code=503, detail="Network error - Unable to connect to CapsuleCRM API")
    except Exception as e:
        logger.error(f"Unexpected error for {method} {url}: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

def filter_entities(entity: str, filter_obj, page: int = 1, per_page: int = 50, embed: Optional[str] = None):
    """
    Filter entities using CapsuleCRM's filter API.
    
    Args:
        entity: Entity type (parties, opportunities, tasks)
        filter_obj: Filter object with conditions
        page: Page number
        per_page: Items per page
        embed: Additional fields to embed
        
    Returns:
        Filtered results
    """
    params = {"page": page, "perPage": per_page}
    if embed:
        params["embed"] = embed
    
    try:
        data = {"filter": filter_obj.dict(exclude_none=True)}
        endpoint = f"/{entity}/filters/results"
        
        logger.debug(f"Filtering {entity} with conditions: {filter_obj.conditions}")
        return request("POST", endpoint, params=params, json=data)
        
    except Exception as e:
        logger.error(f"Filter operation failed for {entity}: {e}")
        raise 