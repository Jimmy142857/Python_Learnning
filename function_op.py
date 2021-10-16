####################################################
# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()                                       # return:将值返回到调用语句的代码行
# musician=get_formatted_name('jim','hendrix')                       # 提供一个变量将返回的值赋给它
# print(musician)

# def get_formatted_name(first_name,last_name,middle_name=''):       # 提供默认值，让实参变成可选的
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name=f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name=f"{first_name} {last_name}"
#     return full_name.title()
# musician=get_formatted_name('jim','hendrix')                       # 没有中间名时
# print(musician)
# musician=get_formatted_name('john','hokker','lee')
# print(musician)

# def build_person(first_name,last_name,age=None):
#     person={'first':first_name,'last':last_name}                   # 定义一个字典接受名和姓
#     if age:
#         person['age']=age                                          # 如果实参有age则存储在字典中
#     return person
# musician=build_person('micheal','jackson',20)
# print(musician)

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# while True:                                                        # while循环中调用函数
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")                       # 添加消息告诉退出条件
#     f_name=input("First name:")
#     if f_name == 'q':
#         break
#     l_name=input("Last name:")
#     if l_name == 'q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)               # 调用函数
#     print(f"Hello, {formatted_name}!")
######################################################



#################################################
# def city_country(city,country):                                    # practice
#     city_info=f"{city.title()}, {country.title()}"
#     return city_info
# city_0=city_country('wuhan','china')
# city_1=city_country('shanghai','china')
# city_2=city_country('new york','america')
# print(f"{city_0}\n{city_1}\n{city_2}")

# def make_album(name,album,number=None):
#     albums={'name':name,'album':album}
#     if number:
#         albums['number']=number
#     return albums
# album_0=make_album('Micheal jackson','Thriller',10)
# album_1=make_album('Queen','Queen Rocks')
# album_2=make_album('萧敬腾','爱的自选时刻',8)
# print(f"{album_0}\n{album_1}\n{album_2}")

# while True:
#     print("\nPlease enter the name of the singer and the album:")
#     print("Enter 'f' to quit")
#     name=input("Singer's name:")
#     if name == 'f':
#         break
#     album=input("Album's title:")
#     if album == 'f':
#         break
#     album_col=make_album(name,album)
#     print(f"\nMy album:\n{album_col}")
################################################



##########################################
# def greet_users(names):                                                   # 向函数传递列表参数
#     """向列表中的每位用户发出简单的问候"""
#     for name in names:                                                    # 遍历收到的列表
#         msg=f"Hello, {name.title()}!"
#         print(msg)
# usersname=['joy','jimmy','zf']
# greet_users(usersname)

def print_models(unprinted_designs,completed_models):                       # 处理列表的函数
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models。
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):                                # 打印列表的函数
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)
# unprinted_designs=['phone case','robot pendant','dodecahedron']
# completed_designs=[]
# print_models(unprinted_designs,completed_designs)                         # 调用函数完成对列表的修改
# show_completed_models(completed_designs)                                  # 调用函数打印列表

# print_models(unprinted_designs[:],completed_designs)                      # 使用列表的副本作为实参，使得列表的原始值不变
# show_completed_models(completed_designs)    
####################################################



#################################
def make_pizza(size,*toppings):                                             # practice
    """"概述要制作的pizza"""                                                 # 可传递任意数量位置实参
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def show_msg(messages):
    for message in messages:
        print(message)


def send_messages(ori_message,send_messages):
    while ori_message:
            message=ori_message.pop(0)
            print(message)
            send_messages.append(message)


# ori_messages=['I am','hungry','and','thirsty']
# messages=[]
# send_messages(ori_messages,messages)
# print('\n')
# show_msg(ori_messages)
# show_msg(messages)

# send_messages(ori_messages[:],messages)
# print('\n')
# show_msg(ori_messages)
# show_msg(messages)
##############################################