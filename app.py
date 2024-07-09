from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from sentiment_analysis import analyze_sentiment  # Importer la fonction depuis le fichier séparé

app = FastAPI()

# Dossier pour les templates
templates = Jinja2Templates(directory="templates")


# Page HTML principale
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

# Route pour traiter le formulaire
@app.post("/", response_class=HTMLResponse)
async def post_form(request: Request, text: str = Form(...)):
    result = analyze_sentiment(text)  # Utiliser la fonction importée
    return templates.TemplateResponse("form.html", {"request": request, "result": result, "text": text})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
