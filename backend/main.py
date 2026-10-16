from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import httpx
import os

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://db:27017")
WEB_SERVICE_URL = os.getenv("WEB_SERVICE_URL", "http://web-service:8001")

client = MongoClient(MONGO_URI)
db = client["hotel_db"]
collection = db["rooms"]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
async def get_items():
    items = list(collection.find({}, {"_id": 0}))
    if not items:
        return {"message": "Нет данных в БД. Проверьте init.js."}
    return items

@app.get("/booking")
async def get_booking():
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{WEB_SERVICE_URL}/calculate", timeout=5.0)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Web-service error: {str(e)}")

# Инициализация тестовыми данными, если пусто (для надежности)
@app.on_event("startup")
async def startup_event():
    if collection.count_documents({}) == 0:
        test_data = [
            {"room_id": "101", "type": "Standard", "price": 5000},
            {"room_id": "102", "type": "Suite", "price": 12000}
        ]
        collection.insert_many(test_data)
