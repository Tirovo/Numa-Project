import requests

API_URL = "http://localhost:8000/ask"

def test_numa(emotion="Happy", message="Hello Numa, what's your purpose?"):
    payload = {
        "emotion": emotion,
        "message": message
    }

    try:
        print(f"Sending the test : [{emotion}] {message}")
        response = requests.post(API_URL, json=payload)

        if response.ok:
            data = response.json()
            print("\nNuma's answer :")
            print(data["response"])
            if "forwarded" in data:
                print("\n📡 Forward result if used :")
                print(data["forwarded"])
        else:
            print(f"Error HTTP {response.status_code} : {response.text}")

    except Exception as e:
        print("Error during request :", e)

if __name__ == "__main__":
    test_numa()
