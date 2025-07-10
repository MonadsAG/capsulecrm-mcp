"""Party (People & Organizations) MCP Tools"""

from typing import Optional
from api.models import Party
from api.parties import list_parties, get_party, create_party, update_party, search_parties, find_parties


def register_party_tools(mcp):
    """Register all party-related MCP tools"""
    
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