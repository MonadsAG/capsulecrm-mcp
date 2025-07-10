import os
from fastmcp import FastMCP
from models import OpportunityCreate, Party, Milestone, Task
from api.parties import list_parties, get_party, create_party, update_party, search_parties, find_parties
from api.opportunities import list_opportunities, get_opportunity, create_opportunity, update_opportunity, search_opportunities, find_opportunities
from api.tasks import list_tasks, get_task, create_task, update_task, search_tasks, find_tasks
from api.milestones import list_milestones
from typing import Optional

mcp = FastMCP(
    name="capsulecrm-mcp",
    instructions="Nutze die Tools, um Opportunities, Parties und Tasks in Capsule CRM zu verwalten.",
    dependencies=["fastapi", "httpx", "pydantic", "fastmcp"]
)

# Parties
@mcp.tool()
def list_parties_tool(page: int = 1, per_page: int = 50) -> list[Party]:
    """
    List all parties (people and organizations) from CapsuleCRM with pagination.
    
    Args:
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
    Returns:
        List[Party]: A list of Party objects (Person or Organisation) with all available details.
    """
    return list_parties(page=page, per_page=per_page)

@mcp.tool()
def get_party_tool(party_id: int) -> Party:
    """
    Get a specific party (person or organization) by ID.
    
    Args:
        party_id (int): The unique ID of the party.
    Returns:
        Party: The requested Party object (Person or Organisation) with all details.
    """
    return get_party(party_id)

@mcp.tool()
def create_party_tool(party: Party) -> Party:
    """
    Create a new party (person or organization) in CapsuleCRM.
    
    Args:
        party (Party): The Party object to create (must be Person or Organisation).
    Returns:
        Party: The created Party object with assigned ID and details.
    """
    return create_party(party)

@mcp.tool()
def update_party_tool(party_id: int, party: Party) -> Party:
    """
    Update an existing party by ID.
    
    Args:
        party_id (int): The unique ID of the party to update.
        party (Party): The updated Party object (Person or Organisation).
    Returns:
        Party: The updated Party object with new details.
    """
    return update_party(party_id, party)

@mcp.tool()
def search_parties_tool(q: str, page: int = 1, per_page: int = 50, embed: Optional[str] = None):
    """
    Search parties by name, address, phone number, or email address.
    
    Args:
        q (str): The search query (e.g. name, postcode, phone number).
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
        embed (str, optional): Comma-separated list of extra fields to include (e.g. 'tags,fields').
    Returns:
        List[Party]: A list of matching Party objects.
    """
    return search_parties(q, page, per_page, embed)

# Opportunities
@mcp.tool()
def list_opportunities_tool(page: int = 1, per_page: int = 50) -> list[dict]:
    """
    List all sales opportunities from CapsuleCRM with pagination.
    
    Args:
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
    Returns:
        List[dict]: A list of opportunity dictionaries. For reporting and value queries, use the 'current_value' attribute if present, as it reflects the probability-weighted value of the opportunity.
    """
    return list_opportunities(page=page, per_page=per_page)

@mcp.tool()
def get_opportunity_tool(opportunity_id: int) -> dict:
    """
    Get a specific sales opportunity by ID with full details.
    
    Args:
        opportunity_id (int): The unique ID of the opportunity.
    Returns:
        dict: The opportunity details, including value, probability, and calculated fields. For reporting and value queries, use the 'current_value' attribute if present.
    """
    return get_opportunity(opportunity_id)

@mcp.tool()
def create_opportunity_tool(opportunity: OpportunityCreate) -> dict:
    """
    Create a new sales opportunity with name, party, milestone, and value.
    
    Args:
        opportunity (OpportunityCreate): The opportunity to create.
    Returns:
        dict: The created opportunity with assigned ID and calculated fields. For reporting and value queries, use the 'current_value' attribute if present.
    """
    return create_opportunity(opportunity)

@mcp.tool()
def update_opportunity_tool(opportunity_id: int, opportunity: OpportunityCreate) -> dict:
    """
    Update an existing sales opportunity by ID.
    
    Args:
        opportunity_id (int): The unique ID of the opportunity to update.
        opportunity (OpportunityCreate): The updated opportunity data.
    Returns:
        dict: The updated opportunity with new details and calculated fields. For reporting and value queries, use the 'current_value' attribute if present.
    """
    return update_opportunity(opportunity_id, opportunity)

