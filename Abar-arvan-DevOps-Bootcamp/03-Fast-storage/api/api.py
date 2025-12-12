from fastapi import FastAPI, Header
from typing import Optional, Dict
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)


@app.get("/")
def root(CLIENT_KEY: Optional[str] = Header(None)):


    if CLIENT_KEY is not None:
        r.incr(CLIENT_KEY)  

    state: Dict[str, int] = {}

    keys = r.keys("*")
    if keys:
        values = r.mget(keys)
        state = {k: int(v) for k, v in zip(keys, values) if v is not None}

    return {"state": state}
