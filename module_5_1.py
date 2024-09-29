class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


# Создание объекта класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)

# Вызов метода go_to с произвольным числом
h1.go_to(5)  # Выводит: 1, 2, 3, 4, 5

# Пример метода go_to вызова с несуществующим этажом
h2.go_to(10)  # Выводит: Такого этажа не существует

# Пример метода go_to вызова всех этажей
h3.go_to(30)  # Выводит: Все этажи