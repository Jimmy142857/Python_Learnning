###############################################
# users_o={
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
#     }
# for ke,value in users_o.items():                                              # 遍历所有键值对
#     print(f"\nKey: {ke}")                                                     # items():返回一个包含所有键值对的列表
#     print(f"Value: {value}")

# favorite_languages={
#     9527:'c',                                                                 # 键名也可以是数字
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'java',
#     } 
# for name,language in favorite_languages.items():                              # 将键名赋给name,键值赋给language
#     print(f"{name}'s favorite language is {language.title()}.\n")

# favorite_languages={
#     'lily':'c',
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'java',
#     } 
# for name in favorite_languages.keys():                                        # keys():返回一个列表包含字典中所有键
#     print(name.title())
# print('\n')
# for name in favorite_languages:                                               # 省略时也是提取键
#     print(name.title())

# favorite_languages={
#     'lily':'c',
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'java',
#     } 
# friends=['jimmy','jack']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}!")
#     if name in friends:
#         language=favorite_languages[name].title()                               # 将name的当前值作为键
#         print(f"{name.title()}, I guess u love {language}!\n")                  # 对朋友打印特殊消息
#     else:
#         print()    

# favorite_languages={
#     'lily':'c',
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'java',
#     }   
# for name in sorted(favorite_languages.keys()):                                # 利用sorted()在遍历之前进行排序
#     print(f"{name.title()}, thank u for taking the poll.\n")

# favorite_languages={
#     'lily':'c',
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'c',
#     } 
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():                                  # values():返回字典中所有值的列表,值可能会重复
#     print(language.title())

# favorite_languages={
#     'lily':'c',
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'c',
#     } 
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):                             # 使用集合set()使得列表中没有重复值
#     print(language.title())

# languages={'python','c','c++','python'}                                       # 集合:花括号内没有键值对，存储没有特定顺序
# print(languages)                                                              # 集合可以自动去重
##################################################



##############################################
# dictionary={                                                                  # practice
#     'if':'条件判断',
#     'for':'循环',
#     'list':'列表',
#     }
# for name,explain in dictionary.items():
#     print(f"{name.title()}表示python中的{explain}.\n")

# rivers={
#     'nile':'egypt',
#     'yellow river':'china',
#     'ganges':'india',
#     }
# for river,country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")
# print()
# for river in rivers.keys():
#     print(river.title())
# print()
# for country in rivers.values():
#     print(country.title())

favorite_languages={
    'lily':'c',
    'jimmy':'python',
    'tom':'c++',
    'jack':'java',
    } 
guys=['jimmy','tom','joy']
for guy in guys:
    if guy in favorite_languages.keys():
        print(f"{guy.title()}, thank u for joining the poll!\n")
    else:
        print(f"{guy.title()}, we strongly invite u for the poll!\n")
##################################################