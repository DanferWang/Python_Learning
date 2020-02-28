# 组织 大概就是 排序
# sort 方法：永久性排序
cars = ["bmw", "benz", "audi","toyota","ford"]
print(cars)
# cars.sort() # 他只是一步操作，没有返回值
# print(cars) # 字符串：alphabetic
# num = [99,58,12,60]
# num.sort()
# print(num)# 数字：从小到大
# num.sort(reverse=True) # reverse 参量默认为False，现在赋值为True 则倒置排序
# print(num)# 数字：从大到小

# sorted 方法：临时性排序
# new_cars = sorted(cars) #不能 cars.sorted   他是排序操作，并且返回排序结果，且不改变原来的列表顺序
# print(new_cars)
# print(cars)
# new_cars = sorted(cars,reverse=True)
# print(new_cars)

# 反转列表
# reverse 方法
# cars.reverse()
# print(cars)

#确定列表长度=元素个数
## pretty 常用
print(len(cars))