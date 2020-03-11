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