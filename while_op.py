##############################################
# unconfirmed_users=['lily','joy','jimmy']                                   # 使用while循环处理列表                                
# confirmed_users=[]
# while unconfirmed_users:
#     current_user=unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)                                   # 在列表之间移动元素
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(f"\t{confirmed_user.title()}")
# print(unconfirmed_users)
# print(confirmed_users)

# pets=['dog','cat','dog','goldfish','cat','rabbit']
# print(pets)
# while 'cat' in pets:                                                       # 使用while循环删除为特定值的所有列表元素,不断删除'cat'
#     pets.remove('cat')                                                     # 不应使用for循环修改列表，修改过程中列表元素会整体移动，使某些元素漏掉
# print(pets)

# responses={}                                                               # 使用用户输入来填充字典
# polling_active=True                                                        # 标志
# while polling_active:
#     name=input("\nWhat's your name? ")
#     response=input("Which mountain would u like to clim? ")
#     responses[name]=response                                               # 将回答存储在字典中
#     repeat=input("Would u like to let another person respond?(yes/no) ")
#     if repeat == 'no':
#         polling_active=False
# print("\n--Poll Results--")
# print(responses)
# for name,response in responses.items():
#     print(f"{name.title()} would like to climb {response}.")
##########################################################



#################################
# sandwich_orders=['salad','vegetable','beaf']                                # practice
# finished_sanwichs=[]
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     finished_sanwichs.append(sandwich)
#     print(f"I made your {sandwich} sandwich!")
# print("\nThese sandwich have been made:")
# for sandwich in finished_sanwichs:
#     print(f"{sandwich.title()} sandwich")

# sandwich_orders=['pastrami','vegetable','pastrami','beaf','pastrami']
# print("\nSorry customers, all pastrami has been sold out!")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# finished_sandwiches=sandwich_orders[:]                                      # 复制列表
# print(finished_sandwiches)

places={}
while True:
    name=input("What's your name? ")
    place=input("If u could visit one place in the world,where would u go? ")
    places[name]=place
    choice=input("Continue or not?(yes/no) ")
    if choice == 'no':
        break
for name,place in places.items():
    print(f"\n{name.title()}'s dream place is {place}.")
input()
#####################################################