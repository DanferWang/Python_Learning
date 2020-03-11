## OOP: object-oreitialed programming
## 实例化：根据类创建对象
# 创建类
## 创造对象 + 定义方法
class Dog():  ## 为了区别，我们默认类的首字母大写
    def __init__(self, name, age):  ## 每次实例化，python都会自动的运行这个__init__方法
        ## self必不可少,指向实例本身的引用
        self.name = name
        self.age = age
        ## 以self为前缀的变量都可供类中的所有方法使用
        ## 属性：通过实例访问的变量

    def sit(self):
        print(self.name + " is now sitting!")

    def wangwang(self):
        for i in range(self.age):
            print("wang!")


# 使用类
## 将类实例化
my_dog = Dog("trump", 6)

## 访问属性
print("my dog's name is " + my_dog.name)
print("his age is " + str(my_dog.age))
## 调用方法
my_dog.sit()
my_dog.wangwang()

## 多个实例化
your_dog = Dog("zhangsan", 8)
her_dog = Dog("lisi", 7)
her_dog.sit()
your_dog.wangwang()