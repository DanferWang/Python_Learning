# input()接收字符串
# age = input("please input your age:")
## 执行了三步操作：
# 1、打印input函数中字符串参量；
# 2、使程序暂停运行；
# 3、接收用户从控制台的输入，默认以字符串的类型存在指定变量中

## 注重编程的设计感和用户交互体验
# msg = "we are gethering personal infomation."
# msg += "\nwhat is your first name?"  ## 扩展符 \n=nextline \t=tab
#
# first_name = input(msg)
# print("your first name is " + first_name)

# int()转化为整型
# print("please calculate : 4+3*6=?")
# answer = int(input()) ## 将字符串转化为整型
# if answer == 4+3*6:
#     print("you are right!")
# else:
#     print("you are wrong!!")
#
# #float()转化为小数
# print("please calculate : 4.5+3*6=?")
# answer =float(input()) ## 将字符串转化为浮点型
# if answer == 4.5+3*6:
#     print("you are right!")
# else:
#     print("you are wrong!!")
#
# # 判断是否为润年.py
year = input('请输入年份：')

if len(year) != 4:
    print('输入错误')
else:
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, '是闰年')
    else:
        print(year, '不是闰年')

# # 来进制转换 base=基数、进制
# age_int = int(age,16)
# print(age_int)