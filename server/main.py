#!/usr/bin/env python3
"""
CapsuleCRM MCP Server
A Model Context Protocol server for CapsuleCRM integration with Claude Desktop.
"""

import os
import sys
import logging
from pathlib import Path

# Add server directory to Python path
server_dir = Path(__file__).parent
sys.path.insert(0, str(server_dir))
sys.path.insert(0, str(server_dir / "lib"))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr  # MCP uses stderr for logging
)
logger = logging.getLogger("capsulecrm-mcp")

try:
    from fastmcp import FastMCP
    
    # Import tool registration functions
    from tools.parties import register_party_tools
    from tools.opportunities import register_opportunity_tools
    from tools.tasks import register_task_tools
    from tools.milestones import register_milestone_tools
    
    logger.info("Starting CapsuleCRM MCP Server...")
    
    # Validate environment
    if not os.getenv("CAPSULECRM_ACCESS_TOKEN"):
        logger.error("CAPSULECRM_ACCESS_TOKEN environment variable not set")
        sys.exit(1)
    
    # Create MCP server instance
    mcp = FastMCP(
        name="capsulecrm-mcp",
        instructions="Use these tools to manage opportunities, parties (customers), and tasks in CapsuleCRM. Support both simple queries and advanced filtering.",
        dependencies=["fastapi", "httpx", "pydantic", "fastmcp"]
    )
    
    # Register all tools by entity
    logger.info("Registering MCP tools...")
    register_party_tools(mcp)
    register_opportunity_tools(mcp)
    register_task_tools(mcp)
    register_milestone_tools(mcp)
    
    logger.info("CapsuleCRM MCP Server initialized successfully")
    
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    sys.exit(1)
except Exception as e:
    logger.error(f"Failed to initialize server: {e}")
    sys.exit(1)

if __name__ == "__main__":
    try:
        # FastMCP automatically uses stdio transport for MCP protocol
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)