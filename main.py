import json
from transport.client import Client
from transport.van import Van
from transport.ship import Ship
from transport.transport_company import TransportCompany


# Функция для сохранения транспорта в transport.json
def save_transport_to_file(vehicles):
    transport_data = []
    
    for vehicle in vehicles:
        vehicle_info = {
            "id": vehicle.vehicle_id,
            "capacity": vehicle.capacity,
            "current_load": vehicle.current_load,
            "client_list": [client.name for client in vehicle.clients_list]  # Сохраняем только имена клиентов
        }
        transport_data.append(vehicle_info)

    with open('transport/transport.json', 'w', encoding='utf-8') as file:
        json.dump(transport_data, file, indent=4, ensure_ascii=False)

def list_vehicles():
    with open('transport/transport.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for vehicle in data:
            print(f"ID: {vehicle['id']}, Грузоподъемность: {vehicle['capacity']}, Загруженность: {vehicle['current_load']}")
# Функция для ввода данных клиента
def input_client():
    name = input("Введите имя клиента: ")
    cargo_weight = float(input("Введите вес груза клиента (в тоннах): "))
    is_vip = input("Есть ли у клиента VIP статус? (да/нет): ").strip().lower() == 'да'
    
    return Client(name, cargo_weight, is_vip)


# Функция для ввода данных транспортного средства с валидацией
def input_vehicle():
    vehicle_type = input("Введите тип транспортного средства (фургон/судно): ").strip().lower()
    capacity = float(input("Введите грузоподъемность транспортного средства (в тоннах): "))
    
    # Проверяем на корректность введенных данных
    if capacity <= 0:
        print("Ошибка: грузоподъемность должна быть положительным числом.")
        return None
    
    if vehicle_type == "фургон":
        is_refrigerated = input("Нужен ли холодильник? (да/нет): ").strip().lower() == 'да'
        return Van(capacity, is_refrigerated)
    elif vehicle_type == "судно":
        name = input("Введите название судна: ")
        return Ship(capacity, name)
    else:
        print("Некорректный тип транспортного средства.")
        return None

# Функция для проверки уникальности ID транспортного средства
def is_vehicle_id_unique(vehicle_id):
    with open('transport/transport.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for vehicle in data:
            if vehicle['id'] == vehicle_id:
                return False  # ID уже существует
    return True


# Функция для добавления транспортного средства в список
def add_vehicle_to_list(vehicle):
    with open('transport/transport.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if is_vehicle_id_unique(vehicle.vehicle_id):  # Проверяем уникальность ID
        new_vehicle = {
            "id": vehicle.vehicle_id,
            "capacity": vehicle.capacity,
            "current_load": vehicle.current_load,
            "client_list": [client.name for client in vehicle.clients_list]  # Сохраняем только имена клиентов
        }
        data.append(new_vehicle)
        
        with open('transport/transport.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Транспортное средство добавлено.")
    else:
        print("Ошибка: транспортное средство с таким ID уже существует.")


# Меню для взаимодействия с пользователем
def menu(company):
    while True:
        action = input("1 - Добавить клиента \n2 - Добавить транспорт\n3 - Распределить грузы \n4 - Вывести список транспорта \n5 - Выход\n")
        
        if action == '1':
            client = input_client()
            company.add_client(client)
            print(f"Клиент {client.name} добавлен.")
        
        elif action == '2':
            vehicle = input_vehicle()
            if vehicle:
                add_vehicle_to_list(vehicle)  # Добавляем транспортное средство в файл
            else:
                print("Ошибка при добавлении транспортного средства.")
                
        elif action == '3':
            company.optimize_cargo_distribution()
        
        elif action == '4':
            print("\nСписок всех транспортных средств:")
            list_vehicles()
        
        elif action == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Неверная команда, попробуйте снова.")


# Основная функция
def main():
    company_name = input("Введите название компании: ")
    company = TransportCompany(company_name)
    menu(company)


# Запуск программы
if __name__ == "__main__":
    main() 