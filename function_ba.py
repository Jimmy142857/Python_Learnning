#####################################
# def  greet_user():                                                # def:函数定义
#     """显示简单的问候语"""                                         # 文档字符串:描述函数的主要功能
#     print("Hello!")
# greet_user()                                                      # 括号不能少
# print(greet_user.__doc__)                                         # 调用文档字符串属性


# def greet_user(username):                                         # 向函数传递信息,形参(username)
#     print(f"Hello, {username}!")
# greet_user('joy')                                                 # 实参('joy')
# greet_user(9527)
#####################################



######################################
# def display_message():                                            # practice
#     """打印一个句子，指出本章所学内容。"""
#     print("I learn function of python this chapter.")
# display_message()
# print("\n"+display_message.__doc__)

# def favorite_book(title):
#     print(f"\nOne of my favorite book is {title.title()}.")
# favorite_book('relativity')
######################################



###################################################
# def describe_pet(animal_type,pet_name):                          
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
# describe_pet('cat','joy')                                          # 位置实参:基于实参的顺序来关联实参和形参
# describe_pet('dog',233)                                            # 多次调用函数

# def describe_pet(animal_type,pet_name):                          
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
# describe_pet(animal_type='cat',pet_name='joy')                     # 关键字实参:顺序无关紧要
# describe_pet(pet_name='joy',animal_type='cat')

# def describe_pet(pet_name,animal_type='cat'):                      # 指定形参默认值，未设置默认值的形参顺序在前
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
# describe_pet(pet_name='joy')
# describe_pet('joy')
# describe_pet(pet_name='joy',animal_type='dog')                     # 有实参时忽略默认值，使用实参值
# describe_pet('joy','dog')
####################################################



#####################################
# def make_shirt(size,words):                                                       # practice
#     print(f"We goona make a {size}-size shirt with word '{words}' on it.")
# make_shirt('L','hot')
# make_shirt(size='XL',words='cold')

# def make_shirt(size='XXL',phrase='I love Python'):
#     print(f"\nWe goona make a {size}-size shirt with phrase '{phrase}' on it.")
# make_shirt()
# make_shirt(size='XL')
# make_shirt(phrase='I love C++')

def describe_city(city,country='China'):
    print(f"\n{city.title()} is in {country.title()}.")
describe_city('wuhan')
describe_city('shanghai')
describe_city(city='new york',country='america')
#####################################