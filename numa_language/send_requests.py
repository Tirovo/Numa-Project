import requests

def ask_numa_llm(user_emotion, user_text):
    # Historique simulé pour guider le modèle (optionnel)
    full_prompt = (
        "user #Sad Hi Numa, I'm feeling a bit low today...\n"
        "assistant [Compassionate] I'm really sorry you're feeling this way. I'm right here with you.\n"
        f"user #{user_emotion} {user_text}\n"
        "assistant"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "numa-llm",
            "prompt": full_prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "[Error] No valid response generated.")
