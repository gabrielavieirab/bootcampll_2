import requests
import os
from dotenv import load_dotenv

load_dotenv()

class NasaClient:
    def __init__(self):
        self.api_key = os.getenv('NASA_API_KEY', 'DEMO_KEY')
        self.base_url = 'https://api.nasa.gov/planetary/apod'

    def get_daily_picture(self ):
        params = {'api_key': self.api_key}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro na NASA: {response.status_code}")

if __name__ == "__main__":
    client = NasaClient()
    data = client.get_daily_picture()
    print(f"Título: {data.get('title')}")
    print(f"Link: {data.get('url')}")
