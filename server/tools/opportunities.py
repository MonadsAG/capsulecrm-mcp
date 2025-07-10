"""Opportunity (Sales) MCP Tools"""

from typing import Optional
from api.models import OpportunityCreate
from api.opportunities import list_opportunities, get_opportunity, create_opportunity, update_opportunity, search_opportunities, find_opportunities


def register_opportunity_tools(mcp):
    """Register all opportunity-related MCP tools"""
    
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