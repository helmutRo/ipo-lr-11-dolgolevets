import json
class TransportCompany:
    def __init__(self, name: str):
        self.name = name
        self.clients = []  # Список клиентов
        self.vehicles = []  # Список транспортных средств

    def add_client(self, client):
        self.clients.append(client)
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def list_vehicles(self):
        return self.vehicles
    
    def optimize_cargo_distribution(self):
        # Сортируем клиентов: сначала VIP, потом обычные
        self.clients.sort(key=lambda client: client.is_vip, reverse=True)
        
        # Перебираем все транспортные средства
        for vehicle in self.vehicles:
            for client in self.clients:
                # Пытаемся загрузить транспортное средство
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:
                    vehicle.load_cargo(client)
                    vehicle.clients_list.append(client)
                    print(f"Груз клиента {client.name} загружен на транспортное средство {vehicle.vehicle_id}")
                    self.clients.remove(client)  # Убираем клиента из списка
                    break
            # Если список клиентов пуст, выходим из цикла
            if not self.clients:
                break
        
        if self.clients:
            print("Не все грузы удалось распределить, не хватает транспорта.")
        else:
            print("Все грузы успешно распределены по транспортным средствам.")
