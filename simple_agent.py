"""
Simple Investment Agent - Minimal Example
"""

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
import yfinance as yf

@tool
def get_stock_price(symbol: str) -> str:
    """Get current stock price for a symbol."""
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d")
    price = hist['Close'].iloc[-1]
    return f"Current price of {symbol}: ${price:.2f}"

def create_simple_agent(api_key: str):
    """Create a simple agent with one tool."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)
    tools = [get_stock_price]
    return create_react_agent(llm, tools)

def analyze_stock(agent, symbol: str):
    """Ask agent to analyze a stock."""
    prompt = f"""
    Create a simple investment report for {symbol}.
    
    First, make a plan:
    1. Get the current stock price
    2. Write a brief analysis
    
    Then follow your plan and create the report.
    """
    
    result = agent.invoke({"messages": [("user", prompt)]})
    return result["messages"][-1].content

if __name__ == "__main__":
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    
    agent = create_simple_agent(api_key)
    report = analyze_stock(agent, "AAPL")
    print(report)
