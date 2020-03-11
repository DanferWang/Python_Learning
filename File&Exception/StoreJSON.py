# JSON (JavaScript Ocject Notation)
## json 既是一种储存格式，也是一个py包，也是一种对象
import json

## 储存
# number = [2, 3, 5, 7, 11, 13]
#
# file_name = "prime.json"
#
# with open(file_name,"w") as json_file:
#     json.dump(number,json_file)


## 读取
# file_name = "prime.json"
#
# with open(file_name) as file:
#     read_prime = json.load(file) ##json.load() 只是定位到json对象，并且装载于内存，
#                                 ## 如果要调用，必须要将其赋值给某个变量
# print(read_prime)

## 保存和读取用户数据，举个例子
# file_name = "name.json"
# user = input("what's your name?")
# with open(file_name,"w") as file :
#     json.dump(user , file)

# file_name = "name.json"
# with open(file_name) as file:
#     username = json.load(file)
# print("hello " + username)

## 结构化的数据
# 表格、字典、有结构的

file_name = "prime.json"

with open(file_name) as json_file:
    file = json.load(json_file)
    for person,info in file.items():
        print(person)
        for detail in info.keys():
            print(detail+":"+info[detail])