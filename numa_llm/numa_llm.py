import requests
import subprocess
import time

class NumaLLM:
    def __init__(self, model_name="numa-llm", host="http://localhost:11434"):
        self.model_name = model_name
        self.api_url = f"{host}/api/generate"

        print(f"Initializing Numa LLM with the model '{model_name}'...")
        if not self._is_ollama_running():
            print("Ollama isn't launch yet, trying to launch...")
            self._launch_ollama()
            time.sleep(2)

        if not self._is_model_running():
            print(f"Modèle '{model_name}' isn't loaded, trying to load...")
            self._run_model()
            time.sleep(2)

        print("🔥 Warmup...")
        try:
            _ = requests.post(self.api_url, json={
                "model": self.model_name,
                "prompt": "Hello!",
                "stream": False
            })
            print("Model Ready.")
        except Exception as e:
            print("Failure during warmup :", e)

    def _is_ollama_running(self):
        try:
            r = requests.get("http://localhost:11434")
            return r.status_code == 200
        except:
            return False

    def _launch_ollama(self):
        try:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print("Ollama can't be launched :", e)

    def _is_model_running(self):
        try:
            r = requests.get("http://localhost:11434/api/show")
            return self.model_name in r.json().get("models", [])
        except:
            return False

    def _run_model(self):
        try:
            subprocess.Popen(["ollama", "run", self.model_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print("The model can't be launched :", e)

    def ask(self, emotion, text):
        prompt = (
            "user #Sad Hi Numa, I'm feeling a bit low today...\n"
            "assistant [Compassionate] I'm really sorry you're feeling this way. I'm right here with you.\n"
            f"user #{emotion} {text}\n"
            "assistant"
        )

        try:
            response = requests.post(self.api_url, json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            })

            if response.ok:
                return response.json().get("response", "[Error] No answer.")
            else:
                return f"[HTTP error {response.status_code}] {response.text}"

        except Exception as e:
            return f"[Request error] {e}"

