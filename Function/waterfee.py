def calculate(volume):
    total = 0
    if volume < 3:
        total = volume * 2.25
    elif volume < 10:
        total = 3 * 2.25 + (volume - 3) * 3.15
    elif volume < 15:
        total = 3 * 2.25 + 7 * 3.15 + (volume - 10) * 4.00
    else:
        total = 3 * 2.25 + 7 * 3.15 + 5 * 4.00 + (volume - 15) * 4.95
    return total

def userquary():
    volume = input("请输入您当月的用水量： 输入back 返回模式选择  输入quit退出系统")
    if volume == "quit":
        print("感谢您的使用！")
        active = False  ## break
        return active
    elif volume == "back":
        return
    else:
        volume = float(volume)
        total = calculate(volume)
        print("您当月应缴纳水费为：" + str(total))