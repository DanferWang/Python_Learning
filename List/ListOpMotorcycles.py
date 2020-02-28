motorcycles = ["honda","kawasaki","yamaha","suzuki"]
print(motorcycles)
# # 修改
# motorcycles[1] = "ducati" #先访问 再覆盖
# print(motorcycles)

#添加/插入
#在C里，静态的，static 在py，是动态的，dynamic
# ## append 方法
# motorcycles.append("ducati") #appendix 附录
# print(motorcycles)
# ### 这样也可以新建列表
# moto = []
# moto.append("honda")
# moto.append("kawasaki")
# moto.append("yamaha")
# print(moto)

# ## insert 方法
# motorcycles.insert(2,"ducati") #insert 方法：插入添加的地方（在其前添加），所插入的对象
# print(motorcycles)

#删除
##永久性删除 del
# del motorcycles[1] # 错误的：motorcycles[1].del 不能对删除的对象进行操作
# print(motorcycles)

##保留性删除
# purchase = motorcycles.pop() # 被删除的元素依然能被访问，但是在列表中已经不存在了
# print(purchase)
# print(motorcycles)
# print(motorcycles.pop(1)) # pop 两部操作:1、访问该索引，并且作为返回值；2、把该对象从列表里删除
# print(motorcycles)

##查询性删除（识别） remove
# motorcycles.remove("kawasaki") # 干了两件事：1、根据内容查找对象；2、删除它
# print(motorcycles)

## 原来就有['honda', 'kawasaki', 'yamaha', 'suzuki']，来了一个新的“ducati”，
# 发现ducati是最便宜的，meanwhile“yamaha”最贵的，用“ducati”替换“yamaha”的销售位置，并打一个广告，
# “ducati is the newest and cheapest one!”.
motorcycles[2] = "ducati"
print(motorcycles)
print(motorcycles[2]+" is the newest and cheapest one!")