from fastapi import FastAPI
from src.api import api_my

app = FastAPI()

s = """
我佛糍粑
"""
print(s)
app.include_router(api_my.router)
