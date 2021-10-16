################################
# age=19
# if age>=18:                                                             # 最基本的if语句
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")

# age=17
# if age>=18:                                                             # if-else:只存在两种情形时
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Register to vote as soon as you turn 18!")

# age=12
# if age<4:                                                               # if-elif-else:考虑的情形超过两个
#     print("Your admission coat is $0.")
# elif age<18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")
# if age<4:                                                               # 让代码更简洁引入price变量
#     price=0
# elif age<18:
#     price=25
# else:
#     price=40
# print(f"\nYour admission cost is ${price}.")

# age=66
# if age<4:                                                               
#     price=0
# elif age<18:                                                            # 使用多个elif模块
#     price=25
# elif age<=65:
#     price=40
# else:
#     price=20
# print(f"\nYour admission cost is ${price}.")

# age=12
# if age<4:                                                               
#     price=0
# elif age<18:                                                            
#     price=25
# elif age<=65:
#     price=40
# elif age>65:                                                            # 可以省略else代码块，使特定条件更清晰
#     price=20
# print(f"\nYour admission cost is ${price}.")

# requested_toppings=['mushrooms','extra cheese']                       
# if 'mushrooms' in requested_toppings:                                   # 使用多个简单的if语句，判断所有独立的条件
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")
##################################################


#################################################
# alien_color='red'                                                       # practice
# if alien_color=='green': 
#     print("You scored 5 points!")
# elif alien_color=='yellow':
#     print("You scored 10 points!")
# elif alien_color=='red':
#     print("You scored 15 point!")

# age=23
# if age<2:
#     print("You are a baby.")
# elif age<4:
#     print('You are a small kid.')
# elif age<13:
#     print("You are a child.")
# elif age<20:
#     print("You are a teenager.")
# elif age<65:
#     print("You are an adult.")
# else:
#     print("You are an old people.")

# favorite_fruits=['apple','banana','orange']
# if 'apple' in favorite_fruits:
#     print("\nu really like apple!")
# if 'banana' in favorite_fruits:
#     print("\nu really like banana!")
# if 'orange' in favorite_fruits:
#     print("\nu really like orange!")
###############################################



##############################################
# requested_toppings=['mushrooms','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping=='green peppers':                              # 检查特殊元素
#         print("Sorry,we are out of green peppers now.")
#     else:
#         print(f"Adding {requested_topping}")
# print("\nFinished making your pizza.")

# requested_toppings=[]                                                    # 检查列表是否为空
# if requested_toppings:                                                   # 将列表名用作条件表达式时，列表为空返回False,至少包含一个元素时为True
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza.")
# else:
#     print("Are u sure u want a plain pizza.")

# available_toppings=['mushrooms','olives',
#                     'green peppers','pepperoni',
#                     'pineapple','extra cheese'
#                     ]            
# requested_toppings=['mushrooms','french fries','extra cheese']              # 使用多个列表
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry,we dont have {requested_topping}.")
# print("\nFinished your pizza!")
#######################################



########################################
# names=['lily','jimmy','joy','admin','tom']                                  # practice
# if names:
#     for name in names:
#         if name=='admin':
#             print(f"Hello {name},would u like to see a status report?")
#         else:
#             print(f"Hello {name.title()},thank u for logging again.")
# else:
#     print("We need to find some users!")

current_users=['david','Lily','joy','jimmy','tom']
cur_users=[name.lower() for name in current_users]                           # 模拟网站注册用户名
new_users=['lily','jimmy','Sam','jack','John']
for user in new_users:
    if user.lower() in cur_users:
        print(f"\n{user} has been used,you need to change a name.")
    else:
        print(f"\nYou can use {user}.")

# numbers=list(range(1,10))
# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#         print(f"{number}nd")
#     elif number == 3:
#         print(f"{number}rd")
#     else:
#         print(f"{number}th")
####################################
