from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for a location.
    
    Args:
        location: City name
    
    Returns:
        Weather description for the location
    """
    return f"Weather in {location}: Sunny and 25°C"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
