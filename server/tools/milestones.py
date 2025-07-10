"""Milestone & Pipeline MCP Tools"""

from api.models import Milestone
from api.milestones import list_milestones


def register_milestone_tools(mcp):
    """Register all milestone-related MCP tools"""
    
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