class Car():
    def __init__(self, factory, model, year, price):
        self.model = model
        self.factory = factory
        self.year = year
        self.price = price
        self.odo = 0

    def info(self):
        detail_info = self.factory + " " + self.model + " produced in " + \
                      str(self.year) + " as " + str(self.price)
        print(detail_info)

    def read_odo(self):
        print("this car has run " + str(self.odo))

    def update_odo(self,km):
        if km < 0:
            print("you cannot roll back odo!")
        else:
            self.odo += km

    def set_odo(self,km):
        self.odo = km


new_car = Car("Tesla", "Model Y", 2020, 420000)

new_car.info()

## 给属性指定默认值
# new_car.read_odo()

## 更新或修改属性的值
### 直接修改(赋值）
new_car.odo =  20000
new_car.read_odo()

### 通过方法修改
new_car.update_odo(10000)
new_car.read_odo()
new_car.update_odo(-20000)
new_car.set_odo(-20000)
new_car.read_odo()