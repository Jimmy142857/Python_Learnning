###################################
# from class_op import Car                                                # 将类存储在模块中，在主程序中导入模块的一个类

# my_new_car=Car('audi','a4',2021)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()


# from class_op import Car,ElectricCar                                    # 从一个模块中导入多个类，用逗号分隔各个类

# my_car=Car('benz','amg',2021)
# print(my_car.get_descriptive_name())
# print('\n')
# my_tesla=ElectricCar('tesla','model 3',2021)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# import class_op                                                         # 导入整个class_op模块，推荐使用

# my_beetle=class_op.Car('volkswagen','beetle',2021)                      # 使用语法(module_name.ClassName)访问需要的类
# print(my_beetle.get_descriptive_name())
# print('\n')
# my_tesla=class_op.ElectricCar('tesla','model s',2021)
# print(my_tesla.get_descriptive_name())


# from class_op import *                                                  # 导入模块中的每个类，不推荐使用，容易引发难以诊断的错误


# from class_ba1 import Car   
# from class_op import ElectricCar                                        # 分别从每个模块中导入类

# my_beetle=Car('volkswaagen','beetle',2021)
# print(my_beetle.get_descriptive_name())
# print('\n')
# my_tesla=ElectricCar('tesla','model s',2021)
# print(my_tesla.get_descriptive_name())


# from class_op import ElectricCar as EC                                  # 给导入的类指定别名,也可对导入的模块指定别名

# my_tesla=EC('tesla','model s',2021)
# print(my_tesla.get_descriptive_name())
##########################################################



##########################################################
# from class_op import Restaurant as Res                                   # practice
# restaurant=Res('blue whale','chinese food')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# from class_op import Admin
# host=Admin('li','weijie',23)
# host.describe_user()
# host.privileges.show_privileges()
######################################################



##############################################
# from random import randint                                               # 使用Python标准库中的模块random
# print(randint(1,6))                                                      # randint():随机生成一个给定范围内的整数

# from random import choice, randint
# players=['jimmy','joy','sam','lily','john']
# while players:
#     if len(players) > 2:
#         guy=choice(players)                                              # choice():随机返回给定列表中的一个元素
#         players.remove(guy)
#         print(guy)
#     else:
#         break
###########################################



#############################################
import random as R                                                          # practicce

class Die:
    """模拟骰子"""

    def __init__(self,sides=6):
        """初始化骰子的面数"""
        self.sides=sides
    
    def roll_die(self):
        """模拟一次投掷后向上点数"""
        point=R.randint(1,self.sides)
        print(f"The number is: {point}.")

# dice=Die(10)
# for i in range(10):
#     dice.roll_die()


# lotteries=['a',1,2,3,4,5,6,7,12,23,43,'b','r','s','t']
# prize=[]
# for i in range(4):
#     a=R.choice(lotteries)
#     lotteries.remove(a)
#     prize.append(a)
# print(f"If u got the {prize} u win.")


# my_ticket=[2,3,'a',43]
# prize=[]
# count=0
# while my_ticket != prize:                                                  # 模拟何时中彩票
#     lotteries=['a',1,2,3,4,5,6,7,12,23,43,'b','r','s','t']
#     prize=[]
#     for i in range(4):
#         a=R.choice(lotteries)                                              # 使用choice函数一个一个获取
#         lotteries.remove(a)
#         prize.append(a)
#     count+=1
# print(f"After buying {count} lotteries, you got the first prize!")


lotteries=['a',1,2,3,4,5,6,7,12,23,43,'b','r','s','t']
my_ticket=[2,3,'a',43]
count=0
while True:
    prize=R.sample(lotteries,4)                                            # 使用sample函数从列表中随机获取4个元素
    if prize != my_ticket:
        count+=1
    elif prize == my_ticket:
        break
print(f"After buying {count} lotteries, you got the first prize!")
#########################################################################
