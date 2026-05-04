import unittest
from nasa_integration import NasaClient

class TestNasaIntegration(unittest.TestCase):
    def test_api_connection(self):
        client = NasaClient()
        data = client.get_daily_picture()
        self.assertIn('title', data)
        print(f"\n[Teste OK] Título recebido: {data['title']}")

if __name__ == '__main__':
    unittest.main()
