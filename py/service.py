from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate_price():
    # Эмуляция расчета стоимости бронирования
    return {
        "hotel": "Grand Hotel",
        "room_type": "Standard",
        "check_in": "2024-12-01",
        "check_out": "2024-12-03",
        "nights": 2,
        "total_price": 11000,
        "currency": "RUB"
    }
