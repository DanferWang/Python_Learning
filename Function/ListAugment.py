# 传递列表
# def greet_name(names):  # name  形式参数:接收一个列表
#     ## 遍历使用列表中的元素
#     for name in names:
#         print("good morning " + name.title())
#
#
# baijiaxing = ["zhao", "qian", "sun", "li"]
# greet_name(baijiaxing)

## 在函数中修改列表(破坏性修改)
un3D = ["phonecase","cup","spoon"]
com3D = []
### 打印函数
def print3D(unprint,complished):
    while unprint:
        current = unprint.pop()
        print("printing: "+current)
        complished.append(current)

### 输出工作结果函数
def show3D(complisheds):
    print("the following models have been printed:")
    for complished in complisheds:
        print(complished)
    print("finish")

# print3D(un3D,com3D)
# show3D(com3D)
# print(un3D)

## 在函数中修改列表(建立副本修改)
### slice
print3D(un3D[:],com3D)
show3D(com3D)
print(un3D)