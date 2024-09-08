print()
print('Задача "Магические здания"')
print('----------')
print()

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(' Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
        print()

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

first = House('ЖК Горский', 20)
second = House('Домик в деревне', 3)

# __str__
print(first)
print(second)

# __len__
print()
print(len(first))
print(len(second))

print('----------')