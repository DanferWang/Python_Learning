# 遍历列表
# for 循环
# magicians = ["liuqian1", "liuqian2", "dawei1", "dawei2"]
# print(magicians)
#
# for magician in magicians:
#     print("'It's my show time! said '" + magician.title())
#     print("Don't Do THAT Mr. Luo!")
# print("Thank you ARE U OK?")

## Tom, Jerry, Mickey, Minnie 四个人参加商业活动，现在制作一个嘉宾欢迎词，要求将所有嘉宾存储在一个列表中，
#   1、获取该列表长度，并使用访问检查是否存储正确；
#   2、该活动又邀请了HelloKitty，要把她也要加到该列表的第三位中，输出检查；
#   3、为了尊重每一位嘉宾，按照字母倒序排列他们在列表中的位置，输出检查；
#   4、Tom和Jerry因为参加音乐会演出，所以要把这两个人从列表中删除，并且要祝他们音乐会演出成功,之后输出列表；
#   5、使用for循环遍历，向每一个参加活动的嘉宾发表欢迎词Welcome to our party, XXX，
#   并在最后祝愿每个人都玩的开心Help yourselves。

# 1
guests = ["Tom", "Jerry", "Mickey", "Minnie"]
print("length=" + str(len(guests)))
print("query:" + guests[0] + " " + guests[1] + " " + guests[2] + " " + guests[-1])
# 2
guests.insert(2, "HelloKitty")
print(guests)
# 3
guests.sort(reverse=True)
print(guests)
# 4
print("Wish you succeed " + guests.pop(0) + "&" + guests.pop(2) + "!")
guests.remove("HelloKitty")
print(guests)
# 5
for guest in guests:
    print("Welcome to our party, " + guest)
print("Help yourselves!")
