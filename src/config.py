import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)

# Format the v1 base URLs
mini_base = os.getenv("AZURE_MINI_ENDPOINT", "").rstrip('/')
main_base = os.getenv("AZURE_MAIN_ENDPOINT", "").rstrip('/')

# 1. Initialize Client for GPT-5.4 mini (Router)
client_mini = OpenAI(
    api_key=os.getenv("AZURE_MINI_API_KEY"),
    base_url=f"{mini_base}/openai/v1/"
)

DEPLOYMENT_MINI = os.getenv("AZURE_MINI_DEPLOYMENT", "gpt-5.4-mini")

# 2. Initialize Client for GPT-5.4 Main (Mentor Voice)
client_main = OpenAI(
    api_key=os.getenv("AZURE_MAIN_API_KEY"),
    base_url=f"{main_base}/openai/v1/"
)

DEPLOYMENT_MAIN = os.getenv("AZURE_MAIN_DEPLOYMENT", "gpt-5.4")