year = input('请输入年份：')
if len(year) != 4:
    print('输入错误')
else:
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, '是闰年')
    else:
        print(year, '不是闰年')
