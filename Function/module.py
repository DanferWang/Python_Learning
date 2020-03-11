# 模块化

## 导入整个模块
### import 模块名
### 模块名.函数名（参数列表）
# import greet
# greet.greeting("wanghaochen")

## 导入特定函数
### from 模块名 import 函数名1,函数名2,函数名3,......
### 函数名2（参数列表）
# from greet import greeting, pets
# greeting("wanghaochen")
# pets("cat","tangbao")

## 使用as给函数重命名（在调用时重命名）
# from greet import greeting as gg
# gg("wanghaochen")

## 使用as给模块宝重命名（在调用时重命名）
# import greet as gt
# gt.pets("cat","tangbao")

## 导入模块中的所有函数
### 使用 * 提示python，我全都要
### 推荐在大项目中使用这个
from greet import *
greeting("wanghaochen")
pets("cat","tangbao")

# 使用函数时的提示：
##  1、def 函数名有实际意义（首字母只能使用小写字母，加下划线而不能有空格）
##  2、编写好函数，最好加上功能描述
##  3、函数的名称+所需要的实参+返回值（略）
##  4、import一般都放在代码的前面，文档注释的后面