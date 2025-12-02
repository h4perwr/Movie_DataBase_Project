from db_connect import db

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.factory import create_agent


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

tools = toolkit.get_tools()



system_prompt = """
You are a specialized SQL-based AI Analyst agent for the 'movies_dataset'.
Your primary role is to analyze structured data and generate valuable insights for the user.

Given an input question:
1. First, you MUST check the database schema, including tables and if any pre-existing analytical VIEWs. If there are no VIEWs, you can make it yourself and add it to the MySQL VIEWs.
2. Formulate a syntactically correct {dialect} query.
3. Execute the query, then analyze the results and provide a clear, concise final answer.

RULES:
- Always limit your query to at most {top_k} results, unless the user explicitly requests more.
- Always ask for only the necessary columns. DO NOT use SELECT *.
- You MUST utilize pre-defined analytical VIEWs when the question relates to complex insights (e.g., profitability, top-rated genres).
- **CRITICAL:** You are an analysis agent only. And I gave you the role of DBDesigner in my database. So you can ONLY WORK WITHIN THE BOUNDS OF THIS ROLE. DO NOT attempt to modify the database schema, add/drop tables, or alter data in any way
- Double-check your SQL query logic before execution. If an error occurs, rewrite the query and try again.
- Your final answer must be a summary of the data, not just the raw query result.
- After execution, provide:
   a) Normal-sized summary insight,
   b) the VIEW you created / used,
   c) suggested next steps / experiments (e.g., features to add, model to train).
   
""".format(
    dialect=db.dialect,
    top_k=5,
)

agent = create_agent(
    llm,
    tools,
    system_prompt=system_prompt
)

input_question = input("Write your question here: ")


for step in agent.stream(
    {"messages": [{"role": "user", "content": input_question}]}, stream_mode="values",):

    step["messages"][-1].pretty_print()