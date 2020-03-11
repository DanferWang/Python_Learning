# 传递任意数量的实参
# def order(*foods): ## * 提示python接受的是一个元组
#     for food in foods:
#         print("you have ordered: " + str(food))
#
# order("big mac","french fired","cola")
# order("sandy")

## 位置实参(关键字实参)+任意数量实参
###　任意数量实参必须放到参数列表的最后，让py先去接收位置实参和关键字实参
# def order(size,*foods): ## * 提示python接受的是一个元组
#     print("you ordered: "+ str(size))
#     for food in foods:
#         print("you have ordered: " + str(food))
#
# order(12,"duck","smelly tofu","yogurt")

## 任意数量的关键字实参
def create_profile(first,last,**user_info): ## ** 提示python接受的是一个键值对（一项字典）
    profile = {}
    profile["first name"] = first
    profile["last name"] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile


wang_profile = create_profile("Haochen","Wang",age="22",sex = "male") ## 调用到任意数量实参时，key不能加“”
print(wang_profile)