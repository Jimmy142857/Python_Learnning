#################################################
# megicians=['alice','david','carolina']
# for megician in megicians:                                         # megician:临时变量,一般命名与列表名有关
#     print(megician)
#     print(f"{megician.title()}, that was a trick!\n")              # 每个缩进代码都是循环的一部分
# print("Thank you, everyone. That was a great show!")               # 没有缩进只执行一次 
## message="Hello world."
##     print(message)                                                # 不必要的缩进，报错
###############################################



########################################
# fruits=['apple','banana','pepperoni']                              # practice
# for fruit in fruits:
#     print(f"I like {fruit.title()}!")
# print("I really love fruit!")
#######################################



#########################################
# for value in range(1,6):                                           # range(,):从指定的第一个数开始，在指定的第二个值前停止
#     print(value)
# numbers=list(range(1,6))                                           # list():以range()为参数创建数字列表
# print(numbers)
# even_number=list(range(2,10,2))                                    # range(,,):第三个参数来指定步长
# print(even_number)
# print('\n')

# squares=[]
# for value in range(1,11):
#     square=value**2
#     squares.append(square)
# print(squares)
# print('\n')

# digits=[1,2,3,4,5,6,7,8,9]
# print(min(digits))                                                 # min,max,sum:处理数字列表的基本函数
# print(max(digits))
# print(sum(digits))
# print('\n')

# squares=[value**3 for value in range(1,11)]                        # 列表解析，可以通过表达式(value***3)来操作每一个数值元素
# print(squares)
###########################################



#################################################
# for value in range(1,21):                                           # practice
#     print(value)
# print('\n')

# big_list=list(range(1,10_000))
# for number in big_list:
#     print(number)
# print('\n')

# huge_list=list(range(1,1_000_000))
# print(min(huge_list))
# print(max(huge_list))
# print(sum(huge_list))
# print('\n')

# odd_list=list(range(1,20,2))
# for odd in odd_list:
#     print(odd)
# odd_list=[odd for odd in range(1,20,2)]
# print(odd_list)
# print('\n')

# three_list=list(range(3,30,3))
# for three in three_list:
#     print(three)
# three_list=[three for three in range(3,30,3)]
# print(three_list)
# print('\n')

# cube_list=[]
# for cube in range(1,11):
#     cube_list.append(cube**3)
#     print(cube_list[-1])
# cube_list=[ele**3 for ele in range(1,11)]
# for cube in cube_list:
#     print(cube)
###############################################



####################################################
# players=['lily','tom','tina','sam']
# print(players[0:3])                                      # print(list(a,b)):列表切片,输出列表中a到b-1的元素
# print(players[1:3])
# print(players[:3])                                       # 没有指定第一个索引，自动从表头开始
# print(players[1:])                                       # 没有指定第二个索引，一直输出到列表末尾
# print(players[-3:])                                      # 输出最后三名,复数索引返回离列表末尾相应距离元素,
# print(players,"\n")

# print("Here are the first three players in my team:")
# for player in players[:3]:                               # 输出前三个
#     print(player.title())


# my_foods=['beef','pizza','cola','cake']
# friend_foods=my_foods[:]                                 # list(:):复制列表，创建一个包含整个列表的切片
# friend_foods.append('hamburger')
# print("My favotite foods are:")
# print(my_foods,"\n")
# print("My friend's favorite foods are:")
# print(friend_foods,"\n")

# my_foods=['beef','pizzza','cola','cake']
# friend_foods=my_foods                                    # 直接赋值，使两个变量指向同一个列表,只能操作原列表
# friend_foods.append('hamburger')
# print(my_foods)
# print(friend_foods)
####################################################



##############################################
# names=['lily','joy','jimmy','jack']                      # practice
# print("The first three items in the list are:")
# print(names[:3])
# print("\nTwo items from the middle of the list are:")
# print(names[1:3])
# print("\nThe last three items in the list are:")
# print(names[-3:])


# my_foods=['beef','pizzza','cola','cake']
# friend_foods=my_foods[:]                            
# friend_foods.append('hamburger')
# print("\nMy favotite foods are:")
# for food in my_foods:
#     print(food)
# print("\nMy friend's favorite foods are:")
# for food in friend_foods:
#     print(food)
#################################################



#################################################
dimensions=(200,50)                                      # 元组:把不可变的列表称为元组，使用圆括号定义
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
print('\n')
# dimensions[0]=250                                      # 试图修改元组时报错

my_st=('shithead',)                                      # 只包含一个元素的元组,必须在元素后加上逗号
print(my_st[0])

dimensions=(200,50)
print("\nThe original dimension is:")
for dimension in dimensions:
    print(dimension)
dimensions=(400,10)                                      # 重新定义整个元组以改变元组元素
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
###########################################