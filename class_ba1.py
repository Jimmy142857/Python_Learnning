##############################
# class Car:
#     """一次模拟汽车的简单尝试"""

#     def __init__(self,make,model,year):
#         """初始化描述汽车的属性"""
#         self.make=make
#         self.model=model
#         self.year=year
    
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name.title()

# my_car=Car('audi','r8',2021)
# print(my_car.get_descriptive_name())


class Car:

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0                                        # 在方法__init__中给属性指定默认值0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,miles):                            
        """
        将里程表读数设置为指定的值
        禁止里程表读数往回调
        """                                                           # 设置方法，用来修改属性的值
        if miles >= self.odometer_reading:                            # 增加条件判断语句使属性值无法减小，以符合实际情况
            self.odometer_reading=miles
        else:
            print("You can't roll back an odometer.")
    
    def increment_odometer(self,mileage):                             # 设置方法对属性值进行递增
        """将里程表读数增加指定的量"""
        self.odometer_reading+=mileage
    
    def fill_gas_tank(self):
        """提醒车辆需要加油"""
        print("This car need to fill its gas tank.")
       
# my_new_car=Car('audi','r8',2021)                                      # 实例my_new_car
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# my_new_car.odometer_reading=23                                        # 通过实例直接访问并修改属性的值
# my_new_car.read_odometer()
# print('\n')

# my_new_car.update_odometer(100)                                       # 调用方法修改属性值
# my_new_car.read_odometer()
# print('\n')

# my_new_car.increment_odometer(2000)                                   # 调用方法对属性的值进行递增
# my_new_car.read_odometer()
#################################################



######################################################
class Restaurant:                                                        # practice
    """餐馆的简单信息"""

    def __init__(self,name,type):
        """设置餐馆名称和餐馆类型"""
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served=0                                             # 就餐人数属性
    
    def describe_restaurant(self):
        """打印餐馆信息"""
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"The restaurant's cuisine type is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        """显示餐馆正在营业"""
        print(f"The {self.restaurant_name.title()} is now opening.")
    
    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served=number
    
    def increment_number_served(self,num):
        """设置就餐人数增加量"""
        self.number_served+=num

# restaurant=Restaurant('blue whale','chinese food')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# print(f"\n{restaurant.number_served} people eat in this restaurant.")

# restaurant.number_served=100
# print(f"\nNow, {restaurant.number_served} people eat in this restaurant.")

# restaurant.set_number_served(120)
# print(f"\nNow, {restaurant.number_served} people eat in this restaurant.")

# restaurant.increment_number_served(30)
# print(f"\nNow, {restaurant.number_served} people eat in this restaurant.")


class User:
    """一个人的基本信息"""
    def __init__(self,first_name,last_name,age):
        """姓、名、年龄"""
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0                                                           # 登录次数属性

    def describe_user(self):
        """描述基本信息"""
        print(f"Person's name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Person's age: {self.age}")

    def greet_user(self):
        """一句问候语"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        """登录次数加一"""
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        """登录次数置零"""
        self.login_attempts=0

# user_0=User('li','weijie',23)
# print("\n",user_0.login_attempts)

# user_0.increment_login_attempts()
# print('\n',user_0.login_attempts)

# user_0.increment_login_attempts()
# print('\n',user_0.login_attempts)

# user_0.reset_login_attempts()
# print('\n',user_0.login_attempts)
#################################################