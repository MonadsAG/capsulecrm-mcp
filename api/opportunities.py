from api.utils import request, filter_entities
from models import OpportunityCreate, Filter, Condition
from typing import List, Optional

# You may want to define an Opportunity model for full read support, but for now use dict for responses

def list_opportunities(page: int = 1, per_page: int = 50) -> List[dict]:
    data = request("GET", "/opportunities", params={"page": page, "perPage": per_page})
    return data.get("opportunities", [])

def search_opportunities(q: str, page: int = 1, per_page: int = 50, embed: Optional[str] = None) -> List[dict]:
    params = {"q": q, "page": page, "perPage": per_page}
    if embed:
        params["embed"] = embed
    data = request("GET", "/opportunities/search", params=params)
    return data.get("opportunities", [])

def filter_opportunities(filter_obj: Filter, page: int = 1, per_page: int = 50, embed: Optional[str] = None) -> List[dict]:
    data = filter_entities("opportunities", filter_obj, page, per_page, embed)
    return data.get("opportunities", [])

def get_opportunity(opportunity_id: int) -> dict:
    data = request("GET", f"/opportunities/{opportunity_id}")
    return data["opportunity"]

def create_opportunity(opportunity: OpportunityCreate) -> dict:
    # Always send value.amount as per-unit value to Capsule.
    # If value_type is 'total', convert total to per-unit by dividing by duration.
    data_dict = opportunity.dict(exclude_none=True)
    value_type = data_dict.pop('value_type', 'per_unit')
    duration = data_dict.get('duration')
    if value_type == 'total' and duration and data_dict['value']['amount'] is not None:
        data_dict['value']['amount'] = data_dict['value']['amount'] / duration
    data = request("POST", "/opportunities", json={"opportunity": data_dict})
    return data["opportunity"]

def update_opportunity(opportunity_id: int, opportunity: OpportunityCreate) -> dict:
    data = request("PUT", f"/opportunities/{opportunity_id}", json={"opportunity": opportunity.dict(exclude_none=True)})
    return data["opportunity"]

def find_opportunities(user_input: dict):
    filterable_fields = {"status", "tag", "addedOn", "owner", "milestone"}
    filter_conditions = []
    for key in filterable_fields:
        if key in user_input:
            filter_conditions.append(Condition(field=key, operator="is", value=user_input[key]))
    if filter_conditions:
        filter_obj = Filter(conditions=filter_conditions)
        return filter_opportunities(filter_obj)
    elif "q" in user_input:
        return search_opportunities(user_input["q"])
    else:
        return list_opportunities() 