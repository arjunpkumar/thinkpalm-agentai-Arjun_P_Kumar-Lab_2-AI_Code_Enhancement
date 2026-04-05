import os
import warnings
import logging
import nest_asyncio
from google.colab import userdata

# 1. AGGRESSIVE SILENCING (Muting the 'noise')
warnings.filterwarnings("ignore")
logging.getLogger("jupyter_client.session").setLevel(logging.ERROR)
os.environ["GRPC_VERBOSITY"] = "ERROR"

# 2. COLAB SETUP
nest_asyncio.apply()
os.environ["GOOGLE_API_KEY"] = userdata.get('GEMINI_API_KEY')

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver 
from langchain_core.tools import tool

# 3. ROBUST SEARCH TOOL
@tool
def internet_search(query: str) -> str:
    """Useful for finding current prices and real-time news."""
    from ddgs import DDGS
    try:
        with DDGS() as ddgs:
            # Fetch 10 results to ensure the Lite model 'sees' the number
            results = [r['body'] for r in ddgs.text(query, max_results=10)]
            return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search failed: {e}. Please try again."

# 4. AGENT CLASS
class ResearchAgent:
    def __init__(self):
        # We use temperature 0 for the most 'factual' and stable results
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
        self.memory = MemorySaver()
        
        # PROMPT
        self.system_message = (
            "You are a helpful assistant. To find a price:\n"
            "1. Search for 'Current Bitcoin Price USD live'.\n"
            "2. Scan the search results for a dollar amount (e.g., $65,000).\n"
            "3. If you see it, report it immediately.\n"
            "4. If you don't see it, try searching 'CoinMarketCap Bitcoin' and look again."
        )
        
        self.agent = create_react_agent(
            self.llm, 
            [internet_search], 
            checkpointer=self.memory
        )

    async def run(self, user_input: str, thread_id: str):
        config = {"configurable": {"thread_id": thread_id}}
        
        # We send the system message and user query
        inputs = {"messages": [("system", self.system_message), ("user", user_input)]}
        
        print(f"📡 Processing [Thread: {thread_id}]...")
        
        async for event in self.agent.astream(inputs, config=config, stream_mode="values"):
            message = event["messages"][-1]
            
            # Clean output logic
            if message.type == "ai" and message.content:
                if not message.tool_calls:
                    print(f"\n✅ Final Answer: {message.content}")
            elif hasattr(message, "tool_calls") and message.tool_calls:
                print(f"🔍 Searching for: {message.tool_calls[0]['args']['query']}...")

# 5. EXECUTION
bot = ResearchAgent()
# Use a specific query to help the Lite model
await bot.run("What is the current Bitcoin price in USD?", "session_777")