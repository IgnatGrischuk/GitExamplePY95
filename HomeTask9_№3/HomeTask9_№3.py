class Car:

    def __init__(self, car_type, year, color):
        self.type = car_type
        self.year = year
        self.color = color
        self.engine_status = False  # Изначально двигатель не заведен

    def start_engine(self):
        if not self.engine_status:
            print('The engine is started.')
            self.engine_status = True
        else:
            print('The engine is already started.')

    def stop_engine(self):
        if self.engine_status:
            print('The engine is shut down')
            self.engine_status = False
        else:
            print('The engine is already shut down.')

    def set_type(self, new_type):
        self.type = new_type

    def set_year(self, new_year):
        self.year = new_year

    def set_color(self, new_color):
        self.color = new_color


#  Пример использования класса Car

my_car = Car(car_type='Hatchback', year=2012, color='Black')
print(f"Car type: {my_car.type}\nYear of manufacture: {my_car.year}\n"
      f"Color: {my_car.color}")

my_car.start_engine()
my_car.stop_engine()


my_car.set_type('Jeep')
my_car.set_year('2023')
my_car.set_color('Purple')

print(f"New parameters - Car type: {my_car.type}\nYear of manufacture:"
      f"{my_car.year}\nColor: {my_car.color}")
