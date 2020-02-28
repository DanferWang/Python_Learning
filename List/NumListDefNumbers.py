# 创建
## 简单粗暴，一个个输入
# numbers_sim = [1, 2, 3]
# print(numbers_sim)
# ##　列表内部元素没有一致性
# temp = [numbers_sim, "numbers_sim", 1, 2, 3]
# print(temp)

## 利用range 函数、list 函数
# for value in range(1, 6):  ## 绝大多数的范围，默认都是前闭后开，默认步长为1
#     print(value)
# numbers_lr = list(range(1, 6))  # 与str() int()类似
# print(numbers_lr)
# for value in range(6):  ## range后参数只有一个stop，就是从0开始，几个数，步长为1
#     print(value)
# for value in range(1,12,2):  ## range后参数有三个start、stop、stride，就是从几开始，在几前停，步长为几
#     print(value)

## 在创建数值列表时，可以利用append方法，结合for循环，做更复杂的逻辑创建
## 结合append添加与for循环逻辑体
# 生成1~10的平方的列表
# squares = []
# for square in range(1, 11): ## square在py内部，是一个iterable，迭代器，他的数据结构（形势）必须和in后面的返回值是一致的
#     squares.append(square ** 2)
# print(squares)

#执行简单内部函数，常用在统计中
# digits = list(range(0,10))
# print(digits)
# ## py内部有几个集成好的函数
# print(min(digits))
# print(max(digits))
# print(sum(digits))

#解析式创建
squares1 = [value ** 2 for value in range(1,11)] ## 解析式有点像：(y=)ax+b(0<b<11)
print(squares1)

