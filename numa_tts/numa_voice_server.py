from fastapi import FastAPI
from pydantic import BaseModel
from numa_speak import NumaTTS
import uvicorn

'''print(" Now launching the NumaTTS local server...")'''
# Local server launch
app = FastAPI()
tts = NumaTTS(highPitch_mode=True)

class SayRequest(BaseModel):
    text: str

@app.post("/say") 
def say(req: SayRequest):
    tts.say(req.text)
    return {"status": "ok", "message": "Text spoken."}

if __name__ == "__main__":
    tts.say("Hello! It's me! Numa! What do you want to talk about this time?") # Launch sentence
    uvicorn.run("numa_voice_server:app", host="127.0.0.1", port=8000, reload=False)