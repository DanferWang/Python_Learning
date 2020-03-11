# 写入文件
## 写入一个空文件
# file_name  ="new_file.txt"
#
# with open(file_name,"w") as file: ## open函数打开文件的方式默认为“r“只读，将第二个参数设置为”w“就可以写入
#     file.write("I love you!")
#
# ### 非常注意：python只能把字符串写入文本文件。如果写入数值，必须要str（）
#
# ## 写入多行
# with open(file_name,"w") as file: ## open函数打开文件的方式默认为“r“只读，将第二个参数设置为”w“就可以写入
#     file.write("I love you!\nI love Python!\n")
#     file.write("I love sb!\n")
#     file.write("bvuidshvbis")
#
file_name_r = "pi_million_digits.txt"
#### 首先打开文件
with open(file_name_r) as file:
    #### 其次按行读文件
    lines = file.readlines()
    #### 再来创建一个空字符串，用来保存拼接结果
    pi_string = ""
    #### 遍历按行存的2列表，循环拼接
    for line in lines:
        pi_string += line.strip()
#
# file_name_w = "pi_100.txt"
# with open(file_name_w,"w") as file:
#     i = 2
#     file.write(pi_string[:2]) ## 3.
#     while i <= len(pi_string[:102]):
#         file.write(pi_string[i:i+10]+"\n")
#         i += 11


## 附加到文件
file_name_a = "pi_100.txt"
with open(file_name_a,"a") as file:
    file.write("\n")
    file.write(pi_string[102:112]+"\n")
    file.write(pi_string[112:122] + "\n")