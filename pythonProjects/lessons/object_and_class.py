class Hous:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if not  isinstance(new_floor, int) or new_floor < 1 or new_floor > self.number_of_floor:
            print('такой этаж не существует')
        else:
            for i in range(1, new_floor):
                print(i)

zhuk = Hous('Zhukovsky', 10)
zhuk.go_to(9)