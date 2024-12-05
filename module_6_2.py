class Vehicle:
    __COLOR_VARIANTS = ["white", "black", "grey", "red", "blue"]
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f'Модель: {self.__model} \nМощность двигателя: {self.__engine_power} '
              f'\nЦвет: {self.__color} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        reg_color = (color.lower() for color in self.__COLOR_VARIANTS)
        if new_color.lower() in reg_color:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', '500', "blue")
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
