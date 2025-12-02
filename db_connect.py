import os
from dotenv import load_dotenv

from langchain_community.utilities import SQLDatabase

load_dotenv()

ai_agent = os.getenv("AI_AGENT_DB")

ai_agent_password = os.getenv("AI_AGENT_DB_PASSWORD")
ai_agent_host = os.getenv("AI_AGENT_DB_HOST")
ai_agent_db_name = os.getenv("AI_AGENT_DB_NAME")
ai_agent_port = os.getenv("AI_AGENT_DB_PORT")

db = SQLDatabase.from_uri(f"mysql+mysqlconnector://{ai_agent}:{ai_agent_password}@{ai_agent_host}:{ai_agent_port}/{ai_agent_db_name}")

# print(f'Sample output: {db.run("SELECT * FROM movies LIMIT 5;")}')