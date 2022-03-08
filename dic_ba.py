##########################################
# alien_0={'color':'green','points':3}                                     # 字典:一系列键值对，每个键('color')都与一个值相关联('green')
# print(alien_0['color'])                                                  # 访问字典中的值，值可以为数、字符串、列表、字典等
# print(alien_0['points'])
# new_points=alien_0['points']
# print(f"\nYou just earned {new_points} points!")

# alien_0={'color':'green','points':5}
# print(alien_0)
# alien_0['x_position']=0                                                  # 添加键值对，排列顺序与添加顺序相同
# alien_0["y_position"]=25
# print(alien_0)

# alien_0={}                                                               # 使用空字典创建
# alien_0['color']='green'
# alien_0['points']=5
# print(alien_0)

# alien_0={'color':'green'}
# print(f"The alien color is {alien_0['color'].title()}.")
# alien_0['color']='yellow'                                                # 修改字典中的值
# print(f"The alien color now is {alien_0['color'].title()}.")

# alien_0={'x_position':0,'y_position':25,'speed':'medium'}
# print(f"Original x_position: {alien_0['x_position']}")
# if alien_0['speed']=='slow':
#     x_increment = 1
# elif alien_0['speed']=='medium':
#     x_increment = 2
# else:
#     x_increment=3
# alien_0['x_position']+=x_increment
# print(f"\nNew x_position: {alien_0['x_position']}")

# alien_0={'color':'green','points':5}
# print(alien_0)
# del alien_0['color']                                                    # del:删除键值对，使其永远消失
# print(alien_0)
 
# favorite_languages={
#     'lily':'c',
#     'jimmy':'python',
#     'tom':'c++',
#     'jack':'java',
#     }                                                                    # 字典存储众多对象的同一种信息
# language=favorite_languages['jimmy'].title()
# print(f"Jimmy's favorite language is {language}.")

# alien_0={'color':'green','points':5}
# speed_value=alien_0.get('speed','No speed value assigned.')              # get(,):如果有指定键则返回关联值，没有返回指定的默认值
# print(speed_value,'\n')
# color_value=alien_0.get('color','No color value assigned.')
# print(color_value)
###########################################



# #####################################
# familiar_guy={                                                           # practice
#     'first_name':'luo',
#     'last_name':'huan',
#     'age':24,
#     'city':'Nanjing',
#     }
# print(f"This guy's name is {familiar_guy['first_name'].title()} {familiar_guy['last_name']}.")
# print(f"She is {familiar_guy['age']} years old and she lived in {familiar_guy['city']}.")

# favorite_numbers={
#     'joy':28,
#     'jimmy':18,
#     'zf':6,
#     'tom':3,
#     }
# print(f"\nJoy's favorite number is {favorite_numbers['joy']}.")
# print(f"\nJimmy's favorite number is {favorite_numbers['jimmy']}")

dictionary={
    'if':'条件判断',
    'for':'循环',
    'list':'列表',
    "while":"循环",
    }
print(f"If 语句:\n\t{dictionary['if']}")
print(f"For 语句:\n\t{dictionary['for']}")
print(f"List:\n\t{dictionary['list']}")
print(f"While:\n\t{dictionary['while']}")
###############################################