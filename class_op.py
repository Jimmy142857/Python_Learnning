##############################################
# class Car:                                                         # 创建子类时父类必须包含在当前文件中，且位于子类前面
#     """一次模拟汽车的简单尝试"""

#     def __init__(self,make,model,year):
#         """初始化描述汽车的属性"""
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0                                       

#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name.title()    
    
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print(f"This car has {self.odometer_reading} miles on it.")
    
#     def update_odometer(self,miles):                            
#         """将里程表读数设置为指定的值
#         禁止里程表读数往回调
#         """                                                          
#         if miles >= self.odometer_reading:                           
#             self.odometer_reading=miles
#         else:
#             print("You can't roll back an odometer.")
    
#     def increment_odometer(self,mileage):                             
#         """将里程表读数增加指定的量"""
#         self.odometer_reading+=mileage
    
#     def fill_gas_tank(self):
#         """提醒车辆需要加油"""
#         print("This car need to fill its gas tank.")


from class_ba1 import Car                                          # 在一个模块中导入另一个模块


# class ElectricCar(Car):                                          # 定义子类，必须在圆括号内指定父类名称
#     """电动汽车的独特之处"""                                      # 子类继承父类时，将自动获得父类所有属性和方法

#     def __init__(self,make,model,year):                          # 方法__init__():接受创建Car实例所需的信息
#         """初始化父类的属性"""
#         super().__init__(make,model,year)                        # super():特殊的函数，让你能够调用父类的方法
#                                                                  # 调用Car类的方法__init__(),让ElectricCar实例包含这个方法中定义的所有属性
                                                                 
# my_tesla=ElectricCar('tesla','model 3',2021)
# print(my_tesla.get_descriptive_name())


# class ElectricCar(Car):
#     """电动汽车的独特之处"""

#     def __init__(self,make,model,year):
#         """
#         初始化父类的属性
#         再初始化电动车特有的属性
#         """
#         super().__init__(make,model,year)
#         self.battery_size=75                                          # 添加新属性battery_size,只能在ElectricCar实例中使用
 
#     def describe_battery(self):                                       # 添加新方法
#         """打印一条描述电瓶容量的消息"""
#         print(f"This car has a {self.battery_size}-kwh battery.")
    
#     def fill_gas_tank(self):                                          # 重写一个与父类同名的方法，运行时只调用该方法，忽略父类中的方法
#         """电动汽车没有油箱"""
#         print("This car doesn't need a gas tank!")
      
 
# my_tesla=ElectricCar('tesla','model s',2021)

# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()                                           # 调用新方法
# print('\n')
# my_car=Car('audi','r8',2021)
# my_car.fill_gas_tank()
# my_tesla.fill_gas_tank()                                              # 执行重新定义过的方法
#####################################################



##################################################
class Battery:                                                          # 定义一个新类，用来存储电动车专门的属性和方法
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self,battery_size=75):                                 # 形参设定默认值
        """初始化电瓶属性"""
        self.battery_size=battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range=260
        elif self.battery_size == 100:
            range=315
        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性
        再初始化电动汽车的特有属性"""
        super().__init__(make,model,year)
        self.battery=Battery()                                          # 将Battery实例赋给属性self.battery

# my_tesla=ElectricCar('tesla','model 3',2021)

# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()                                   # 先找到属性，由于属性是实例，再调用实例中的方法
# my_tesla.battery.get_range()
# print('\n')

# my_tesla.battery.battery_size=100
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
########################################################



#######################################################
class Restaurant:                                                         # practice
    """餐馆的简单信息"""

    def __init__(self,name,type):
        """餐馆姓名、类型"""
        self.restaurant_name=name
        self.cuisine_type=type
    
    def describe_restaurant(self):
        """打印餐馆信息"""
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"The restaurant's cuisine type is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        """显示餐馆正在营业"""
        print(f"The {self.restaurant_name.title()} is opening.")

class IceCreamStand(Restaurant):
    """冰淇凌小店简单信息"""

    def __init__(self,name,type):
        """
        初始化父类属性
        再初始化子类特有属性
        """
        super().__init__(name,type)
        self.flavors=['chocolate','strawberry','vanilla']
    
    def show_toppings(self):
        print("The icecream has the following flavors:")
        for topping in self.flavors:
            print(topping.title())

# icecreamstand=IceCreamStand('D&Q','dessert')
# icecreamstand.describe_restaurant()
# icecreamstand.open_restaurant()
# icecreamstand.show_toppings()


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

# class Admin(User):
#     """管理员基本信息"""

#     def __init__(self,first_name,last_name,age):
#         super().__init__(first_name,last_name,age)
#         self.privileges=['can add post','can delete post','can ban user']
    
#     def show_privileges(self):
#         """显示管理员权限"""
#         print(f"{self.first_name} {self.last_name} has the following authorities:")
#         for authority in self.privileges:
#             print(authority)

# admin=Admin('li','weijie',23)
# admin.describe_user()
# admin.show_privileges()


class Privileges:
    """管理员权限"""

    def __init__(self,privileges=['can add post','can delete post','can ban user']):
        """初始化管理员几类权限"""
        self.privileges=privileges
    
    def show_privileges(self):
        """显示管理员权限"""
        print(f"The person has the following authorities:")
        for authority in self.privileges:
            print(authority)

class Admin(User):

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=Privileges()

# admin=Admin('li','weijie',23)
# admin.describe_user()
# admin.privileges.show_privileges()
########################################################