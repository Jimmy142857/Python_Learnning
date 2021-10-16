###############################################
# name=['Li ','Wei ','Jie']
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[0]+name[1]+name[2])
# print(233)


# mes='I said "HI python".'
# print(mes)


# name="ada lovelace"
# print(name.title())                                                   # title():字符串中每个单词首字母大写
# print(name.upper())
# print(name.lower())


# first_name="ada"
# last_name="lovelace"
# full_name=f"{first_name} {last_name}"                                 # f字符串:通过把花括号内的变量替换为其值来设置字符串格式
# print(full_name)
# print(f"Hello, {full_name.title()}")
# message=f"Hello, {full_name.upper()}"
# print(message)


# print("python")
# print("\tpython")                                                     # \t:字符组合-制表符
# print("\nLanguages:\nPython\nC\nJavaScript")                          # \n:换行符
# print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")


# favorite_language='  python  '
# print(favorite_language)
# print(favorite_language.rstrip())                                     # rstrip():去除字符串末尾多余空白,变量值不变
# print(favorite_language.lstrip())                                     # lstrip():去除字符串开头多余空白,变量值不变
# print(favorite_language.strip())                                      # strip():去除字符串开头及末尾多余空白,变量值不变
# print('\n')
# print(favorite_language)
# favorite_language=favorite_language.lstrip()                          #将删除结果关联到变量,变量更新
# print(favorite_language)


# message="One of Python's strengths is its diverse community."
# print(message)
# message='One of Python's strengths is its diverse community.'                          #语法错误,应当注意双引号和单引号的对应
# print(message)
#################################################################



##########################################################
# name="jimmy"
# print(f"Hello {name.title()},would u like to learn some python today?")                # Practice
# print(f"{name.title()}\n{name.upper()}\n{name.lower()}")
# famous_person="Albert Einstein"
# message=f'{famous_person} once said,"A person who....."'
# print(message)
# free_guy="\tDeathpool   "
# print(f"{free_guy}\n{free_guy.lstrip()}\n{free_guy.rstrip()}\n{free_guy.strip()}")     # 制表符可以被去除


x,y,z=1,2,3                                                                              # 给多个变量赋值,用逗号将变量名隔开
a,b,c="sun","glasses","red"
print(f"{c.title()} {a.title()+b}")
print(x+y+z)
MAX_CONNECTIONS=500                                                                      # 常量一般用全大写表示
print(MAX_CONNECTIONS)
###############################################################