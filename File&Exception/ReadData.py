## txt\csv\json\xls
# 读取文件
## 读取整个文件
# with open("pi.txt") as file: ## 首先要打开文件，将其创建一个对象
#     ##　open只在with的代码块内打开文件
#     ## python会知道，在用户不需要文件的时候可以适时关闭
#     contents = file.read() ## read读取文件的全部内容，做为字符串赋值给contents
#     print(contents.rstrip())

## 逐行读取
# file_name = "pi.txt"
#
# with open(file_name) as file:
#     for line in file:
#         print(line.strip())

## 创建包含文件各行内容的列表
# file_name = "pi.txt"
#
# with open(file_name) as file:
#     lines = file.readlines() ## 一行一行读，并且每行默认存在一个列表中
#
# print(lines)
# for line in lines:
#     print(line)


## 使用文件内容
### 把pi拼接起来
# file_name = "pi.txt"
# #### 首先打开文件
# with open(file_name) as file:
#     #### 其次按行读文件
#     lines = file.readlines()
#     #### 再来创建一个空字符串，用来保存拼接结果
#     pi_string = ""
#     #### 遍历按行存的2列表，循环拼接
#     for line in lines:
#         pi_string += line.strip()
#
# print(float(pi_string))
# print(len(pi_string))


## 处理大型文件，以一百万位的pi为例
file_name = "pi_million_digits.txt"

### 数据预处理
with open(file_name) as file:
    pi = ""
    for line in file.readlines():
        pi += line.strip()
# print(len(pi))
# print(pi)

### 数据操作
birth = input("input your birthday:")
if birth in pi:
    print(birth + " is in pi")
else:
    print("fuck")