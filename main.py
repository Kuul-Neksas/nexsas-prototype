from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid, datetime, json

app = FastAPI(title="Neksəs Prototype API")

class CompanyData(BaseModel):
    company_name: str
    vat_number: str
    email: str
    selected_psp: List[str]

@app.get("/")
def home():
    return {"message": "Benvenuto in Neksəs Prototype API"}

@app.post("/activate")
async def activate(data: CompanyData):
    contract_id = str(uuid.uuid4())
    timestamp = datetime.datetime.utcnow().isoformat()

    smart_contract = {
        "contract_id": contract_id,
        "company_name": data.company_name,
        "vat_number": data.vat_number,
        "email": data.email,
        "selected_psp": data.selected_psp,
        "timestamp": timestamp,
        "terms": "L’azienda autorizza il routing dei pagamenti tramite i PSP selezionati."
    }

    contract_file = f"contract_{contract_id}.json"
    with open(contract_file, "w") as f:
        json.dump(smart_contract, f, indent=2)

    for psp in data.selected_psp:
        print(f"Trasmissione sicura dati a PSP: {psp}")

    return {
        "status": "success",
        "message": "Contratto creato e inviato ai PSP selezionati.",
        "contract_id": contract_id
    }
