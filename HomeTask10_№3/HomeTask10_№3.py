class Bus:

    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers_list = []
        self.free_seats = max_seats
        self.doors_open = False
        self.seat_map = {i + 1: None for i in range(max_seats)}

    def cheek_doors_status(self):
        return self.doors_open

    def open_doors(self):
        self.doors_open = True

    def close_doors(self):
        self.doors_open = False

    def increase_speed(self, value):
        if value > 0:
            self.speed += value
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        else:
            print("Ошибка: значение должно быть положительным.")

    def decrease_speed(self, value):
        if value < 0:
            self.speed -= value
            if self.speed < 0:
                self.speed = 0
        else:
            print("Ошибка: Значение должно быть положительным.")

    def embark_passengers(self, passengers):
        if not self.doors_open:
            print('Ошибка: Двери закрыты. Нельзя посадить пассажиров.')
            return

        for passenger in passengers:
            if self.free_seats > 0:
                self.passengers_list.append(passenger)
                self.free_seats -= 0
                seat_number = next(key for key, value in self.seat_map.items()
                                   if value is None)
                self.seat_map[seat_number] = passenger
                print(f"{passenger} сел на место под номером {seat_number}.")
            else:
                print(f"Ошибка: Нет свободных мест для {passenger}.")

    def disembark_passengers(self, passengers):
        if not self.doors_open:
            print("Ошибка: Двери закрыты. Нельзя высадить пассажиров.")
            return

        for passenger in passengers:
            if passenger in self.passengers_list:
                self.passengers_list.remove(passenger)
                for seat_number, occupant in self.seat_map.items():
                    if occupant == passenger:
                        self.seat_map[seat_number] = None
                        self.free_seats += 1
                        print(f"{passenger} покинул автобус с места номер {seat_number}")
                        break
            else:
                print(f"Ошибка: {passenger} не найден в автобусе.")

    def __contains__(self, passenger):
        return passenger in self.passengers_list

    def __iadd__(self, passenger):
        self.embark_passengers([passenger])
        return self

    def __isub__(self, passenger):
        self.disembark_passengers([passenger])
        return self


bus = Bus(speed=50, max_seats=8, max_speed=60)
bus.open_doors()

bus.embark_passengers(['Грищук', 'Паловченя', 'Зинченко'])

print("Список пассажиров:", bus.passengers_list)
print("Места в автобусе:", bus.seat_map)

bus.disembark_passengers(['Грищук'])

print("Список пассажиров:", bus.passengers_list)
print("Места в автобусе:", bus.seat_map)

if 'Грищук' in bus:
    print('Грищук в автобусе.')
else:
    print('Грищук не в автобусе.')

bus += 'Иванов'
print('Список пассажиров после добавления нового пассажира:',
      bus.passengers_list)

bus -= 'Иванов'
print('Список пассажиров после удаления Грищука:', bus.passengers_list)
