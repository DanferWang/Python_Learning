# 分析文本
## 提取单词
### split() 分割，分离函数：将一句话/一段话中的单词存到一个列表/数组中
### 它是以空格为分隔符
# sentence = "I love you ."
# words = sentence.split()
# print(words)

## 字数统计
# file_name = "huang.txt"
#
# try:
#     file = open(file_name, encoding="utf-8")
#     contents = file.read()
# except FileNotFoundError:
#     print("no such file")
# else:
#     words = contents.split()
#     print("this book probably has " + str(len(words)) + " words.")

# def word_count(file_name):
#     try:
#         file = open(file_name, encoding="utf-8")
#         contents = file.read()
#     except FileNotFoundError:
#         pass  ## 出现异常时忽略他
#     else:
#         words = contents.split()
#         print(file_name + " probably has " + str(len(words)) + " words.")
#
#
# books = ["A Modest Proposal.txt", "huang.txt", "Frankenstein; Or, The Modern Prometheus.txt", "Pride and Prejudice.txt"]
# for book in books:
#     word_count(book)

## 词频统计
### 打开文件，读取内容，提取单词
file = open("Pride and Prejudice.txt",encoding="utf-8")
content = file.read()
words =content.split()

### 先提取词典（集合化）
word_dict = set(words)

### 对这个词典中的每一个单词，在单词列表中计数
for word in word_dict:
    num = words.count(word)
    print(word + ":" + str(num))
