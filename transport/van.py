from transport.vehicle import Vehicle

class Van(Vehicle):
    #конструктор класса, который инициализирует объект фургона
    def __init__(self, capacity: float, is_refrigerated: bool):
         #вызов конструкторва род класса
        super().__init__(capacity)
        self.is_refrigerated = is_refrigerated

    def __str__(self):
        #с флага is_refrigerated, определяем есть ли холодильник
        refrigerated_status = "С холодильником" if self.is_refrigerated else "Без холодильника"
        return super().__str__() + f", Статус: {refrigerated_status}"
