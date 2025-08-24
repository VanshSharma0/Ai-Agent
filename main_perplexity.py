from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

load_dotenv()

def test_perplexity():
    """Test Perplexity API connection"""
    try:
        # Perplexity uses OpenAI-compatible API
        llm = ChatOpenAI(
            model="sonar-pro",  # Advanced search with grounding
            api_key=os.getenv("PERPLEXITY_API_KEY"),
            base_url="https://api.perplexity.ai"
        )
        response = llm.invoke("What is the meaning of life according to recent philosophical discussions?")
        print("🔍 Perplexity Response (with web search):")
        print(response.content)
        return True
    except Exception as e:
        print(f"❌ Perplexity API Error: {e}")
        return False

def test_perplexity_fast():
    """Test Perplexity with fast model"""
    try:
        llm = ChatOpenAI(
            model="sonar",  # Lightweight, cost-effective search model
            api_key=os.getenv("PERPLEXITY_API_KEY"),
            base_url="https://api.perplexity.ai"
        )
        response = llm.invoke("What are the latest developments in AI?")
        print("⚡ Perplexity Fast Response:")
        print(response.content)
        return True
    except Exception as e:
        print(f"❌ Perplexity Fast API Error: {e}")
        return False

def test_openai():
    """Test OpenAI API connection"""
    try:
        llm = ChatOpenAI(model="gpt-4o-mini")
        response = llm.invoke("What is the meaning of life?")
        print("🤖 OpenAI Response:")
        print(response.content)
        return True
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return False

def test_anthropic():
    """Test Anthropic API connection"""
    try:
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
        response = llm.invoke("What is the meaning of life?")
        print("🧠 Anthropic Response:")
        print(response.content)
        return True
    except Exception as e:
        print(f"❌ Anthropic API Error: {e}")
        return False

def main():
    print("🚀 Testing AI APIs (Perplexity Pro Priority)...")
    print("=" * 60)
    
    # Check if API keys are set
    perplexity_key = os.getenv("PERPLEXITY_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    print(f"🔍 Perplexity API Key: {'✅ Set' if perplexity_key and perplexity_key != 'your_perplexity_api_key_here' else '❌ Not Set'}")
    print(f"🤖 OpenAI API Key: {'✅ Set' if openai_key else '❌ Not Set'}")
    print(f"🧠 Anthropic API Key: {'✅ Set' if anthropic_key else '❌ Not Set'}")
    print("-" * 60)
    
    # Priority 1: Try Perplexity Pro (your preferred choice)
    if perplexity_key and perplexity_key != 'your_perplexity_api_key_here':
        print("1️⃣ Trying Perplexity Pro (Large Model)...")
        if test_perplexity():
            return
        
        print("\n" + "-" * 40)
        print("2️⃣ Trying Perplexity Pro (Fast Model)...")
        if test_perplexity_fast():
            return
    else:
        print("⚠️ Perplexity API key not configured")
    
    print("\n" + "-" * 60)
    
    # Fallback options
    if openai_key:
        print("3️⃣ Trying OpenAI (Fallback)...")
        if test_openai():
            return
    
    if anthropic_key:
        print("4️⃣ Trying Anthropic (Fallback)...")
        if test_anthropic():
            return
    
    print("\n" + "=" * 60)
    print("❌ All APIs failed. Next steps:")
    print("1. Add your Perplexity API key to .env file")
    print("2. Get your API key from: https://www.perplexity.ai/settings/api")
    print("3. Replace 'your_perplexity_api_key_here' in .env with your actual key")

if __name__ == "__main__":
    main()
