from bs4 import BeautifulSoup
import requests
from langchain_groq import ChatGroq
from langchain_classic.agents import create_react_agent,AgentExecutor
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

load_dotenv()
# make a llm
llm=ChatGroq(model='llama-3.3-70b-versatile')

# fast api server for backend
app = FastAPI()

# CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# *********************************Serve Frontend UI****************************
app.mount("/public",StaticFiles(directory='public'),name='public')
# get request from server
@app.get("/")
def serve_frontend():
    return FileResponse("public/index.html")

# ***************************************TOOLS***********************************
# web search tool
tavilytool=TavilySearch(max_results=2)

# web scraping tool
@tool
def web_scrape(url):
    """This tool have to generate a data from any web services.
    """
    try:
        header={
            'User-agent':'Mozilla/5.0'
        }
        res=requests.get(url,headers=header,timeout=5)
        # used bs4
        soup=BeautifulSoup(res.text,'html.parser')

        paragraph=soup.find_all('p')
        text=" ".join([p.get_text() for p in paragraph])
        return text[:300]
    except:
        return ""

# prompt
prompt=PromptTemplate.from_template("""Answer the following questions as best you can. You have access to the following tools:

{tools}
Use the following format:

Question: the input question you must answer
IMPORTANT RULES:
- If user say hi and hello so you only say `hello,how can i assist today`.
- If the question involves current or real-time information, you MUST use tavily_search.
- NEVER say "I don’t have real-time data" or "based on my knowledge cutoff".
- ALWAYS generate clean search queries (no words like "past", "before knowledge cutoff", etc.)
- Prefer real-time data over your own knowledge.
- If you know answer in two iteration then generate a clean output,otherwise take time to generate answer.
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}""")

# agent creation
agent=create_react_agent(llm=llm,tools=[web_scrape,tavilytool],prompt=prompt)

# agent execution
agent_executor=AgentExecutor(agent=agent,tools=[web_scrape,tavilytool],verbose=True,handle_parsing_errors=True,max_iterations=10)

# *************************************** API ***********************************
class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "✅ Smart Web Research Agent Running"}

@app.post("/ask")
def ask(q: Query):
    try:
        # ✅ IMPORTANT: use 'input'
        result = agent_executor.invoke({"input": q.question})

        return {
            "question": q.question,
            "answer": result.get("output", "No answer found")
        }

    except Exception as e:
        return {
            "error": str(e)
        }
