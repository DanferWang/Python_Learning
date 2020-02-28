# exercise: 物业水电费阶梯式管理系统
#   1、自来水费计费规则(前闭后开)：月使用水量小于3吨，自来水单价2.25元/吨；用水量在3~10吨，该部分自来水单价3.15元/吨；
#     用水量在10~15吨，该部分自来水单价4.00元/吨；超过15吨部分，单价为4.95元/吨；
#   2、系统化管理系统，应该是循环执行，根据需求（用户查询、物业结算）计算每一个用户需缴费；
#   3、使用布尔变量active作为控制变量；
#   4、在各种模式下，当用户输入‘quit’时退出系统；
#   5、模块化
#   6、加第4个功能选项：查询任一一户的应缴水费
## 物业词典：住户姓名：用水量、应缴水费
### {
#    wang:{
#       volume:16
#       total:53.75
#    }
# }

### {
#       ip1:[16:00,16:30]
#       ip2:[8:00,:9:26,:9:37]
#       }
## 对于物业结算：首先收集住户姓名、用水量；其次计算每一户应缴水费；更新物业词典

active = True
residents = {}
fees = {}
while active:
    msg = input("输入1 用户查询\n输入2 物业结算\n输入3 查看物业结算结果\n输入4 查询特定用户水费\n输入quit退出该系统")
    if msg == "quit":
        active = False
        print("感谢您的使用！")
    elif msg == "1":
        volume = input("请输入您当月的用水量： 输入back 返回模式选择  输入quit退出系统")
        if volume == "quit":
            print("感谢您的使用！")
            active = False  ## break
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
                total = 3 * 2.25 + 7 * 3.15 + 5 * 4.00 + (volume - 15) * 4.95
            print("您当月应缴纳水费为：" + str(total))
    elif msg == "2":
        # 接收并储存用户用水量
        ## 设置控制变量
        finish = True
        while finish:
            ## 接收住户及其用水量
            resident = input("请输入住户姓名：")
            volume = input(resident + "的当月用水量：")
            volume = float(volume)
            ## 将住户和用水量关联保存到字典中
            residents[resident] = volume
            ctrl = input("是否统计输入完成，1 完成 2 继续统计")
            if ctrl == "1":
                finish = False
                print("统计完成！")
            else:
                print(resident + "用水量为" + str(volume) + "统计完成!\n请继续统计")
                continue
        print("原始统计数据：")
        print(residents)
        # 调用字典数据，完成水费计算
        ## 再新建一个二级字典
        for resident in residents.keys():
            volume = residents[resident]
            volume = float(volume)
            total = 0
            if volume < 3:
                total = volume * 2.25
            elif volume < 10:
                total = 3 * 2.25 + (volume - 3) * 3.15
            elif volume < 15:
                total = 3 * 2.25 + 7 * 3.15 + (volume - 10) * 4.00
            else:
                total = 3 * 2.25 + 7 * 3.15 + 5 * 4.00 + (volume - 15) * 4.95
            fees[resident] = {
                "volume":volume,
                "fee":round(total,2)
            }
        print("物业结算完成")
    elif msg == "3":
        print("物业结算结果为：")
        print(fees)
    elif msg == "4":
        print("developing")
        # 若fees为空 报错
        # 若非空，接收输入住户
        ## 在fees中查询
        ## 输出fee域的值
        ## 如查询不到。。。
        ## 输入quit退出
    else:
        print("输入错误，请重新输入！")
