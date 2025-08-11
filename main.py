from dotenv import load_dotenv
import os

load_dotenv()
API_exchangerate = os.getenv("API_EXCHANGERATE")
print(API_exchangerate)