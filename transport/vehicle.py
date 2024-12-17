from uuid import uuid4  # для генерации уникального идентификатора
from transport import func

class Vehicle:
    def __init__(self, capacity: int):
        self.vehicle_id = self.generate_vehicle_id()  # генерируем ID транспорта
        self.capacity = capacity  # грузоподъёмность
        self.current_load = 0  # текущая загрузка
        self.clients_list = []  # список клиентов чьи грузы загружены
        # здесь добавляем информацию в список
        info = {'id': self.vehicle_id, 'capacity': self.capacity, 'current_load': 0, 'client_list': self.clients_list}
        func.add_to_transport_list(info)

    def generate_vehicle_id(self):
        # Метод для генерации уникального идентификатора транспортного средства
        return str(uuid4())

    def load_cargo(self, client):
        # функция для загрузки груза на транспортное средство
        self.current_load += client.cargo_weight

    def __str__(self):
        data = f"id: {self.vehicle_id}\nгрузоподъемность: {self.capacity}\nТекущая загрузка: {self.current_load}"
        return data
