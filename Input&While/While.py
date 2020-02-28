# while 不必要迭代器，只需要一个控制条件
## 数星星
# current_num = 1 ## 从1开始数
# while current_num <= 29: ## 数到29睡着了
#     print(current_num)
#     current_num += 1
# print("爷睡了")

## 鹦鹉学舌.py
# print("我是鹦鹉，你来教我说话：\n 输入'quit'把我关闭")
# msg = "" ## 为了有控制条件的变量，应该先定义空字符串，否则，循环条件无法定义
# while msg != "quit": ## while 是一个控制结构，在while后面不能赋值和定义
#     msg = input()
#     if msg == "quit":
#         print("fuck！")
#     else:
#         print(msg)

## 状态变量
### 布尔型：True、False
# active = True
# print("我是鹦鹉，你来教我说话：\n 输入'quit'把我关闭")
# while active:
#     msg = input()
#     if msg == "quit":
#         active = False
#         print("fuck！")
#     else:
#         print(msg)

# break语句（外停）
## break 是从整个while中出去，不在循环
# print("赵子良睡着了。。。")
# while True:
#     status = input("0:郭戈没来；1：郭戈来了")
#     status = int(status)
#     if status == 0:
#         print("fuck 郭戈")
#     else:
#         print("哦啊，我就是兰迪奥顿")
#         break


# continue 语句（内停）
## continue 是返回到while开头，重新循环
## 测试条件表达式千万不能使True，除非你想让她一直数下去
# current_num = 1  ## 从1开始数
# while current_num <= 30:  ## 数到29睡着了
#     current_num += 1
#     if current_num % 3 == 0:
#         print(current_num)
#     else:
#         continue
# print("爷睡了")


# 避免无限循环
## 炸屏的例子（小朋友不要轻易模仿）
# current_num = 1 ## 从1开始数
# while current_num <= 29: ## 数到29睡着了
#     print(current_num)
#     # current_num += 1
# print("爷睡了")


# exercise: 物业水电费阶梯式管理系统
#   1、自来水费计费规则(前闭后开)：月使用水量小于3吨，自来水单价2.25元/吨；用水量在3~10吨，该部分自来水单价3.15元/吨；
#     用水量在10~15吨，该部分自来水单价4.00元/吨；超过15吨部分，单价为4.95元/吨；
#   2、系统化管理系统，应该是循环执行，根据需求（用户查询、物业结算）计算每一个用户需缴费；
#   3、使用布尔变量active作为控制变量；
#   4、在各种模式下，当用户输入‘quit’时退出系统；


active = True
while active:
    mode = input("请选择管理模式：\n1 物业结算\n2 用户查询\n输入quit退出系统\n")
    if mode == "1":
        print("物业结算尚未开发\n")
    elif mode == "2":
        volume = input("请输入您当月的用水量 输入back返回模式选择 输入quit退出系统\n")
        if volume == "quit":
            print("感谢您的使用！")
            break
        elif volume == "back":
            continue
        else:
            volume = float(volume)
            total = 0
            if volume < 3:
                total = volume * 2.25
            elif volume < 10:
                total = 3 * 2.25 + (volume - 3) * 3.15
            elif volume < 15:
                total = 3 * 2.25 + 7 * 3.15 + (volume - 10) * 4.00
            else:
                total = 3 * 2.25 + 7 * 3.15 + 5 * 4 + (volume - 15) * 4.95
            print("您当月的水费为:" + str(total))
    elif mode == "quit":
        print("感谢您的使用！")
        active = False
    else:
        print("您的模式选择有误！请重新输入\n")
