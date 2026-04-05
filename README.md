# Agentic AI Workshop: Stateful Research Agent

## 🚀 Project Overview
This project demonstrates the evolution of an AI agent from a basic **stateless prototype** to a **production-ready, stateful research agent**. It utilizes **LangGraph** for orchestration and **Google Gemini 2.5 Flash-Lite** as the reasoning engine.

### 🏗️ Evolution Path
1. **v1 (Prototype):** A simple ReAct agent capable of one-off internet searches.
2. **v2 (Production-Ready):** A modular, stateful agent with persistent memory, custom error handling, and optimized system instructions.

---

## 🛠️ Tech Stack
- **Orchestration:** [LangGraph](https://github.com/langchain-ai/langgraph)
- **LLM:** Google Gemini 2.5 Flash-Lite
- **Tools:** DuckDuckGo Search (via `ddgs`)
- **Environment:** Google Colab / Python 3.12

---

## 🧪 Key Enhancements (Technical Lead Perspective)

### 1. Persistence & Memory
Unlike the prototype, the enhanced version implements `MemorySaver`. This allows the agent to maintain a `thread_id`, enabling multi-turn conversations where the agent remembers previous context.

### 2. Environment Resilience
Implemented granular logging overrides and `nest_asyncio` to handle the specific constraints of the Google Colab/IPython environment, eliminating kernel-level deprecation noise.

### 3. Model-Specific Optimization
To compensate for the smaller reasoning window of the `flash-lite` model, I implemented **Instruction Tuning**. By providing a "Chain of Verification" system prompt, the agent is forced to verify numerical data (like Bitcoin prices) rather than giving up on vague search results.

---

## 🚀 How to Run
1. Ensure your `GEMINI_API_KEY` is added to your environment secrets.
2. Install dependencies:
   ```bash
   pip install -U langchain-google-genai langgraph duckduckgo-search nest_asyncio