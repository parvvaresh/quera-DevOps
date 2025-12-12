from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from typing import Optional, Dict, List
import time

app = FastAPI()

state: Dict[str, int] = {}

request_times: Dict[str, List[float]] = {}

RATE_LIMIT = 10        
WINDOW_SECONDS = 60    


@app.get("/")
def root(CLIENT_KEY: Optional[str] = Header(None)):
    if CLIENT_KEY is None:
        return {"state": state}

    now = time.time()

    times = request_times.get(CLIENT_KEY, [])

    times = [t for t in times if now - t <= WINDOW_SECONDS]

    if len(times) >= RATE_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"message": f"Too many request from {CLIENT_KEY}"},
        )

    times.append(now)
    request_times[CLIENT_KEY] = times

    state[CLIENT_KEY] = state.get(CLIENT_KEY, 0) + 1

    return {"state": state}
