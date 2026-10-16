// Инициализация БД: создание коллекции и добавление тестовых данных
print("Initializing MongoDB...");

db = db.getSiblingDB("hotel_db");

// Создаем коллекцию, если нет
if (!db.rooms.findOne()) {
    db.rooms.insertMany([
        { room_id: "101", type: "Standard", price: 5000 },
        { room_id: "102", type: "Suite", price: 12000 },
        { room_id: "103", type: "Deluxe", price: 7500 }
    ]);
    print("Test data inserted.");
} else {
    print("Data already exists.");
}
