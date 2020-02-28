# exercise:
# 开发一个APP或者网页用户名注册系统，要求确保每位用户的用户名都是独一无二的。
#   #1、已经注册好的用户名列表：current_users = ["Wang","Ren","Yao","trump","Jerry"，"Randy orton"]
#   #2、需要新注册的用户名：new_users = ["Tom","TruMp","mickey","Minnie","Randy Orton"]
#   #3、为了确保系统的鲁棒性，首先检查待新建的用户名列表是否为空
#   4、对new_users遍历，其中的每个用户名，都要检查是否已经被current_users占用。如果已经被占用，
#     则输出”（用户名）该用户名已被占用，请重新输入“；否则，输出”（用户名）该用户名设置成功“。
#   5、确保比较时不区分大小写。举个例子：Randy orton（兰迪奥顿）已被使用，应该拒绝用户名Randy Orton。

current_users = ["Wang", "Ren", "Yao", "trump", "Jerry", "Randy orton"]
new_users = ["Tom", "TruMp", "mickey", "Minnie", "Randy Orton"]
if current_users: ## 判断是否为空 非空
    current_users_temp = []
    ## 对current_user整体做lower，确保比较时无大小写区分（全部转换为小写）
    for current_name in current_users:
        current_name_low = current_name.lower()
        current_users_temp.append(current_name_low)
    ## 对new_users遍历，在current_users中比对
    for new_name in new_users:
        new_name_low = new_name.lower()
        if new_name_low in current_users_temp:
            print(new_name + "该用户名已被占用，请重新输入")
        else:
            current_users.append(new_name)
            print(new_name + "该用户名设置成功")
    ## 输出添加后的用户名列表
    print(current_users)
else:## 若为空
    current_users = new_users
    for name in current_users:
        print(name + "该用户名设置成功")
