import os
from dotenv import load_dotenv
import openai

openai.api_key = os.environ.get("api_key")