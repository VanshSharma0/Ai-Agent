from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

load_dotenv()

def test_perplexity():
    """Test Perplexity API connection"""
    try:
        # Perplexity uses OpenAI-compatible API
        llm = ChatOpenAI(
            model="sonar-pro",  # Correct Perplexity model name
            api_key=os.getenv("PERPLEXITY_API_KEY"),
            base_url="https://api.perplexity.ai"
        )
        response = llm.invoke("What is the meaning of betrayal?")
        print("Perplexity Response:")
        print(response.content)
        return True
    except Exception as e:
        print(f"Perplexity API Error: {e}")
        return False

def test_openai():
    """Test OpenAI API connection"""
    try:
        llm = ChatOpenAI(model="gpt-4o-mini")
        response = llm.invoke("What is the meaning of life?")
        print("OpenAI Response:")
        print(response.content)
        return True
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return False

def test_anthropic():
    """Test Anthropic API connection"""
    try:
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
        response = llm.invoke("What is the meaning of life?")
        print("Anthropic Response:")
        print(response.content)
        return True
    except Exception as e:
        print(f"Anthropic API Error: {e}")
        return False

def main():
    print("Testing AI APIs...")
    
    # Check if API keys are set
    perplexity_key = os.getenv("PERPLEXITY_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    print(f"Perplexity API Key: {'Set' if perplexity_key and perplexity_key != 'your_perplexity_api_key_here' else 'Not Set'}")
    print(f"OpenAI API Key: {'Set' if openai_key else 'Not Set'}")
    print(f"Anthropic API Key: {'Set' if anthropic_key else 'Not Set'}")
    print("-" * 50)
    
    # Try Perplexity first (your Pro subscription)
    if perplexity_key and perplexity_key != 'your_perplexity_api_key_here':
        print("Attempting Perplexity...")
        if test_perplexity():
            return
    
    # If Perplexity fails, try OpenAI
    if openai_key:
        print("\nAttempting OpenAI...")
        if test_openai():
            return
    
    # If OpenAI fails, try Anthropic
    if anthropic_key:
        print("\nAttempting Anthropic...")
        if test_anthropic():
            return
    
    print("\nAll APIs failed or API keys not available.")
    print("Please check your API keys and quotas.")

if __name__ == "__main__":
    main()