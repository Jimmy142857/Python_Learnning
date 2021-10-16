########################################
# def make_pizza(*toppings):                                       # *toppings:创建一个名为toppings的空元组，将收到的所有值都封装到这个空元组中
#     """打印顾客点的所有配料"""
#     print(toppings)
# make_pizza('pepper')
# make_pizza('beef','extra cheese','pork')                         # 将实参封装到一个元组中,可传递任意数量的位置实参

# def make_pizza(*toppings):
#     """概述要制作的pizza"""
#     print("\nMaking pizza with the following toppings:")
#     for topping in toppings:                                    # 遍历列表,打印元组元素
#         print(f"-{topping}")
# make_pizza('pepper')
# make_pizza('beef','pork','extra cheese')

# def make_pizza(size,*toppings):                                 # 结合使用位置实参和任意数量实参，任意数量实参必须放在最后面
#     """概述要制作的pizza"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
# make_pizza(8,'beef')
# make_pizza(12,'beef','pork','extra cheese')                     # 任意数量实参必须放到最后


# def build_profile(first,last,**user_info):                      # **user_info:创建一个空字典，并将收到的所有名称值对都放到这个字典中
#     """创建一个字典，其中包含我们知道有关用户的一切。"""
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info
# user_profile=build_profile('albert','einstein',
#                           location='princeton',
#                           field='physics')                      # 传递两个键值对，相当于可传递任意数量的关键字实参
# print(user_profile)
#############################################



###########################################
# def make_sandwich(*toppings):                                  # practice
#     print("\nThe sandwich u ordered have the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_sandwich('pork')
# make_sandwich('pork','vegetable')
# make_sandwich('beef','tomato','pepper')

# def build_profile(first,last,**user_info):                     
#     """创建一个字典，其中包含我们知道有关用户的一切。"""
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info
# user_profile=build_profile('Li','WeiJie',
#                             birthplace='Wuhan',
#                             gender='male',
#                             hobbies=['football','computer game','singing'])               # hobbies为键名所以键值可以是列表
# print(user_profile)

# def make_car(manufacturer,type,**cars):
#     """创建一个字典，包含车车信息"""
#     cars['manufacturer']=manufacturer
#     cars['type']=type
#     return cars
# car=make_car('Benz','AMG',
#             color='red',
#             turbo=True)
# print(car)
####################################################



##################################################
# import function_op                                                         # 导入function_op.py模块，将其中所有的函数都复制过来
# function_op.make_pizza(16,'pepper')
# function_op.make_pizza(12,'mushrooms','green peppers','extra cheese')      # 指定（被导入模块名称）和（函数名）用（句点）分隔来调用函数


# import function_op as p                                                    # 使用as给模块指定别名
# p.make_pizza(16,'pepper')
# p.make_pizza(12,'mushrooms','red peppers','extra cheese')


# from function_op import make_pizza                                         # 从指定模块中导入指定函数，可以多个
# make_pizza(16,'pepper')
# make_pizza(12,'mushrooms','green peppers','extra cheese')                  # 可直接使用函数


# from function_op import make_pizza as mp                                   # 使用as给函数指定别名
# mp(16,'pepper')
# mp(12,'mushrooms','red peppers','extra cheese')


# from function_op import *                                                  # (*)运算符导入模块中所有函数
# make_pizza(16,'pepper')                                                    # 不建议这种方法，容易覆盖函数
# make_pizza(12,'mushrooms','red peppers','extra cheese')
##############################################################



#########################################
# from function_op import print_models as p                                  # practice
# from function_op import show_completed_models as s
# unprinted=['tree','house','rock']
# printed=[]
# p(unprinted,printed)
# s(printed)

import function_op as p
unprinted=['tree','house','rock']
printed=[]
p.print_models(unprinted,printed)
p.show_completed_models(printed)
##########################################