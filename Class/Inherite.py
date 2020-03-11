# 继承
## 自动获得被继承类（父类）的所有属性和方法
## 继承者类（子类）也可以定义自己的新属性和方法
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


## 通过父类继承子类，__init__
# class ElectricCar(Car): ## 让py知道，我们要开始继承了
#     ## 括号里是父类的名称
#     def __init__(self,factory, model, year, price):
#         ## 接收（继承）父类的属性
#         super().__init__(factory, model, year, price)
#         ## super函数，将父类和子类关联起来 来源于superclass
#
# my_tesla = ElectricCar("Tesla","Model 3","2020",299000)
# my_tesla.info()

## 给自类定义特有的属性和方法
# class ElectricCar(Car):  ## 让py知道，我们要开始继承了
#     ## 括号里是父类的名称
#     def __init__(self, factory, model, year, price, battery_size):
#         ## 接收（继承）父类的属性
#         super().__init__(factory, model, year, price)
#         ## super函数，将父类和子类关联起来 来源于superclass
#         self.battery_size = battery_size
#         self.charger = "GB"
#
#     def show_batter_size(self):
#         print(self.battery_size)
#
#     def show_charger(self):
#         print(self.charger)
# my_tesla = ElectricCar("Tesla","Model 3","2020",299000,"350")
# my_tesla.show_batter_size()
# my_tesla.show_charger()

## 覆盖、重写父类的方法
### 取其精华 弃其糟粕
# class ElectricCar(Car):  ## 让py知道，我们要开始继承了
#     ## 括号里是父类的名称
#     def __init__(self, factory, model, year, price, battery_size):
#         ## 接收（继承）父类的属性
#         super().__init__(factory, model, year, price)
#         ## super函数，将父类和子类关联起来 来源于superclass
#         self.battery_size = battery_size
#         self.charger = "GB"
#
#     def show_batter_size(self):
#         print(self.battery_size)
#
#     def show_charger(self):
#         print(self.charger)
#
#     def show_gas_tank(self): ## 覆盖重写时，方法名和父类的一样，即可重写
#         print("Electirc car do not have gas tank!")
#
#
# my_tesla = ElectricCar("Tesla", "Model 3", "2020", 299000, "350")
# my_tesla.show_gas_tank()

## 将其他类(实例化基础之上)用作属性
### 属性或方法过多时，可以把相同类别的内容独立打包成新的小类
class Battery():
    def __init__(self,battery_size):
        self.battery_size = battery_size

    def show_battery_size(self):
        print(self.battery_size)

    def show_range(self):
        if self.battery_size == 70:
            range = 350
            print("can run "+str(range))
        elif self.battery_size == 95:
            range = 560
            print("can run "+str(range))

class ElectricCar(Car):  ## 让py知道，我们要开始继承了
    ## 括号里是父类的名称
    def __init__(self, factory, model, year, price,battery_size):
        ## 接收（继承）父类的属性
        super().__init__(factory, model, year, price)
        ## super函数，将父类和子类关联起来 来源于superclass
        self.charger = "GB"
        self.battery_size = battery_size
        ## 类中类
        ## battery 以类的方式作为ElectricCar的属性（OOP）
        self.battery = Battery(self.battery_size)


    def show_charger(self):
        print(self.charger)

    def show_gas_tank(self): ## 覆盖重写时，方法名和父类的一样，即可重写
        print("Electirc car do not have gas tank!")

# my_tesla = ElectricCar("Tesla", "Model 3", "2020", 299000,95)
# my_tesla.show_gas_tank() ## 重写的
# my_tesla.info() ## 继承的
# my_tesla.show_charger() ## 新建的
# my_tesla.battery.show_battery_size() ## 调用其他类的
# my_tesla.battery.show_range()
