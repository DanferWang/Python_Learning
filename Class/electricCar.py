import car
import battery

class ElectricCar(car.Car):  ## 让py知道，我们要开始继承了
    ## 括号里是父类的名称
    def __init__(self, factory, model, year, price,battery_size):
        ## 接收（继承）父类的属性
        super().__init__(factory, model, year, price)
        ## super函数，将父类和子类关联起来 来源于superclass
        self.charger = "GB"
        self.battery_size = battery_size
        ## 类中类
        ## battery 以类的方式作为ElectricCar的属性（OOP）
        self.battery = battery.Battery(self.battery_size)


    def show_charger(self):
        print(self.charger)

    def show_gas_tank(self): ## 覆盖重写时，方法名和父类的一样，即可重写
        print("Electirc car do not have gas tank!")