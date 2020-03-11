class User():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.dsp = ""
        self.log = 0

    def set_dsp(self):
        msg = input("please input your description:")
        self.dsp = msg

    def read_dsp(self):
        print("User "+self.name+" description:")
        print(self.dsp)

    def greet(self):
        print("good morning " + self.name)

    def login(self):
        self.log += 1

    def reset(self):
        self.log = 0

tom = User("Tom",5,"male")
tom.greet()
tom.set_dsp()
tom.read_dsp()

tom.login()
tom.login()
tom.login()
tom.name = "Tom's father"
tom.greet()
print(tom.log)
tom.reset()
print(tom.log)