@mcp.tool()
def search_opportunities_tool(q: str, page: int = 1, per_page: int = 50, embed: Optional[str] = None):
    """
    Search opportunities by name, description, or associated party details.
    
    Args:
        q (str): The search query (e.g. name, description, party name).
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
        embed (str, optional): Comma-separated list of extra fields to include (e.g. 'tags,fields').
    Returns:
        List[dict]: A list of matching opportunities with calculated fields. For reporting and value queries, use the 'current_value' attribute if present.
    """
    return search_opportunities(q, page, per_page, embed)

# Tasks
@mcp.tool()
def list_tasks_tool(page: int = 1, per_page: int = 50, status: str = "open") -> list[Task]:
    """
    List tasks with filtering by status: 'open', 'completed', or 'pending'.
    
    Args:
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
        status (str): Filter by task status ('open', 'completed', 'pending').
    Returns:
        List[Task]: A list of Task objects with all details.
    """
    return list_tasks(page=page, per_page=per_page, status=status)

@mcp.tool()
def get_task_tool(task_id: int) -> Task:
    """
    Get a specific task by ID with full details including due date and owner.
    
    Args:
        task_id (int): The unique ID of the task.
    Returns:
        Task: The requested Task object with all details.
    """
    return get_task(task_id)

@mcp.tool()
def create_task_tool(task: Task) -> Task:
    """
    Create a new task with description, due date, and assignment details.
    
    Args:
        task (Task): The Task object to create.
    Returns:
        Task: The created Task object with assigned ID and details.
    """
    return create_task(task)

@mcp.tool()
def update_task_tool(task_id: int, task: Task) -> Task:
    """
    Update an existing task by ID, including status, due date, or assignment.
    
    Args:
        task_id (int): The unique ID of the task to update.
        task (Task): The updated Task object.
    Returns:
        Task: The updated Task object with new details.
    """
    return update_task(task_id, task)

@mcp.tool()
def search_tasks_tool(q: str, page: int = 1, per_page: int = 50, embed: Optional[str] = None):
    """
    Search tasks by description, status, or associated party/opportunity.
    
    Args:
        q (str): The search query (e.g. description, status, party name).
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
        embed (str, optional): Comma-separated list of extra fields to include (e.g. 'party,opportunity').
    Returns:
        List[Task]: A list of matching Task objects.
    """
    return search_tasks(q, page, per_page, embed)

# Milestones
@mcp.tool()
def list_milestones_tool(page: int = 1, per_page: int = 50) -> list[Milestone]:
    """
    List all pipeline milestones used for tracking opportunity progress.
    
    Args:
        page (int): The page of results to return (default: 1).
        per_page (int): The number of entities per page (default: 50).
    Returns:
        List[Milestone]: A list of Milestone objects with all details.
    """
    return list_milestones(page=page, per_page=per_page)

# Advanced search functions
@mcp.tool()
def find_opportunities_tool(user_input: dict):
    """
    Find opportunities with structured filters or free text search.
    
    Args:
        user_input (dict): Dictionary of search and/or filter parameters. Use 'q' for free text, or filterable fields like 'status', 'tag', 'owner', etc.
    Returns:
        List[dict]: A list of matching opportunities with calculated fields. For reporting and value queries, use the 'current_value' attribute if present.
    """
    return find_opportunities(user_input)

@mcp.tool()
def find_parties_tool(user_input: dict):
    """
    Find parties (people/organizations) with structured filters or free text search.
    
    Args:
        user_input (dict): Dictionary of search and/or filter parameters. Use 'q' for free text, or filterable fields like 'tag', 'type', 'owner', etc.
    Returns:
        List[Party]: A list of matching Party objects.
    """
    return find_parties(user_input)

@mcp.tool()
def find_tasks_tool(user_input: dict):
    """
    Find tasks with structured filters or free text search.
    
    Args:
        user_input (dict): Dictionary of search and/or filter parameters. Use 'q' for free text, or filterable fields like 'status', 'tag', 'owner', etc.
    Returns:
        List[Task]: A list of matching Task objects.
    """
    return find_tasks(user_input)

if __name__ == "__main__":
    mcp.run() 