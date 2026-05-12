import os
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.environ.get('NASA_API_KEY', 'DEMO_KEY')
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    try:
        response = requests.get(url )
        # Se a NASA der erro (como o 429), vamos tratar aqui
        if response.status_code != 200:
            return f"<h1>NASA em manutenção</h1><p>A API retornou erro {response.status_code}. Tente novamente em alguns minutos.</p>"
            
        data = response.json()
        html = f'''
        <html>
            <body style="text-align: center; font-family: Arial; background-color: #1a1a1a; color: white; padding: 50px;">
                <h1>{data.get('title', 'Foto do Dia')}</h1>
                <img src="{data.get('url', '')}" style="max-width: 80%; border-radius: 15px;">
                <p style="max-width: 800px; margin: 20px auto;">{data.get('explanation', '')}</p>
            </body>
        </html>
        '''
        return render_template_string(html)
    except Exception as e:
        return f"Erro de conexão: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
