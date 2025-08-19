from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Middleware CORS per test web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("form.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/register")
async def register(
    nome_azienda: str = Form(...),
    codice_fiscale: str = Form(...),
    partita_iva: str = Form(...),
    iban: str = Form(...),
    stripe: bool = Form(False),
    paypal: bool = Form(False),
    nexi: bool = Form(False),
    sumup: bool = Form(False),
    contract: bool = Form(...)
):
    return {
        "message": "Dati ricevuti",
        "azienda": nome_azienda,
        "cf": codice_fiscale,
        "iva": partita_iva,
        "iban": iban,
        "psp": {
            "stripe": stripe,
            "paypal": paypal,
            "nexi": nexi,
            "sumup": sumup
            "adyen": adyen
        },
        "contratto_accettato": contract
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
