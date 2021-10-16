#################################################
# with open('pi_digits.txt') as file_object:                           # open():接受一个参数即要打开文件的名称，并返回一个表示文件的对象
#     contents=file_object.read()                                      # read():一种方法，用来读取文件的全部内容，返回一个空字符串，显示为一个空行
# print(contents)
# print(contents.rstrip())                                             # 删除文件末尾空行


# with open('text_file/pi_digits.txt') as file_object:                 # 目标文件存在于代码所在目录的子文件夹内时
#     contents=file_object.read()                                      # 使用斜杠(/),或双反斜杠(\\),不使用反斜杠(\)
# print(contents.rstrip())


# file_path='C:\\Users\\Jimmy\\Desktop\\Python_code\\text_file\\pi_digits.txt'         
# with open(file_path) as file_object:
#     print(file_object.read())                                        # 绝对文件路径，不能使用反斜杠(\)


# filename='text_file/pi_digits.txt'

# with open(filename) as file_object:                                  # for循环,默认一行一行读取
#     for line in file_object:                                         # 原文件每行末尾都存在一个看不见的换行符，因此出现空白行
#         print(line)


# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())                                         # 消除空白行 


# with open(filename) as file_object:
#     lines=file_object.readlines()                                    # readlines():从文件中读取每一行并将其存储在一个列表中
# for line in lines:                                                   # 在with代码块外依然可以使用变量lines
#     print(line.rstrip())


# with open(filename) as file_object:
#     lines=file_object.readlines()
# pi_string_0=''
# pi_string_1=''
# for line in lines:
#     pi_string_0+=line.rstrip()                                        # 删除每行末尾换行符，忽略了每行左端缩进
#     pi_string_1+=line.strip()                                         # 删除段前段后所有空格
# print(pi_string_0)
# print(len(pi_string_0))
# print('\n')
# print(pi_string_1)
# print(len(pi_string_1))                                               # 读取文本文件时，python将其中所有文本解读为字符串，如果需要数值则需类型转换


# filename='text_file/pi_million_digits.txt'

# with open(filename) as file_object:
#     lines=file_object.readlines()
# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# print(pi_string[:50])
# print(len(pi_string))                                                  # 百万位圆周率

# birthday=input("Enter your birthday, in the form yymmdd: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("404 not found.")
######################################



#######################################
filename='text_file/learning_python.txt'

# with open(filename) as file_object:
#     contents=file_object.read()
#     print(contents.rstrip())
# print('\n')

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
# print('\n')

with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.strip())
print('\n')

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('python','C++').strip())                  # replace(,):替换字符串中特定单词为指定值，并不影响原字符串
###################################################