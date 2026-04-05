import os
from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

# 2. Configuration
os.environ["GOOGLE_API_KEY"] = userdata.get('GEMINI_API_KEY')

# 3. Custom Search Tool (Bypassing legacy community wrapper bugs)
@tool
def internet_search(query: str):
    """Searches the internet for real-time news, facts, and events."""
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        # Returns a list of result snippets
        results = [r['body'] for r in ddgs.text(query, max_results=3)]
        return "\n".join(results)

# 4. Initialize Gemini (Using the current 2026 flagship)
# Note: Gemini 2.5 Flash is available, but 3.1 is the 2026 recommendation
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

# 5. Create the Agent (The modern replacement for initialize_agent)
agent_executor = create_react_agent(llm, tools=[internet_search])

# 6. Run a Live Query
query = "What is the current price of Bitcoin today"
print(f"User: {query}\n")

# Use 'stream' to see the Thought -> Action -> Observation flow
for chunk in agent_executor.stream({"messages": [("user", query)]}, stream_mode="values"):
    message = chunk["messages"][-1]
    if message.type == "ai":
        if message.tool_calls:
            print(f"🎬 Action: Searching for '{message.tool_calls[0]['args']['query']}'...")
        elif message.content:
            print(f"\n🧠 Final Answer: {message.content}")