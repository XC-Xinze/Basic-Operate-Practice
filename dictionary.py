# 动态的,可以动态添加键值对
alien_1 = {"hp": 100, "color": "green", "points": 5}
enemy_hp = alien_1["hp"]
print("enemy_hp:", enemy_hp)
# 添加键值对,只需要直接添加即可
alien_1["attack"] = 10
enemy_attack = alien_1["attack"]
print("alien's attack:", alien_1["attack"])
# 删除键值对
del alien_1["attack"]
# print(alien_1['attack'])#报错,因为已经删除了
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")
# get()方法,可以设置默认值,即不存在的键值对,返回默认值,但是只能对于特定的参数
get_language = favorite_languages.get("ben", "no language using")
print("Ben's favorite language is:", get_language.title())
# 遍历字典,两个变量,一个是键,一个是值
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}.")
# 遍历键,两种方法,一种是通过keys()方法,一种是直接遍历字典
# keys()方法
for name in favorite_languages.keys():
    print(name.title())
# 直接遍历字典
for name in favorite_languages:
    print(name.upper())
# keys()方法返回的是一个列表,可以直接使用列表的方法,保存了所有键值,可以直接使用
# 对于字典中的键值对,可以使用sorted()方法,对键进行排序,略过
# sorted(dictionary.keys()),以排序的顺序返回字典值
for name in sorted(favorite_languages.keys()):
    print(f"{name} is sorted")  # 这里就是按照开头字母顺序排列的输出
for language in sorted(favorite_languages.values()):
    print(f"{language} is sorted(by values)")
# set()方法返回字典中不重复的元素
# 与sorted()方法使用方法一样
# 集合:也是使用花括号创建的,集合与字典的最大的区别就是没有键值对,只有单一的一个元素
# 嵌套:列表中嵌套字典,字典中嵌套列表
# 假设有一堆外星人,每个外星人有不同的信息,可以用列表存储多个外星人字典
alien_a = {"name": "alex", "hp": "100", "color": "red"}
alien_b = {"name": "bob", "hp": "100", "color": "yellow"}
alien_c = {"name": "misa", "hp": "100", "color": "blue"}
aliens = [alien_a, alien_b, alien_c]
for alien in aliens:
    print(alien)
# 同理,字典里也可以嵌套列表
alien_d = {
    "name": "chanel",
    "eat": ["banana", "apple", "orange"],
    "hp": "100",
    "color": "dark",
}
for food in alien_d["eat"]:
    print("Chanel likes eating: \n", food)
# 字典中也可以嵌套字典

#
#
