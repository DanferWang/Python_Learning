# 返回值
## return 语句
## 返回简单的值
# def name(lastname, firstname):
#     fullname = lastname.title() + " " + firstname.title()
#     return fullname
#
#
# name1 = name("wang", "haochen")
# name2 = name(1, 2)
# print(name1)
# print(name2)


## 让实参变成可选的
### solution: 默认实参+if判断
def name(lastname, firstname, middlename=""):
    if middlename:
        fullname = lastname + " " + middlename + " " + firstname
    else:
        fullname = lastname + " " + firstname
    return fullname.title()


# name3 = name("wang","haochen")
# name4 = name("wang","haochen","danfer")
# print(name3)
# print(name4)

## 返回字典
# def born(first, last, age, middle=""):
#     ## 定义字典
#     person = {
#         "name": name(last, first, middle),  ## 函数间也是可以调用的
#         "age": age
#     }
#     return person


# name5 = born("haochen", "wang", 22, "danfer")
# name6 = born("haochen", "wang", 22)
# print(name5)
# print(name6)

## 函数与while
### 函数可以和任何之前学过的代码逻辑和控制结构结合使用，实际上，函数的定义（def）就是一个小的py文件
def greet(name):
    '''这个函数的功能'''
    print("good morning " + name + "!")

while True:
    last = input("your lastname:")
    first = input("your firstname:")
    middlename = input("your middlename:")
    fullname = name(last,first,middlename)
    greet(fullname)
    ctrl = input("input q to quit!")
    if ctrl == "q":
        break