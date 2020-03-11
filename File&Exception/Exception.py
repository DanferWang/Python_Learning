## python 为我们提供了一个面临错误时尝试解决该错误的特殊对象：异常（exception）
## 具体实现是通过try-except代码块实现

# ZeroDivisionError
## 除以0异常
# try: ## while True:
#     print(5/0)
# except ZeroDivisionError: ## if try的代码块报了除0的错，则执行
#     print("除数不能为0")

## 通过异常防止崩溃
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# FileNotFoundError
file_name = "123.txt"
try:
    with open(file_name) as file:
        file.readlines()
except FileNotFoundError:
    print("这个文件不存在")
