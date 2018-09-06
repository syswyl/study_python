# list = ["shuifu", "bicyle", "um"]
# # append,insert 插入 注意insert需要标注插入位置
# list.append("songshuang")
# list.insert(0, "yth")
# del list[2]
# # remove只删除第一个出现的位置
# # sort 永久性改变， sorted只是临时改变 通过reserve可以进行排序后得翻转
# print(sorted(list, reverse=True))
# # 遍历list学习
# the_2 = list[:]
# the_2[2] = "bjtu"
# for the, anth, than in zip(the_2, list, the_2):
#     print(the, "\t", anth, "\t", than)
# print("the module is over")

# if语句学习
# age = int(input())
# if age < 4:
#     price = 10
# elif age < 18:
#     price = 100
# else:
#     price = 99
# print("your admission price is $" + str(price) + "!")
# alien = {"color": "green", "price": 5}
# alien["x_position"] = 0
# alien["y_position"] = 25
# # print(alien)
# favorite_languages = {
#     'jen': ['java', 'c', 'python'],
#     'sarach': 'c',
#     'phil': ['python', 'java', 'perl'],
# }
# friends = ['zyh', 'ss', 'jen']
# for i in favorite_languages:
#     print(i.title())
#     if i in friends:
#         print("hello " + i + " i see your favorite language is " +
#               favorite_languages[i].title())
#     else:
#         print("sorry " + i + " i don't see your favorite language"
#                              "in the dictionary")
# print("\nthe followed languages have been mentioned:\n")
# for language in favorite_languages.values():
#     print(language.upper())
# array = [1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 4, 5]
# print(len(array))
# for key in favorite_languages.keys():
#     if len(favorite_languages[key]) == 1:
#         print("hello " + key + " your favorite language is " + favorite_languages[key].upper())
#     else:
#         print("hello " + key + " your favorite languages are : ")
#         for lan in favorite_languages[key]:
#             print(lan.title())
# responses = {}
# active = True
# while active:
#     name = input("what is your name?\n")
#     mountain = input("which mountain would you like to climb?\n")
#     re = input("let other people to answer yes/no  ?\n")
#     responses[name] = mountain
#
#     if re == 'no':
#         active = 0
#
# print(responses)
# for name in sorted(responses.keys()):       #按照字典序排序
#     print(name.title())


# def as_print(person_name, name, album=0):
#     if album == 0:
#         this_album = {"person": person_name,
#                       "album_name": name}
#     else:
#         this_album = {"person": person_name,
#                       "album_name": name,
#                       "album_num": album}
#
#     return this_album
#
#
# while True:
#     print("input 'q' to quit")
#     p = input("person's name:")
#     if p == 'q':
#         break
#     album_name = input("input album's name:")
#     num = int(input("input album's number:"))
#     print("hello  the album's infor is as followed" + str(as_print(p, album, num)))

# def un_printname(unprintnames):
#     modify = []
#     for name in unprintnames:
#         name = name + "the coll"
#         modify.append(name)
#
#     return modify
#
#
# def showname(completednames):
#     print("the followed have been printed: \n")
#     for (name, i) in zip(completednames, range(len(completednames))):
#         print("this is the number" + str(i+1) + " show the window :  " + name)
#
#
# uncompletedname = ['ss', 'xmh', 'scy', 'tht']
# showname(uncompletedname)
# showname((un_printname(uncompletedname[:])))
# def person_infor(xm, nn, **other):
#     person_resume = {}
#     person_resume['name'] = xm
#     person_resume['sex'] = nn
#     for (key, value) in other.items():
#         person_resume['key'] = value
#
#     return person_resume
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.lower() + " is now sitting!")

    def roll(self):
        print(self.name.title() + " is now rolling!")

