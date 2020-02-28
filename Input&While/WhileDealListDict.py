# # 在列表之间移动元素
# current_users = ["Wang", "Ren", "Yao", "trump", "Jerry", "Randy orton"]
# new_users = ["Tom", "TruMp", "mickey", "Minnie", "Randy Orton"]
# ## 直接将new_users 里的元素全部添加到current_users 中
# while new_users:
#     movement = new_users.pop()
#     current_users.append(movement)
# ### 检查
# print(new_users)
# print(current_users)

# # 删除包含特定值的列表元素（查找并删除）
# pets = ["dog", "cat", "goldfish", "dog", "rabbit", "cat", "snick"]
# ## 笨方法：逐一删除
# # pets.remove("cat") ## 只能删除掉第一次出现的内容，直接返回了，后面的不再遍历
# # print(pets)
# ## 循环删除
# while "cat" in pets:
#     pets.remove("cat")
# print(pets)
# # 回顾一下如何查重
# ## 集合化
# pets = set(pets)
# print(pets)
# pets = list(pets)
# print(pets)

# 用户输入来填充字典
## 先新建一空字典
residents = {}
## 设置控制变量
finish = True
while finish:
    ## 接收住户及其用水量
    resident = input("请输入住户姓名：")
    volume = input(resident+"的当月用水量：")
    volume = float(volume)
    ## 将住户和用水量关联保存到字典中
    residents[resident] = volume
    ctrl = input("是否统计输入完成，1 完成 2 继续统计")
    if ctrl == "1":
        finish = False
        print("统计完成！")
    else:
        print(resident+"用水量为"+str(volume)+"统计完成!\n请继续统计")
        continue
print(residents)