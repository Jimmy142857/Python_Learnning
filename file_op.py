################################
# filename='text_file/programming.txt'
#                                                             # open(,):提供两个实参，第一个为要打开文件的名称，第二个为指定模式(默认只读)
# with open(filename,'w') as file_object:                     # 'w'写入模式  'r'读取模式  'a'附加模式  'r+'读写模式
#     file_object.write("I love programming.")                # 如果写入的文件不存在，open()将自动创建它;已存在则自动清空再写入
#                                                             # 方法write()将字符串写入文件，python只能将字符串写入文本文件，若存储数值则要用str()转换


# with open(filename,'w') as file_object:
#     file_object.write("I love programming.")                # write()不会在写入文本末尾添加换行符，导致两行内容挤在一起
#     file_object.write("I love python.")


# with open(filename,'w') as file_object:
#     file_object.write("I love programming.\n")              # 包含换行符后换行成功
#     file_object.write("I love python.\n")


# with open(filename,'a') as file_object:                     # 附加模式，不会清空文件内容而是将写入的内容添加到文件末尾 
#     file_object.write("I also love C++.\n")                 # 如果指定文件不存在，则创建一个新文件
#     file_object.write("I hope i can master more computer languages.")
######################################



########################################
# filename='text_file/guest.txt'                              # practice
# prompt="Please input your name: "

# with open(filename,'w') as file_object:
#     file_object.write(input(prompt))


filename='text_file/guest_book.txt'
prompt_0="Please enter your name: "
prompt_1="Why do you like coding? "

with open(filename,'a') as file_object:
    while True:
        print("Welcome to the survey, enter 'q' to quit: ")

        name=input(prompt_0)
        if name == 'q':
            break
        reason=input(prompt_1)
        if reason == 'q':
            break

        file_object.write("Name: "+name.title()+"\n")
        file_object.write("Reason: "+reason.title()+"\n\n")
        print()
#####################################################

