# 定义函数
## def 出来函数
# def greet():
#     '''这个函数的功能'''
#     print("good morning!")
#
#
# ## 调用该函数
# greet()


# def greet_name(name): # name  形式参数:接收函数所需要的信息
#     print("good morning " + name)
#
# greet_name("Wang") # 实际参数，传参（verb）：“wang”传递给name，说白了就是给name赋值
# greet_name("Ren")
# greet_name("Yao")

# 传递实参
## 位置实参
### 实参顺序与形参顺序相同
def pets(category, name):
    print("i have a " + category + " whose name is " + name)


### 实参的顺序非常重要！！！
# pets("cat", "Be rich")
# pets("Be rich", "cat")
# pets("dog", "Trump")

## 关键字实参
### 每个实参都是由变量名和值组成
### 形参与实参的对应关系已经明确确定，顺序无关紧要
pets(category="pig", name="Hengheng")
## 默认值
### 可以简化函数调用，还可以指出函数最典型的使用场景
# def pet_default(name,type="dog"): ## 设置为默认值的形参，必须放在参数列表的最后,
#                                 ##   为了py的安全性，防止调用函数时缺少参数
#     print("i have a " + type + " whose name is " + name)
#
# # 等效函数调用
# pet_default("Zaizai")## 依然认为其是位置实参
# pet_default("Be rich","cat")
# pet_default(category="pig",name="Hengheng")

# 避免参数错误
## 实参参数列表与形参参数列表数目冲突
# pets()
## 实参和形参的类型冲突
pets(1, 2)
