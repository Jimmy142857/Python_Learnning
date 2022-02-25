####################################
# message=input("Tell me something, I will repeat it back to you:")              # input(a):接收第一个参数——提示a,并打印出来   
# print(message)                                                                 # 用户输入并按回车键后，将输入当作字符串，赋给message

# name=input("please enter your name: ")                                         # 提示应该清晰易懂
# print(f"Hello, {name.title()}!")

# prompt="If you tell us who you are,we can personalize the message you see."
# prompt+="\nWhat is your first name? "
# name=input(prompt)                                                             # 提示过长时可将提示赋给一个变量
# print(f"Hello, {name.title()}!")

# height=input("How tall are you, in inches? ")
# height=int(height)                                                             # int():将字符串转化为整型
# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou will be able to ride when u are a little older.")

# prompt="Enter a number and i'll tell u if its even or odd: "
# number=input(prompt)
# number=int(number)
# if number%2 == 0:                                                               # 取模(余数)运算符，可以判断一个数是奇数还是偶数
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
##########################################################



##################################################
# car=input("What kind of car do u want to rent? ")                               # practice
# print(f"\nLet me see if i can find a {car.upper()}.")

# book=input("How many people will join the meal? ")
# book=int(book)
# if book<=8:
#     print("\nWe have empty tables.")
# else:
#     print("\nSorry, we dont have empty tables.")

number=input("Enter a numer and i'll check if its an integral multiple of ten: ")
number=float(number)
if number%10 == 0:
    print(f"\nThe number {number} is an integral multiple of 10.")
else:
    print(f"\n{number} is not an integral multiple of 10.")
####################################################