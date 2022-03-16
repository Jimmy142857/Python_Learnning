###############################################
# from test_ba import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
#     first=input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last=input("Please give me a last name: ")
#     if last == 'q':
#         break
#     formatted_name=get_formatted_name(first,last)
#     print(f"Neatly formatted name: {formatted_name}.")


# import unittest
# from test_ba import get_formatted_name
# class NamesTestCase(unittest.TestCase):                        # 必须继承unittest.TestCase类
#     """测试test_ba内的函数"""

#     def test_first_last_name(self):
#         """能够正确处理像 Jimmy page 这样的名字吗？"""
#         formatted_name=get_formatted_name('jimmy','page')
#         self.assertEqual(formatted_name,'Jimmy Page')          # 断言方法：核实得到的结果是否与期望的结果一致
# if __name__ == '__main__':                                     # 导入的文件'test_ba'作为主程序运行时特殊变量'__name__'将被设置为'__main__'
#     unittest.main()                                            # 调用unittest.mian()来运行测试用例


# import unittest
# from test_ba import get_formatted_name_1
# class NamesTestCase(unittest.TestCase):                        
#     """测试test_ba内的函数"""

#     def test_first_last_name(self):
#         """能够正确处理像 Jimmy page 这样的名字吗？"""
#         formatted_name=get_formatted_name_1('jimmy','page')
#         self.assertEqual(formatted_name,'Jimmy Page')         
# if __name__ == '__main__':                                       # 测试未通过FAILED，显示缺少一个位置实参
#     unittest.main()                                              # 如果检查的条件没错，则说明导入的代码出现问题，应当修改导入的代码


import unittest
from test_ba import get_formatted_name_2
class NamesTestCase(unittest.TestCase):                        
    """测试test_ba内的函数"""

    def test_first_last_name(self):
        """能够正确处理像 Jimmy page 这样的名字吗？"""
        formatted_name=get_formatted_name_2('jimmy','page')         # 修改原函数后测试通过
        self.assertEqual(formatted_name,'Jimmy Page')         
if __name__ == '__main__':                                      
        unittest.main()                                             
