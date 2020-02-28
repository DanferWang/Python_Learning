# 创建一个字典
alien_0 = {'colour': 'green', 'sex': 'male', 'height': 140}  # 字典里的第一个成员：内容就是KV对
# 查字典
# print(alien_0['colour'])
# print(alien_0['height'])
# alien_0_height = alien_0['height']
# print("Alien_0 的身高是" + str(alien_0_height))

# # 添加KV对
# alien_0['weight'] = 410
# print(alien_0)
# # ## 也可用这种方法新建字典
# # alien_1 = {}
# # alien_1['colour'] = 'red'
# # alien_1['sex'] = 'female'
# # alien_1['height'] = 110
# # alien_1['weight'] = 5
# # print(alien_1)
# #
# # # 修改
# # alien_1['weight'] = 101
# # print(alien_1)
#
# # 删除
# del alien_0['sex']
# print(alien_0)

alien_0 = {'colour': 'green', 'sex': 'male', 'height': 140}
alien_1 = {'colour': 'red', 'sex': 'famale', 'height': 110}
alien_2 = {'colour': 'yellow', 'sex': 'male', 'height': 80}

# # 字典嵌套在列表里
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

## 自动生成一些n胞胎
### 常用业务新建模式：新建空列表、for循环迭代（迭代范围）、dict新建定义、遍历查看
alien_bros = []
for bro_number in range(30):
    new_bro = {'colour': 'yellow', 'sex': 'male', 'height': 80}
    alien_bros.append(new_bro)
# for alien1 in alien_bros:
#     print(alien1)

## 成群结队修改
# # ### 常用业务修改模式：列表的切片、for循环迭代、dict访问修改、遍历查看
# # # for edit_alien in alien_bros[-3:]:
# # #     edit_alien['colour'] = 'red'
# # # for alien1 in alien_bros:
# # #     print(alien1)
#
# # 列表嵌套在字典里
# mcdonald = {
#     'wang': ["mailajituibao set", "double pies"],
#     'ren': ["roast duck", "mai storm", "big mac"],
#     'trump':["cola"] # 那怕他只配喝个可乐，也得给他加个[]形成列表，否则不可迭代
# }
# ## 遍历查询
# ### 这是我们常用的双重遍历（先遍历字典，再遍历列表）
# print("请给我们来点这些东西：")
# for food in mcdonald.values():
#     for food1 in food:
#         print(food1)

# 在字典里嵌套字典 有点结构体的意思
## 定义的时候，就要把每个次级字典的结构保持一致
# users = {
#     'einstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'loc': 'princeton'
#     },  # 这里的，容易被忽略
#     'newton': {
#         'first': 'isaac',
#         'last': 'newton',
#         'loc': 'huangtugaopo'
#     }
# }
#
# ## 遍历一把
# ## 字典与字典的嵌套遍历时,特别要注意上级字典Value（下级字典）的KV对应关系
# for user_name, user_info in users.items():
#     print(user_name)
#     for detail_tag, detail_info in user_info.items():
#         print(detail_tag + ":" + detail_info)  ## 逻辑复杂点

# exercise:
## 1、计算3~3000000中3的倍数的总和：创建一个列表，其中包含3~3000000中3的倍数，再计算这些数的总和
num3 = [value * 3 for value in range(1,1000001)]
print(sum(num3))

## 2、列表cars = ["bmw", "benz", "audi", "toyota", "ford"]，wang要买前三辆车，trump要买后三辆车，
#    请分别列出wang和trump的购买列表
## 3、城市信息统计：创建西安市城市行政区信息统计，其中将13个行政区用作键；对于每个行政区，都创建一个字典，并在其中包含该
#    行政区的占地面积、政府地址、政府电话。将每个行政区的的名字和相关信息都输出。
#  新城区人民政府：尚德路115号，电话：87444870，面积：30.13
#  碑林区人民政府：南院门27号，电话：89625070，面积：23.37
#  莲湖区人民政府：北院门159号，电话：87334782，面积：38.32
#  灞桥区人民政府：纺一路809号，电话：83519508，面积：324.50
#  未央区人民政府：龙首北路西段1号，电话：86235439，面积：264.41
#  雁塔区人民政府：小寨东路168号，电话：85252032，面积：151.44
#  阎良区人民政府：阎良区延安街6号，电话：86875049，面积：244.55
#  临潼区人民政府：临潼区书院门街41号，电话：83872245，面积：915.97
#  长安区人民政府：长安区韦郭路中段，电话：85292125，面积：1588.53
#  周至县人民政府：周至县老城东街37号，电话：87111824，面积：2945.20
#  鄠邑区人民政府：鄠邑区东大街7号，电话：84812290，面积：1279.42
#  蓝田县人民政府：蓝田县县门街6号，电话：82721166，面积：2005.95
#  高陵区人民政府：高陵县县门街29号，电话：86913024，面积：285.03
