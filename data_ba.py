######################################
import json                                           # 模块json能够让你将简单python数据结构转存到文件中，并在文件再次运行时加载该文件数据

# numbers=[2,3,5,7,11,13]

# filename='json_file/numbers.json'                   # 使用拓展名json指出文件存储的数据为JSON格式
# with open(filename,'w') as f:
#     json.dump(numbers,f)                            # dump(,):接受两个实参，第一个为要存储的数据，第二个为可用存储的文件对象


# filename='json_file\\numbers.json'
# with open(filename) as f:
#     numbers=json.load(f)                            # load():加载文件数据，可实现程序之间的数据共享
# print(numbers)


# username=input("What is your name? ")

# filename='json_file\\username.json'
# with open(filename,'w') as f:                       # 写入
#     json.dump(username.title(),f)                                     
#     print(f"We will remember you when you come back, {username.title()}!")
# with open(filename) as f:
#     username=json.load(f)                           # 读取
#     print(f"\nWelcome back, {username}!")


# filename='json_file/username.json'
# try:
#     """
#     如果以前存储了用户名就加载它
#     否则提示用户输入用户名并存储
#     """   
#     with open(filename) as f:
#         username=json.load(f)
# except FileNotFoundError:
#     username=input("What is your name? ")
#     with open(filename,'w') as f:
#         json.dump(username,f)
#         print(f"We will rember you when you come back, {username.title()}!")
# else:
#     print(f"Welcome back, {username.title()}!")


# def greet_user():
#     """问候用户，并指出其名字"""                        # 重构:将代码划分为完成一系列具体工作的函数
#     filename='json_file\\username.json'               # 重构让代码更清晰，更容易理解，更容易拓展
#     try:                                              # 将代码整体放入一个函数中
#         with open(filename) as f:
#             username=json.load(f)
#     except FileNotFoundError:
#         username=input("What is your name? ")
#         with open(filename,'w') as f:
#             json.dump(username,f)
#             print(f"We will remember you when you come back, {username}!")
#     else:
#         print(f"Welcome back, {username}!")

# greet_user()


# def get_stored_username():                            # 将原函数块重构为两个函数
#     """如果存储了用户名就获取它"""
#     filename='json_file\\username.json'
#     try:
#         with open(filename) as f:
#             username=json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def greet_user():
#     """问候用户，并指出其名字"""
#     username=get_stored_username()                    # 函数中调用函数
#     if username:
#         print(f"Welcome, {username}!")
#     else:
#         username=input("What is your name? ")
#         filename='json_file\\username.json'
#         with open(filename,'w') as f:
#             json.dump(username,f)
#             print(f"we will remember you when you come back, {username}!")

# greet_user()


filename='json_file\\username.json'

def get_stored_username():                            # 将代码块重构为三个函数
    """如果存储了用户名就获取它"""                      # 每个函数都执行单一而清晰的任务
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入姓名并存储"""
    username=input("What is your name? ")
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """问候用户并得出其名字"""
    username=get_stored_username()
    if username:
        answer=input(f"Whether your name is {username}?(yes/no) ")
        if answer == 'yes':
            print(f"Welcome, {username}!")
        elif answer == 'no':
            user=get_new_username()
            print(f"We will rember you when you come back, {user}!")
        else:
            print("Enter yes/no only.")
    else:
        username=get_new_username()
        print(f"We will rember you when you come back, {username}!")

greet_user()
##############################################



#############################################
# filename='json_file\\favor_num.json'
# with open(filename,'w') as f:
#     num=input("What is your favorite number? ")
#     json.dump(num,f)
# with open(filename) as f:
#     number=json.load(f)
#     print(f"I know your favorite number! It's {number}.")


# filename='json_file\\favor_num.json'
# try:
#     with open(filename) as f:
#         number=json.load(f)
# except FileNotFoundError:
#     with open(filename,'w') as f:
#         number=input("What is your favorite number? ")
#         json.dump(number,f)
# else:
#     print(f"I know your favorite number! It's {number}.")
######################################################