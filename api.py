import requests
from dotenv import load_dotenv
import os

# Ładuje zmienne środowiskowe z pliku .env
load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")
LANGFLOW_ID = os.getenv("LANGFLOW_ID")
ENDPOINT = os.getenv("ENDPOINT")
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")

def run_flow(message, tweaks=None):
    """
    Wywołuje przepływ Langflow API z podanym komunikatem i tweaks.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    if tweaks:
        payload["tweaks"] = tweaks

    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Wyciągamy właściwy tekst z zagnieżdżonej struktury
        try:
            text = data['outputs'][0]['outputs'][0]['results']['text']['text']
            return {"response": text}
        except (KeyError, IndexError):
            raise Exception("Nieoczekiwana struktura odpowiedzi API")
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
