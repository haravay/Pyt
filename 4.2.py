class Airline:
    def __init__(self, destination, flight_number, aircraft_type, departure_time, weekdays):
        self.destination = destination
        self.flight_number = flight_number
        self.aircraft_type = aircraft_type
        self.departure_time = departure_time
        self.weekdays = weekdays

flight_list = [
    Airline("Нью-Йорк", "АА123", "Boeing 747", "14:30", ["Понедельник", "Среда", "Пятница"]),
    Airline("Лондон", "BA456", "Airbus A320", "09:45", ["Вторник", "Четверг"]),
    Airline("Париж", "АF789", "Boeing 777", "18:15", ["Суббота"]),
    Airline("Токио", "JL012", "Boeing 787", "22:00", ["Воскресенье"]),
]
destination = "Париж"
flights_to_destination = [flight for flight in flight_list if flight.destination == destination]
print(f"Рейсы в направлении {destination}:")
for flight in flights_to_destination:
    print(f"Номер рейса: {flight.flight_number}, Время вылета:{flight.departure_time}")

weekday = "Вторник"
flights_on_weekday = [flight for flight in flight_list if weekday in flight.weekdays]
print(f"\nРейсы в день недели {weekday}:")
for flight in flights_on_weekday:
    print(f"Номер рейса: {flight.flight_number}, Пункт назначения: {flight.destination}, Время вылета: {flight.departure_time}")
