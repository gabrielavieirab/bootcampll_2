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

if __name__ == "__main__":
    # O Render passa a porta pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
