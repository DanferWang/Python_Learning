# if判断
## 字符串
cars = ["bmw", "benz", "audi","toyota","ford"]
# for car in cars:
#     if car ==  "bmw":## 模式匹配初级阶段 条件测试表达式
#         print(car.upper())
#     else:
#         print(car.title())
# Python 是大小写敏感的lang

# for car in cars:
#     if car !=  "bmw":## 模式匹配初级阶段 条件测试表达式
#         print(car.title())
#     else:
#         print(car.upper())

## 比较数字
### 一个比较底层的例子
# age = 18
# print(age == 18)

## 口算.py
# print("please calculate : 4+3*6=?")
# answer = int(input())
# if answer == 4+3*6:
#     print("you are right!")
# else:
#     print("you are wrong!!")

## 适婚年龄.py
# print("male,female:")
# age1 = int(input())
# age2 = int(input())
# if age1 > 22 and age2 > 20:
#     print("fuck off!")
# else:
#     print("get out!")

## 结婚性别.py
# print("sex1,sex2:")
# sex1 = input()
# sex2 = input()
# if (sex1 == "male" and sex2 == "male") or (sex1 == "female" and sex2 == "female"):
#     print("get out!")
# else:
#     print("fuck off!")

## 检查列表中是否存在某元素
### in 语句
### in 相当于 == not in 相当于 ！=
# res = "audi" not in cars
# print(res)

## 布尔变量
### 取值只能是True（1） False（0）
## 开关灯.py
print("你是想开灯（1）还是想关灯（0）？")
wish = bool(int(input())) ## bool 变量只能接收int型
if wish == True:
    print("灯亮了")
else:
    print("灯关了")