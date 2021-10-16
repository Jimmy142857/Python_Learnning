#######################################
# cars=['audi','bmw','subaru','toyota']
# for car in cars:
#     if car=='bmw':                                                   # if语句:条件测试表达式，测试值为真则执行紧跟其后的代码，为假则忽略这些代码
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping='mushrooms'
# if requested_topping!='anchovies':                                   # 判断两个值是否不相等
#     print("\nHold  the anchovies!")

# answer=20
# if answer!=17:
#     print("\nAnswer is wrong,please try again!")

# age_0=22
# age_1=18
# print(age_0>=21 and age_1>=21,"\n")                                  # and:两个都为真时条件才为真
# print((age_0>=21) and (age_1<=21),"\n")
# print(age_0>=21 or age_1>=21,"\n")                                   # or:有一个为真时条件为真
# print(age_0<=21 or age_1<=21)

# requested_toppings=['mushrooms','onions','pineapple']
# print('mushrooms' in requested_toppings)                             # in:判断特定值是否包含在列表中
# print('pepperoni' in requested_toppings,"\n")

# banned_users=['lily','davis','joy']
# user="joy"
# if user not in banned_users:                                         # not in:检查是否不包含
#     print(f"{user.title()}, u are available for the resources.")
# else:
#     print(f"Sorry {user.title()}, u r a poor guy.")

# game_active=True                                                     # 布尔类型变量
# game_ended=(1>=2)
# print(game_active,game_ended)
#######################################



########################           
# car='bmw'                                                            # practice
# print("Is car == 'subaru'? I predict false.")
# print(car=='subaru')
# print("\nIs car =='bmw'? I predict true.")
# print(car=='bmw')

cars=['Audi','subaru','Bmw','Toyota']                                # 模拟从列表中查找元素是否存在
car="BMW"
print(f"\nWhether {car} is in my garage?\n{car in cars}")
print("Let's try again.")
car_founded='No'
for ele in cars:
    if (car.lower()==ele.lower()):
        car_founded='Yep'
print(f"Is my {car} founded?\n{car_founded}") 

# cars_1=[]
# for ele in cars:                                                     # for生成新列表
#     cars_1.append(ele.lower())
# cars_2=[ele.lower() for ele in cars]                                 # 列表解析生成新列表
# print(cars,cars_1,cars_2)
# print(f"\nWhether {car} is in my garage?\n{car.lower() in cars_1}")
# print(f"\nWhether {car} is in my garage?\n{car.lower() in cars_2}")
####################################


