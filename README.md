# Neksəs Prototype API

Un prototipo in **FastAPI** per gestire l'attivazione del servizio Neksəs.
Permette di inserire i dati aziendali, scegliere i PSP e generare un contratto digitale JSON.

## Deploy su Render
1. Scarica questa cartella e caricala su un tuo repository GitHub.
2. Vai su [Render](https://render.com), crea un nuovo servizio web.
3. Collega il repo GitHub.
4. Imposta come **Start Command**:
   ```
   uvicorn main:app --host=0.0.0.0 --port=10000
   ```
5. Dopo il deploy avrai un endpoint tipo:
   ```
   https://nexsas-prototype.onrender.com/activate
   ```

Ora puoi collegarlo al pulsante *Attivalo Subito* nel sito Canva.
