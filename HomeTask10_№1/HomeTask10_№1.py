class Goods:
    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    @staticmethod
    def __check_string(value, field_name):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError(f"{field_name} должно быть строкой из букв")
        return value

    @staticmethod
    def __check_integer(value, field_name):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"{field_name} должно быть положительным числом")
        return value

    def get_info(self):
        return self.__name

    def get_shop_info(self):
        return self.__shop

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__shop}," \
               f" Стоимость: {self.__price} руб."


class Storage:
    def __init__(self):
        self.__goods = []

    def add_goods(self, goods):
        self.__goods.append(goods)

    def get_info_by_index(self, index: int):
        try:
            goods = self.__goods[index]
            print(goods)
        except IndexError:
            print("Ошибка: Неверный индекс товара")

    def get_info_by_name(self, name):
        goods_found = [goods for goods in self.__goods if
                       goods.get_info() == name]
        if goods_found:
            for goods in goods_found:
                print(goods)
        else:
            print(f"Товар с названием '{name}' не найден")

    def sort_by_name(self):
        self.__goods.sort(key=lambda goods: goods.get_info())

    def sort_by_shop(self):
        self.__goods.sort(key=lambda goods: goods.get_shop_info())

    def sort_by_price(self):
        self.__goods.sort(key=lambda goods: goods.get_price())

    def __add__(self, other_storage):
        new_storage = Storage()
        new_storage.__goods = self.__goods + other_storage.__goods
        return new_storage


storage = Storage()

goods_one = Goods('Ноутбук', 'Электроника', 2999.99)
goods_two = Goods('Холодильник', 'Бытовая техника', 2700)
goods_three = Goods('Мобильный телефон', 'Электроника', 2555.99)

storage.add_goods(goods_one)
storage.add_goods(goods_two)
storage.add_goods(goods_three)

while True:
    print("\n1. Вывести информацию о товаре по индексу")
    print("2. Вывести информацию о товаре по названию")
    print("3. Сортировка по названию")
    print("4. Сортировка по магазину")
    print("5. Сортировка по цене")
    print("6. Объединение складов по цене")
    print("0. Выход")

    choise = input('Выберите действие: ')

    if choise == '1':
        index = int(input('Введите индекс товара: '))
        storage.get_info_by_index(index)
    elif choise == '2':
        name = input('Введите название товара: ')
        storage.get_info_by_name(name)
    elif choise == '3':
        storage.sort_by_name()
        print("Склад отсортирован по названию.")
    elif choise == '4':
        storage.sort_by_shop()
        print("Склад отсортирован по магазину.")
    elif choise == '5':
        storage.sort_by_price()
        print("Склад отсортирован по цене.")
    elif choise == '6':
        storage_two = Storage()
        goods_four = Goods('Наушники', 'Электроника', 3550.55)
        storage_two.add_goods(goods_four)
        consolidated_storage = storage + storage_two
        print("Склады объединены.")
    elif choise == '0':
        break
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
