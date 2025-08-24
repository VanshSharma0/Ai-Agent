from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

load_dotenv()

def test_ollama():
    """Test Ollama local model"""
    try:
        print("Testing Ollama (local model)...")
        llm = Ollama(model="llama2")  # or "mistral", "codellama"
        response = llm.invoke("What is the meaning of life?")
        print("Ollama Response:")
        print(response)
        return True
    except Exception as e:
        print(f"Ollama Error: {e}")
        print("To use Ollama:")
        print("1. Install Ollama from https://ollama.ai/")
        print("2. Run: ollama pull llama2")
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
    print("Testing AI Models...")
    print("=" * 50)
    
    # Check if API keys are set
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    print(f"OpenAI API Key: {'Set' if openai_key else 'Not Set'}")
    print(f"Anthropic API Key: {'Set' if anthropic_key else 'Not Set'}")
    print("-" * 50)
    
    # Try local Ollama first (free)
    print("1. Trying Ollama (Free Local Model)...")
    if test_ollama():
        return
    
    print("\n" + "-" * 50)
    
    # Try OpenAI
    if openai_key:
        print("2. Trying OpenAI...")
        if test_openai():
            return
    
    print("\n" + "-" * 50)
    
    # Try Anthropic
    if anthropic_key:
        print("3. Trying Anthropic...")
        if test_anthropic():
            return
    
    print("\n" + "=" * 50)
    print("All options failed. Here are your next steps:")
    print("1. Install Ollama for free local AI: https://ollama.ai/")
    print("2. Add credits to OpenAI: https://platform.openai.com/billing")
    print("3. Add credits to Anthropic: https://console.anthropic.com/plans")

if __name__ == "__main__":
    main()
