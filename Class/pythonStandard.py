## python 标准库，你只要安装python都会有
import collections
import math
import random

## 带输入顺序的字典
# language = collections.OrderedDict()
#
# language["wang"] = "py"
# language["ren"] = "C"
# language["yao"] = "java"
#
# for k,v in sorted(language.items()):
#     print(k,v)

## 给一个随机数开方
r = random.randint(1,100)
print(r)
print(math.sqrt(r))