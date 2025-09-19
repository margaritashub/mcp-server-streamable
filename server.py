from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Streamable", host="0.0.0.0", port=8000)

@mcp.tool()
def greeting(name: str) -> str:
    """Send a greeting"""
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")