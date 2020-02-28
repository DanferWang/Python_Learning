import os
# 元组Tuple， 实际上是特殊的列表，特殊在只有两个元素，特殊在表现方式
## 不可改变的列表
## 定义创建
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# # dimensions[0] = 100 # 元组的不可改变性

# 遍历
# for i in dimensions:
#     print(i)

# 如果非要修改元组内容，那就重新定义吧
dimensions = (100, 50)  ## 如果在C++中，前后定义同一个全局不可更改的变量，会报冲突（编译型语言）
print(dimensions)

