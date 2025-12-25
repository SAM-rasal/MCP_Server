from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

# Define tools
@tool
def add(a: int, b: int) -> int:
    """Add two integer numbers together.
    
    Args:
        a: An integer number
        b: An integer number
    
    Returns:
        The sum of a and b as an integer
    """
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integer numbers together.
    
    Args:
        a: An integer number
        b: An integer number
    
    Returns:
        The product of a and b as an integer
    """
    return a * b

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location.
    
    Args:
        location: The name of a city or location
    
    Returns:
        A description of the weather in that location
    """
    return f"Weather in {location}: Sunny, 25°C, Light breeze"

def format_response(title, content):
    """Format output nicely"""
    print(f"\n{title}")
    print("-" * 70)
    print(content)
    print("-" * 70)

def main():
    print("\n" + "="*70)
    print("GROQ AI AGENT - INTELLIGENT PROBLEM SOLVER")
    print("="*70)
    
    # Set API key
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    # Initialize model
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        timeout=30
    )
    
    # Create tools
    tools = [add, multiply, get_weather]
    
    # Create agent
    agent = create_react_agent(model, tools)
    
    # Test 1: Math Query with Explanation Request
    print("\n" + "="*70)
    print("PROBLEM: (3 + 5) x 12")
    print("="*70)
    try:
        response = agent.invoke({
            "messages": [{
                "role": "user", 
                "content": "Solve (3 + 5) x 12."
            }]
        })
        
        result = response["messages"][-1].content
        format_response("Output", result)
        
    except Exception as e:
        print(f" Error: {str(e)[:150]}")
    
    # Test 2: Weather Query
    print("\n" + "="*70)
    print("QUESTION: Weather in London")
    print("="*70)
    try:
        response = agent.invoke({
            "messages": [{
                "role": "user", 
                "content": "What is the weather in California"
            }]
        })
        
        result = response["messages"][-1].content
        format_response("Weather Information", result)
        
    except Exception as e:
        print(f" Error: {str(e)[:150]}")
    

if __name__ == "__main__":
    main()
