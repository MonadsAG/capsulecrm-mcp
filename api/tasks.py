from api.utils import request, filter_entities
from models import Task, Filter, Condition
from typing import List, Optional

def list_tasks(page: int = 1, per_page: int = 50, status: str = "open") -> List[Task]:
    data = request("GET", "/tasks", params={"page": page, "perPage": per_page, "status": status})
    return [Task(**task) for task in data.get("tasks", [])]

def search_tasks(q: str, page: int = 1, per_page: int = 50, embed: Optional[str] = None) -> List[Task]:
    params = {"q": q, "page": page, "perPage": per_page}
    if embed:
        params["embed"] = embed
    data = request("GET", "/tasks/search", params=params)
    return [Task(**task) for task in data.get("tasks", [])]

def get_task(task_id: int) -> Task:
    data = request("GET", f"/tasks/{task_id}")
    return Task(**data["task"])

def create_task(task: Task) -> Task:
    data = request("POST", "/tasks", json={"task": task.dict(exclude_none=True)})
    return Task(**data["task"])

def update_task(task_id: int, task: Task) -> Task:
    data = request("PUT", f"/tasks/{task_id}", json={"task": task.dict(exclude_none=True)})
    return Task(**data["task"])

def filter_tasks(filter_obj: Filter, page: int = 1, per_page: int = 50, embed: Optional[str] = None) -> List[Task]:
    data = filter_entities("tasks", filter_obj, page, per_page, embed)
    return [Task(**task) for task in data.get("tasks", [])]

def find_tasks(user_input: dict):
    # Extended filterable fields based on CapsuleCRM API documentation
    filterable_fields = {
        "status", "tag", "dueOn", "owner", "id", "category", "party", 
        "opportunity", "completedOn", "description", "addedOn", "updatedOn"
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
            
            # Handle operator specification in field names like "dueOn_after"
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
        return filter_tasks(filter_obj, page, per_page, embed)
    elif "q" in user_input:
        return search_tasks(user_input["q"], page, per_page, embed)
    else:
        return list_tasks(page, per_page) 