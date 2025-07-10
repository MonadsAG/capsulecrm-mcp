from .utils import request, filter_entities
from .models import Party, Person, Organisation, Filter, Condition
from typing import List, Union, Optional

def list_parties(page: int = 1, per_page: int = 50) -> List[Party]:
    data = request("GET", "/parties", params={"page": page, "perPage": per_page})
    parties = []
    for party in data.get("parties", []):
        if party.get("type") == "person":
            parties.append(Person(**party))
        elif party.get("type") == "organisation":
            parties.append(Organisation(**party))
    return parties

def search_parties(q: str, page: int = 1, per_page: int = 50, embed: Optional[str] = None) -> List[Party]:
    params = {"q": q, "page": page, "perPage": per_page}
    if embed:
        params["embed"] = embed
    data = request("GET", "/parties/search", params=params)
    parties = []
    for party in data.get("parties", []):
        if party.get("type") == "person":
            parties.append(Person(**party))
        elif party.get("type") == "organisation":
            parties.append(Organisation(**party))
    return parties

def filter_parties(filter_obj: Filter, page: int = 1, per_page: int = 50, embed: Optional[str] = None) -> List[Party]:
    data = filter_entities("parties", filter_obj, page, per_page, embed)
    parties = []
    for party in data.get("parties", []):
        if party.get("type") == "person":
            parties.append(Person(**party))
        elif party.get("type") == "organisation":
            parties.append(Organisation(**party))
    return parties

def find_parties(user_input: dict):
    # Extended filterable fields based on CapsuleCRM API documentation
    filterable_fields = {
        "tag", "addedOn", "owner", "type", "name", "jobTitle", "email", 
        "phone", "city", "hasEmailAddress", "hasPeople", "updatedOn", 
        "lastContactedOn", "id", "team"
    }
    
    # Extract pagination and embed parameters
    page = user_input.get("page", 1)
    per_page = user_input.get("per_page", 50)
    embed = user_input.get("embed")
    
    # Build filter conditions with operator support
    filter_conditions = []
    for key in filterable_fields:
        if key in user_input:
            value = user_input[key]
            operator = "is"  # default operator
            
            # Handle operator specification in field names like "addedOn_after"
            if "_" in key:
                field_name, op_suffix = key.split("_", 1)
                if field_name in filterable_fields:
                    operator_map = {
                        "after": "is after",
                        "before": "is before", 
                        "contains": "contains",
                        "starts": "starts with",
                        "ends": "ends with",
                        "gt": "is greater than",
                        "lt": "is less than",
                        "within": "is within last",
                        "not": "is not"
                    }
                    operator = operator_map.get(op_suffix, "is")
                    key = field_name
            
            # Handle operator specified in value dict
            if isinstance(value, dict) and "operator" in value:
                operator = value["operator"]
                value = value["value"]
            
            filter_conditions.append(Condition(field=key, operator=operator, value=str(value)))
    
    # Decide whether to use filtering, search, or list
    if filter_conditions:
        filter_obj = Filter(conditions=filter_conditions)
        return filter_parties(filter_obj, page, per_page, embed)
    elif "q" in user_input:
        return search_parties(user_input["q"], page, per_page, embed)
    else:
        return list_parties(page, per_page)

def list_persons(page: int = 1, per_page: int = 50) -> List[Person]:
    return [p for p in list_parties(page, per_page) if isinstance(p, Person)]

def list_organisations(page: int = 1, per_page: int = 50) -> List[Organisation]:
    return [o for o in list_parties(page, per_page) if isinstance(o, Organisation)]

def get_party(party_id: int) -> Party:
    data = request("GET", f"/parties/{party_id}")
    party = data["party"]
    if party.get("type") == "person":
        return Person(**party)
    elif party.get("type") == "organisation":
        return Organisation(**party)
    else:
        raise ValueError("Unknown party type")

def create_party(party: Party) -> Party:
    # party is either Person or Organisation
    data = request("POST", "/parties", json={"party": party.dict(exclude_none=True)})
    party_data = data["party"]
    if party_data.get("type") == "person":
        return Person(**party_data)
    elif party_data.get("type") == "organisation":
        return Organisation(**party_data)
    else:
        raise ValueError("Unknown party type")

def update_party(party_id: int, party: Party) -> Party:
    data = request("PUT", f"/parties/{party_id}", json={"party": party.dict(exclude_none=True)})
    party_data = data["party"]
    if party_data.get("type") == "person":
        return Person(**party_data)
    elif party_data.get("type") == "organisation":
        return Organisation(**party_data)
    else:
        raise ValueError("Unknown party type") 