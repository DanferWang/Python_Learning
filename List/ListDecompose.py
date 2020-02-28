cars = ["bmw", "benz", "audi", "toyota", "ford"]
# 切片-slices
# ## 简化range函数变为切片slices
# print(cars[0:3]) # 前闭后开
# print(cars[1:5])
# print(cars[ :3])
# print(cars[-2: ])
# ## 切片，实际上就是两个索引夹出来的范围（前闭后开），中间用：连接

# 遍历操作
# for car in cars: ## 更新一下认识：for循环的控制部分，不一定是数字，是任何可以作为迭代的变量
#     print(car.upper())

# cars0 = [["bmw", "benz"],["toyota","ford"],["bmw", "benz","toyota","ford"]]
# for car1 in cars0:
#     for car2 in car1:
#         print(car2.upper())

# 利用切片复制(赋值)
# carsB = cars[:]
# print(carsB)
## 完全复制
carsB = cars
print(cars)