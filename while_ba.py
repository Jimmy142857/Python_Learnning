######################################
# current_numer=1
# while current_numer <= 5:                                                       # while:循环不断运行直到条件不满足为止
#     print(current_numer)
#     current_numer+=1

# prompt="\nTell me someting, and i will repeat it back to you:"
# prompt+="\nEnter 'quit' to end the program. "
# message=''                                                                      # 赋初值使得循环能够开始
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         print(message)

# prompt="\nTell me someting, and i will repeat it back to you:"
# prompt+="\nEnter 'quit' to end the program. "
# active=True                                                                     # 标志:用于判断程序是否应该继续运行
# while active:
#     message=input(prompt)
#     if message == 'quit':
#         active=False
#     else:
#         print(message)

# prompt="\nPlease enter the name of a city u have visited:"
# prompt+="\n(Enter 'quit' when u are finished.) "
# while True:
#     city=input(prompt)
#     if city == 'quit':
#         break                                                                  # break:立即退出循环，不再运行余下代码
#     else:
#         print(f"I'd love to go to {city.title()}!")

# current_number=0
# while current_number<100:
#     current_number+=1
#     if current_number%2 == 0:
#         continue                                                               # continue:返回循环开头，根据条件测试结果决定是否继续执行循环
#     print(current_number)

# x=1
# while x <= 5:                                                                  # 无退出条件，导致无限循环，cpu占用爆表
#     print(x)
##########################################



####################################
# prompt="\nPlease enter your pizza ingredients:"                                # practice
# prompt+="\nEnter 'quit' to end. "
# active=True
# while active:
#     topping=input(prompt)
#     if topping == 'quit':
#         active=False
#     else:
#         print(f"We will add {topping} to your pizza.")

# age=10
# while age > 0 and age <= 100:
#     age=int(input("\nPlease enter your age: "))
#     if age < 3 and age >0:
#         print("Your price is $0.")
#     elif age <=12 and age >=3:
#         print("Your price is $10.")
#     elif age > 12 and age <=100:
#         print("Your price is $15.")
#     else:
#         print("Enter your real age, please.")

# active=True
# while active:
#     age=int(input("\nPlease enter your age: "))
#     if age < 3 and age >0:
#         print("Your price is $0.")
#     elif age <=12 and age >=3:
#         print("Your price is $10.")
#     elif age > 12 and age <=100:
#         print("Your price is $15.")
#     else:
#         print("Enter your real age, please.")
#         active=False

prompt="\nPlease enter your age: "
while True:
    age=int(input(prompt))
    if age <= 0 or age > 100:
        print("Enter your real age, please.")
        break
    elif age < 3:
        price=0
    elif age <= 12:
        price=10
    else:
        price=15
    print(f"\nYour price is ${price}.")
#############################################

