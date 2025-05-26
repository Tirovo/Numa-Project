from fastapi import FastAPI
from pydantic import BaseModel
from numa_llm import NumaLLM
import uvicorn
import requests

app = FastAPI()
llm = NumaLLM()  # Loading and Warmup

class AskRequest(BaseModel):
    emotion: str
    message: str

@app.post("/ask")
def ask(req: AskRequest):
    response = llm.ask(req.emotion, req.message)

    # Sending the answer to another api (here the TTS one)
    try:
        forward_payload = {
            "source": "numa",
            "emotion": req.emotion,
            "text": response
        }
        forwarded = requests.post("http://localhost:5000/analyse", json=forward_payload)
        forwarded_data = forwarded.json()
    except Exception as e:
        forwarded_data = {"error": str(e)}

    return {
        "response": response,
        "forwarded": forwarded_data
    }

if __name__ == "__main__":
    # Starting phrase
    print("🧠 NumaLLM prêt à discuter.")
    uvicorn.run("numa_llm_server:app", host="127.0.0.1", port=8000, reload=False)
