###############################################
# alien_0={'color':'green','points':5}  
# alien_1={'color':'yellow','points':10}
# alien_2={'color':'red','points':15}
# aliens=[alien_0,alien_1,alien_2]                                      # 建立一个列表，字典作为列表元素
# for alien in aliens:
#     print(alien)

# aliens=[]                                                             # 创建一个存储外星人的空列表
# for alien_number in range(30):                                        # 生成30只外星人，每只都是一个字典
#     new_alien={'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"The total number of aliens: {len(aliens)}")

# aliens=[]                                                             # 创建一个存储外星人的空列表
# for alien_number in range(30):                                        # 生成30只外星人
#     new_alien={'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:                                              # 修改前三个外星人
#     if alien['color']=='green':
#         alien['color']='yellow'
#         alien['points']=10
#         alien['speed']='medium'
# for alien in aliens[:5]:
#     print(alien)

# pizza={
#     'crust':'thick',                                                  # 建立一个字典，列表作为字典的键值
#     'toppings':['mushrooms','extra cheese'],                          # 一个键拥有多个值时
#     }
# print(f"You ordered a {pizza['crust']}-crust pizza "
#     "with the following toppings:")                                   # print()字符串很长时可以分行    
# for topping in pizza['toppings']:
#     print("\t"+topping)

# favorite_languages={
#     'lily':['python','c++'],                                          # 列表作为字典键值对
#     'jimmy':['c','python'],
#     'tom':['java'],
#     'joy':[],
#     }
# for name,languages in favorite_languages.items():                     # languages列表元素个数有多种可能，用len()来判断
#     if len(languages)==0:
#         print(f"\n{name.title()} doesn't like any language.")
#     elif len(languages)==1:
#         print(f"\n{name.title()}'s favorite language is:\n\t{languages[0].title()}")
#     else:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print("\t"+language.title())

# users={
#     'lily':{
#         'first':'albert',                                             # 在字典中存储字典
#         'last':'einstein',                                            # 与每个键相关联的值都是一个字典
#         'location':'princeton',
#         },
#     'joy':{
#         'first':'marie',
#         'last':'curie',
#         'location':'paris',
#         },
#     }
# for username,user_info in users.items():                              # 键赋给变量username,相关联的字典赋给变量user_info
#     print(f"\nUsername: {username.title()}")
#     full_name=f"{user_info['first']} {user_info['last']}"
#     location=user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")
##################################################



###########################################
# guy_0={'name':'jimmy','age':'23','city':'wuhan'}                      # practice
# guy_1={'name':'joy','age':'24','city':'chongqin'}
# guy_2={'name':'zf','age':'23','city':'wuhan'}
# people=[guy_0,guy_1,guy_2]
# for guy in people:
#     print(f"\n{guy['name'].title()} is {guy['age']} years old,and was born in {guy['city'].title()}.")

# pet_0={'type':'orange cat','owner':'jimmy'}
# pet_1={'type':'white dog','owner':'joy'}
# pet_2={'type':'black mouse','owner':'zf'}
# pets=[pet_0,pet_1,pet_2]
# for pet in pets:
#     print(f"\nThis pet is a {pet['type']} and its owner is {pet['owner'].title()}.")

# favorite_places={
#     'jimmy':['whhan','nanjing','shanghai'],
#     'joy':['chongqin','nanjing'],
#     'zf':['whhan','chongqin','shenzhen'],
#     }
# for name,places in favorite_places.items():
#     print(f"\n{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")

cities={
    'wuhan':{
        'country':'china',
        'population':'10 million',
        },
    'new york':{
        'country':'american',
        'population':'20 million',
        },
}
for city,info in cities.items():
    print(f"\nCity's name: {city.title()}")
    print(f"{city.title()} belongs to {info['country'].title()}")
    print(f"City's population: {info['population'].title()}")
input()
###############################################