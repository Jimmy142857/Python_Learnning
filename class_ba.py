###########################################
class Dog:                                                  # 定义一个名为Dog的类，依据约定首字母要大写
    """一次模拟小狗的简单操作"""                              # 字符串文档，对类的功能进行描述

    def __init__(self,name,age):                            # 特殊方法，开头末尾必须有2个下划线; 自动传递实参self，它是一个指向实例本身的引用
        """初始化属性name和age"""                            # 形参self必不可少，而且必须位于其他形参前面
        self.name=name                                      # 获取与形参name相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例
        self.age=age                                        # name,age称作属性

    def sit(self):                                          # 方法sit,类中所定义的函数
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):                                    # 方法roll_over
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


# my_dog=Dog('jimmy',2)                                     # 调用Dog类的方法__init__，创建一个表示特定小狗的实例
# print(f"My dog's name is {my_dog.name}")                  
# print(f"My dog is {my_dog.age} years old.")               # 使用句点表示法来访问实例的属性(实例-句点-属性值)

# my_dog.sit()                                              # 使用句点表示法来调用方法(实例-句点-方法)
# my_dog.roll_over()

# my_dog=Dog('Joy',10)
# your_dog=Dog('jimmy',12)                                  # 创建多个实例
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
#########################################



#######################################
class Restaurant:                                           # practice
    """餐馆的简单信息"""
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    
    def describe_restaurant(self):
        """打印餐馆信息"""
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"The restaurant's cuisine type is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        """显示餐馆正在营业"""
        print(f"The {self.restaurant_name.title()} is opening.")

# restaurant=Restaurant('blue whael','chinese food')
# print(restaurant.restaurant_name+"\n"+restaurant.cuisine_type+"\n")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


class User:
    """个人简单信息"""

    def __init__(self,first_name,last_name,age):
        """姓氏、名字、年龄"""
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def describe_user(self):
        """打印个人简单信息"""
        print(f"Person's name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Person's age: {self.age}")

    def greet_user(self):
        """打印个性化问候语"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

# user_0=User('li','weijie',23)
# user_1=User('luo','huan',24)

# user_0.describe_user()
# user_0.greet_user()
# print('\n')
# user_1.describe_user()
# user_1.greet_user()
######################################