class Car():  ## 把他当作父类
    def __init__(self, factory, model, year, price):
        self.model = model
        self.factory = factory
        self.year = year
        self.price = price
        self.odo = 0
        self.tank = 700

    def info(self):
        detail_info = self.factory + " " + self.model + " produced in " + \
                      str(self.year) + " as " + str(self.price)
        print(detail_info)

    def read_odo(self):
        print("this car has run " + str(self.odo))

    def update_odo(self, km):
        if km < 0:
            print("you cannot roll back odo!")
        else:
            self.odo += km

    def set_odo(self, km):
        self.odo = km

    def show_gas_tank(self):
        print(self.tank)