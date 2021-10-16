######################################
# #print(5/0)                                                   # traceback中异常对象为ZerroDivisionError


# try:
#     print(5/0)
# except ZeroDivisionError:                                     # try-except:如果try代码块中代码导致了异常
#     print("You cant divide by zero!")                         # 则查找与异常对象匹配的except代码块，并运行其中的代码


# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:                                                       # 使用异常避免崩溃
#         answer = int(first_number) / int(second_number)        # try-except-else: 不产生异常时执行else
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)


# filename='alice.txt'
# try:
#     with open(filename,encoding='utf-8') as f:                 # 引发了FileNotFoundError异常
#         contents=f.read()
# except FileNotFoundError:
#     print(f"Sorry, the {filename} does not exist.")            # 显示友好的错误消息


# filename='text_file/alice.txt'
# try:
#     with open(filename,encoding='utf-8') as f:                   # encoding:声明open使用'utf-8'读取文本       
#         contents=f.read()
# except FileNotFoundError:
#     print(f"Sorry, the {filename} does not exist.")
# else:
#     # 计算该文件大致包含多少单词
#     words=contents.split()                                       # split():根据一个字符串创建一个包含每个单词的列表,以空格为分隔符
#     num_words=len(words)
#     print(f"The file '{filename}' has about {num_words} words.")


# def count_words(filename):                                         # 定义一个函数用来计算文件中单词
#     """计算一个文件大致包含多少单词"""
#     try:
#         with open(filename,encoding='utf-8') as f:
#             contents=f.read()
#     except FileNotFoundError:
#         # print(f"\nSorry, the '{filename}' does not exist.")     
#         pass                                                       # pass:静默失败，在except代码块中告诉python什么都不做
#     else:
#         words=contents.split()
#         num_words=len(words)
#         print(f"\nThe '{filename}' has about {num_words} words.")

# filenames=['text_file/alice.txt','text_file/siddhartha.txt','text_file/moby_dick.txt','little_women.txt']
# for name in filenames:
#     count_words(name)
################################################



################################################
# prompt_0="Please enter two numbers and i will add them up."            # practice
# prompt_1="The first number: "
# prompt_2="The second number: "

# print(prompt_0)
# while True:
#     try:
#         number_1=int(input(prompt_1))
#     except ValueError:
#         print("Please make sure you enter a number.")
#         continue
#     else:
#         try:
#             numer_2=int(input(prompt_2))
#         except ValueError:
#             print("Please make sure you enter a number.")
#             continue
#         else:
#             sum=number_1+numer_2
#             break
# print(f"Sum: {sum}")


# def count_animals(filename):
#     """计算动物个数"""
#     try:
#         with open(filename,encoding='utf-8') as f:
#             names=f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the '{filename}' does not exist.")
#         # pass
#     else:
#         animals=names.split()
#         counts=len(animals)
#         print(f"There are {counts} animals here:")
#         for animal in animals:
#             print(animal)

# files=['text_file/cats.txt','text_file/dogs.txt']
# for file in files:
#     count_animals(file)
#     print('\n')


def word_frequency(filename,word):
    """NLP给定单词词频统计"""
    try:
        with open(filename,encoding='utf-8') as f:                # lower():转换字符串中所有大写字母为小写
            counts=f.read().lower().count(word)                   # count():用来确定特定的单词或短语在字符串中出现了多少次
            print(f"There are {counts} {word} in this article.")
    except FileNotFoundError:
        pass

word_frequency('text_file/alice.txt','alice')



# def word_frequency(filename):
#     """NLP文献词频自动统计"""
#     try:
#         with open(filename,encoding='utf-8') as f:
#             words=f.read().split()                             # 设想从一个文献中统计所有出现单词词频

#             for word in words:

#     except FileNotFoundError:
#         pass
#############################################