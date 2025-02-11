#动态的,可以动态添加键值对
alien_1={'hp':100,'color':'green','points':5}
enemy_hp=alien_1['hp']
print('enemy_hp:',enemy_hp)
#添加键值对,只需要直接添加即可
alien_1['attack']=10
enemy_attack=alien_1['attack']
print('alien\'s attack:',alien_1['attack'])
#删除键值对
del alien_1['attack']
#print(alien_1['attack'])#报错,因为已经删除了
favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'rust',
      'phil': 'python',
      }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
#get()方法,可以设置默认值,即不存在的键值对,返回默认值,但是只能对于特定的参数
get_language=favorite_languages.get('ben','no language')
print('Ben\'s favorite language is:',get_language.title())
#遍历字典,两个变量,一个是键,一个是值
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
#遍历键,两种方法,一种是通过keys()方法,一种是直接遍历字典
#keys()方法
for name in favorite_languages.keys():
    print(name.title())
#直接遍历字典
for name in favorite_languages:
    print(name.title()) 
# keys()方法返回的是一个列表,可以直接使用列表的方法,保存了所有键值,可以直接使用
#对于字典中的键值对,可以使用sorted()方法,对键进行排序,略过

