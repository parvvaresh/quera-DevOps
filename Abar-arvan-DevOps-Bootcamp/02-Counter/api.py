from fastapi import FastAPI, Header
from typing import Optional, Dict

app = FastAPI()

# state تمام شمارش‌ها را در حافظه نگه می‌دارد
state: Dict[str, int] = {}


@app.get("/")
def root(CLIENT_KEY: Optional[str] = Header(None)):

    if CLIENT_KEY is not None:
        state[CLIENT_KEY] = state.get(CLIENT_KEY, 0) + 1

    return {"state": state}
