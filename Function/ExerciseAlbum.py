# Exercise：
# 1、编写一个make_album()函数，它创建一个描述音乐专辑的字典，这个函数接收歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 2、使用这个函数创建三个表示不同专辑的字典，并打印每个返回值，以核实该函数和字典正确的执行了我们所需要的逻辑。
# 3、给make_album()添加一个可选的形参，以便能储存专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，
#   就将这个值添加到表示专辑的字典中。
# 4、编写一个while循环，每次让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们调用make_album()，
#   并将创建的字典打印出来，建议可以编一个forall_dict()来打印字典。
# 提供的一些艺术家与专辑信息：
#   Jay Chou：Jay Chou's Bedtime Stories (10)
#   JJ Lin：Message In A Bottle (11)
#   Han Hong: The Wimpy Kid
#   Taylor Swift: Lover (18)
#   Justin Bieber: Friends
#   Ed Sheeran: five


## 1、2
def make_album(artist, album):
    artist_dict = {}
    artist_dict[artist] = album
    return artist_dict


Han_Hong = make_album("Han Hong", "The Wimpy Kid")
Justin_Bieber = make_album("Justin Bieber", "Friends")
Ed_Sheeran = make_album("Ed Sheeran", "five")
print(Han_Hong)
print(Justin_Bieber)
print(Ed_Sheeran)


### 3
# def make_album(artist, album, num=""):
#     if num == "":
#         artist_dict = {}
#         artist_dict["artist"] = artist
#         artist_dict["album"] = album
#         return artist_dict
#     else:
#         artist_dict = {}
#         artist_dict["artist"] = artist
#         artist_dict["album"] = album
#         artist_dict["num"] = num
#         return artist_dict


# Han_Hong = make_album("Han Hong", "The Wimpy Kid")
# Jay_Chou = make_album("Jay_Chou", "Jay Chou's Bedtime Stories", 10)
# print(Han_Hong)
# print(Jay_Chou)


# ### 4
# def forall_dict(dict):
#     for k, v in dict.items():
#         print(k + ":" + v)
#
#
# dict = []
# while True:
#     i = 0
#     artist = input("artist:")
#     album = input("album name:")
#     num = input("num of music:")
#     dict_this = make_album(artist, album, num)
#     dict.insert(i,dict_this)
#     print(dict[i])
#     forall_dict(dict_this)
#     i += 1
#     msg = input("input q to quit")
#     if msg == "q":
#         break
#
# print(dict)