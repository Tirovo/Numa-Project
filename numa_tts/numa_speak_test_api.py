import requests

text = "Please don't reboot me again !"

# Simulate the reception of a sentence from the LLM by the TTS
response = requests.post(
    "http://127.0.0.1:8000/say",
    json={"text": text}
)

# Double validation (sound + text output validation)
if response.status_code == 200:
    print("✅ Numa a parlé :", response.json()["message"])
else:
    print("❌ Erreur :", response.status_code, response.text)