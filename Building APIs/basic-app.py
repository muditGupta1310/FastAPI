from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class = HTMLResponse)
def home():
    HTML_Content = """
    <html>
    <body>
        <h1>Hello</h1>
    </body>
    </html>"""
    
    return HTML_Content


