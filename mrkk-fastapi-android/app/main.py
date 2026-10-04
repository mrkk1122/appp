from fastapi import FastAPI

app = FastAPI(title="MRKK Android FastAPI Server", version="1.0.0")

@app.get("/")
def root():
    return {"status": "online", "message": "FastAPI is running on Android"}

@app.get("/health")
def health():
    return {"ok": True}
