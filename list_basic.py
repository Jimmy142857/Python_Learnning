############################################################
# bicycles=['trek','cannodale','redline','specialized']        # 列表元素可以为数字，字符，字符串等
# print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[3],bicycles[-1],bicycles[-2])                 # 索引最后一个元素可以指定为-1；倒数第二个为-2
# print('\n')
# message=f"My first bicycle was a {bicycles[2].title()}."     # 可以像使用变量一样使用列表各个值
# print(message)
# print('\n')
# names=['Jimmy','Joy','Zf']
# print(f"Nice to meet u,{names[0]}!\n"
#       f"Nice to meet u,{names[1]}!\n"
#       f"Nice to meet u,{names[-1]}!")


# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0]='ducati'                                      # 修改列表元素
# print(motorcycles)
# motorcycles.append('honda')                                  # append(元素):给列表末尾附加一个元素
# print(motorcycles)
# print('\n')
# motorcycles=[]                                               # 初始化空列表
# motorcycles.append('honda')                                  # append()动态的创建列表
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# motorcycles.insert(0,'ducati')                               # insert(0,)在索引0初添加空间并将新元素存储于此，造成列表每个元素右移一个位置
# print(motorcycles)                                           # 添加位置在指定索引左侧


# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)                     
# del motorcycles[0]                                           # del():知道元素在列表中位置位置时删除该元素，以后无法访问该元素
# print(motorcycles)    
# del motorcycles[1]
# print(motorcycles)                                  


# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# popped_motorcycles=motorcycles.pop()                                 # pop():默认删除列表末尾的元素，并让你能够接着使用它（弹出栈顶元素）  
# print(motorcycles)
# print(popped_motorcycles)
# print('\n')
# motorcycles=['honda','yamaha','suzuki']
# last_owned=motorcycles.pop()
# print(f"The last motorcycle I owned is a {last_owned.title()}.")     # example
# motorcycles=['honda','yamaha','suzuki']
# first_owned=motorcycles.pop(0)                                       # pop(0):弹出列表的第一个元素，括号可指定任意位置
# print(f"The first motorcycle I owned is a {first_owned.title()}.")


# motorcycles=['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('ducati')                                        # remove():知道要删除元素的值时，删除第一个该元素
# print(motorcycles)
# print('\n')
# motorcycles=['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# too_expensive='ducati'                                              # 接着使用删除元素的值
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.\n")
#####################################################################



###########################################################
print("Here are the original three invited guys:")
names=['joy','jimmy','zf']                                          # practice
print(names)
new_guy="tom"
poor_guy=names.pop()
names.append(new_guy)
print(f"Sorry, {poor_guy.title()} can't come for dinner. "
      f"We invite {new_guy.title()} instead."
      f"\nThe members now are:")
print(names)
print('\n')

names.insert(0,'sam')
names.insert(2,'jack')
names.append('lily')
print("Here comes three new guys, now the list is:")
print(names)
print('\n')

print("Sorry eveybody,I can only invite two guys.")
poor1=names.pop()
poor2=names.pop()
poor3=names.pop()
poor4=names.pop()
print(f"I am sorry, {poor1}, {poor2}, {poor3}, and {poor4}.")
print(f"{names[0].title()} and {names[1].title()}, u two are the left.")

print('\n')
del names[0]
del names[0]
print(names)
##########################################################



#######################################################
# cars=['bmw','audi','toyota','subaru']
# print(f"{cars}\n")
# print(cars,'\n')  
# cars.sort()                                            # sort():从小到大，永久性的修改列表元素的排列顺序
# print(cars)
# print()                                                # print()：函数默认有一个换行参数 end='\n',可实现换行
# cars.sort(reverse=True)                                # reverse=True:传递参数，使函数功能反向
# print(cars)

# cars=['bmw','audi','toyota','subaru']
# print("\nHere is the original list:")
# print(cars)
# print("Here is the sorted list:")
# print(sorted(cars))                                    # sorted(list):保留列表元素原来的顺序，同时以从小到大的顺序呈现它们
# print("Here is the original list:")
# print(cars,'\n')

# cars=['bmw','audi','toyota','subaru']                  # reverse():永久性的反转列表元素的排列顺序
# print(cars)
# cars.reverse()
# print('\n',cars,sep='')                                # print()：函数默认有一个空格参数 end='\n'

# a=len(cars)                                            # len():快速获悉列表的长度
# print(a)
##############################################



###############################################
# places=['shanghai','beijing','shenzheng','guangzhou']   # practice
# print(sorted(places))
# print(sorted(places,reverse=True))
# print(places)
# print('\n')

# places.reverse()
# print(places)
# places.reverse()
# print(places)
# print('\n')

# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)
################################################