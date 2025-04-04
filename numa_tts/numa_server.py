from fastapi import FastAPI
from pydantic import BaseModel
from numa_speak import NumaTTS
import uvicorn


app = FastAPI()
numa = NumaTTS(anime_mode=True)
numa.say("Hello! It's me! Numa! What do you want to talk about this time?") # Launch sentence

class SayRequest(BaseModel):
    text: str

@app.post("/say") 
def say(req: SayRequest):
    numa.say(req.text)
    return {"status": "ok", "message": "Text spoken."}

if __name__ == "__main__":
    uvicorn.run("numa_server:app", host="127.0.0.1", port=8000, reload=False)