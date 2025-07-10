"""Task Management MCP Tools"""

from typing import Optional
from api.models import Task
from api.tasks import list_tasks, get_task, create_task, update_task, search_tasks, find_tasks


def register_task_tools(mcp):
    """Register all task-related MCP tools"""
    
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