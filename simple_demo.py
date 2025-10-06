from simple_agent import create_simple_agent, analyze_stock
import os

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable")
        return
    
    print("Simple Investment Agent")
    print("Enter a stock symbol (or 'quit'):")
    
    agent = create_simple_agent(api_key)
    
    while True:
        symbol = input("> ").strip().upper()
        if symbol == "QUIT":
            break
        
        if symbol:
            print(f"\nAnalyzing {symbol}...")
            report = analyze_stock(agent, symbol)
            print(f"\nReport:\n{report}")

if __name__ == "__main__":
    main()
