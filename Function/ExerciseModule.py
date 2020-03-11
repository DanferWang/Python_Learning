# exercise: 模块化 物业水电费阶梯式管理系统
#   1、在原有物业系统之上，利用原有代码，定义函数：计费函数、功能函数（用户查询函数、物业结算函数、
#       查看物业结算结果函数、查询特定用户水费函数）、退出函数等，以简化高层逻辑，方便阅读优化
#   2、将定义的函数封装在一个.py库中
#   3、用import包调用函数，重构物业系统
#   4、调试一下，看看能不能成功运行我们的业务逻辑

import waterfee



active = True
residents = {}
fees = {}
while active:
    msg = input("输入1 用户查询\n输入2 物业结算\n输入3 查看物业结算结果\n输入4 查询特定用户水费\n输入quit退出该系统")
    if msg == "quit":
        active = False
        print("感谢您的使用！")
    elif msg == "1":
        waterfee.userquary()
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
            total = waterfee.calculate(volume)
            fees[resident] = {
                "volume": volume,
                "fee": round(total, 2)
            }
        print("物业结算完成")
    elif msg == "3":
        print("物业结算结果为：")
        print(fees)
    elif msg == "4":
        # 若fees为空 报错
        if not fees:
            print("未开始统计住户信息！")
            continue
            # 若非空，接收输入住户
        else:
            name = input("请输入需要查询的住户姓名： 输入back 返回模式选择  输入quit退出系统")
            ## 输入quit退出
            if name == "quit":
                active = False
            elif name == "back":
                continue
            ## 在fees中查询
            ## 如查询不到。。。
            elif name not in fees.keys():
                print("您输入的用户不存在！")
                continue
            else:
                volume, fee = fees[name]['volume'], fees[name]['fee']
                ## 输出fee域的值
                print("住户" + name + "当月用水量为：" + str(volume) + "应缴水费：" + str(fee))

    else:
        print("输入错误，请重新输入！")
