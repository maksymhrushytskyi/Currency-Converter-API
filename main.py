from dotenv import load_dotenv
from fastapi import FastAPI
import requests
import os
load_dotenv()
API_exchangerate = os.getenv("API_EXCHANGERATE")

def exchangerate(gerate):

    API_URL = f"https://api.exchangerate.host/live?access_key={API_exchangerate}"
    print(API_URL)
    response = requests.get(API_URL) #підключення
    print(response.status_code) # статус підключення
    resjson = response.json()
    print(resjson['quotes'][gerate]) # отримання 
    return {
    "базова_валюта": "USD",
    "цільова_валюта": gerate[3:],
    "курс": resjson['quotes'][gerate],
    "форматований": f"1 USD = {resjson['quotes'][gerate]} {gerate[3:]}"}

app = FastAPI()

@app.get("/")
def root():
    return exchangerate("USDUAH")