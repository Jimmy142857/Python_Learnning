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
# class NamesTestCase(unittest.TestCase):                               # 测试用例，必须继承unittest.TestCase类
#     """测试test_ba内的函数"""

#     def test_first_last_name(self):
#         """能够正确处理像 Jimmy page 这样的名字吗？"""
#         formatted_name=get_formatted_name('jimmy','page')
#         self.assertEqual(formatted_name,'Jimmy Page')                 # 断言方法：核实得到的结果是否与期望的结果一致
# if __name__ == '__main__':                                            # 导入的文件'test_ba'作为主程序运行时特殊变量'__name__'将被设置为'__main__'
#     unittest.main()                                                   # 调用unittest.mian()来运行测试用例


# import unittest
# from test_ba import get_formatted_name_1
# class NamesTestCase(unittest.TestCase):                        
#     """测试test_ba内的函数"""

#     def test_first_last_name(self):
#         """能够正确处理像 Jimmy page 这样的名字吗？"""
#         formatted_name=get_formatted_name_1('jimmy','page')
#         self.assertEqual(formatted_name,'Jimmy Page')         
# if __name__ == '__main__':                                           # 测试未通过FAILED，显示缺少一个位置实参
#     unittest.main()                                                  # 如果检查的条件没错，则说明导入的代码出现问题，应当修改导入的代码


# import unittest
# from test_ba import get_formatted_name_2
# class NamesTestCase(unittest.TestCase):                        
#     """测试test_ba内的函数"""

#     def test_first_last_name(self):
#         """能够正确处理像 Jimmy page 这样的名字吗？"""
#         formatted_name=get_formatted_name_2('jimmy','page')          # 修改原函数后测试通过
#         self.assertEqual(formatted_name,'Jimmy Page')         
# if __name__ == '__main__':                                      
#         unittest.main(argv=['ignored', '-v'], exit=False)            # 添加参数使得jupyter notebook也能运行                                       


# import unittest
# from test_ba import get_formatted_name_2
# class NamesTestCase(unittest.TestCase):                        
#     """测试test_ba内的函数"""

#     def test_first_last_name(self):
#         """能够正确处理像 Jimmy page 这样的名字吗？"""
#         formatted_name=get_formatted_name_2('jimmy','page')           
#         self.assertEqual(formatted_name,'Jimmy Page')   

#     def test_first_middle_last_name(self):                           # 添加新测试
#         """能够正确处理像 Jimmy larry page这样的名字吗？"""
#         formatted_name=get_formatted_name_2('jimmy','page','larry')      
#         self.assertEqual(formatted_name,"Jimmy Larry Page")
# if __name__ == '__main__':                                      
#         unittest.main(argv=['ignored', '-v'], exit=False)            # 添加参数使得jupyter notebook也能运行                                       
############################################################



############################################################
# import unittest
# from test_ba import city_country
# class CityTestCase(unittest.TestCase):
#     """测试city_country函数"""

#     def test_city_country(self):
#         """能正确处理Wuhan, China这样的值么？"""
#         city_info=city_country('wuhan','china')
#         self.assertEqual(city_info,'Wuhan, China')
# if __name__ == '__main__':
#     unittest.main(argv=['ignored','-v'],exit=False)


# import unittest
# from test_ba import city_country_1
# class CityTestCase(unittest.TestCase):
#     """测试city_country函数"""

#     def test_city_country(self):
#         """能正确处理Wuhan, China这样的值么？"""
#         city_info=city_country_1('wuhan','china')
#         self.assertEqual(city_info,'Wuhan, China')
    
#     def test_city_country_population(self):
#         """能正确处理Wuhan, china 10_000_000这样的值么"""
#         city_info=city_country_1('wuhan','china',10_000_000)
#         self.assertEqual(city_info,"Wuhan, China - Population:10000000")
# if __name__ == '__main__':
#     unittest.main(argv=['ignored','-v'],exit=False)
######################################################


#######################################################
# from test_ba import AnonymousSurvey                                      # 使用简单程序测试原类
# question = "What language did you first learn to speak?"                 # 定义一个问题，并创建一个调查
# my_survey = AnonymousSurvey(question)
# my_survey.show_question()                                                # 显示问题并存储答案
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
# print("\nThank you to everyone who participated in the survey!")         # 显示调查结果
# my_survey.show_results()


# import unittest
# from test_ba import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):                            # 测试用例
#     """针对AnoymousSurvey类的测试"""

#     def test_store_single_response(self):
#         """测试单个答案会被妥善存储"""
#         question = "What language did you first learn to speak?"
#         my_survey=AnonymousSurvey(question)                              # 要测试类的行为，需要创建其实例
#         my_survey.store_response('English')
#         self.assertIn('English',my_survey.responses)                     # assertIn(item,list)核实item在list中
# if __name__ == '__main__':
#     unittest.main(argv=['ignored','-v'],exit=False)


# import unittest
# from test_ba import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
#     """针对AnoymousSurvey类的测试"""

#     def test_store_single_response(self):
#         """测试单个答案会被妥善存储"""
#         question = "What language did you first learn to speak?"
#         my_survey=AnonymousSurvey(question)                              
#         my_survey.store_response('English')
#         self.assertIn('English',my_survey.responses)

#     def test_store_three_response(self):
#         """测试三个答案是否会被妥善存储"""
#         question = "What language did you first learn to speak?"
#         my_survey=AnonymousSurvey(question)
#         responses=['English','Spanish','Chinese']
#         for response in responses:
#             my_survey.store_response(response.title())
#         for response in responses:
#             self.assertIn(response,my_survey.responses)

# if __name__ == '__main__':
#     unittest.main(argv=['ignored','-v'],exit=False)


import unittest
from test_ba import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnoymousSurvey类的测试"""

    def setUp(self):                                                # 先运行setup()方法再运行各个以test_打头的方法
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)                           # 创建一个调查对象
        self.responses=['English','Spanish','Chinese']                     # 创建一个答案列表

    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        self.my_survey.store_response(self.responses[0])                              
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案是否会被妥善存储"""
        for response in self.responses:
            self.my_survey.store_response(response.title())
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
#################################################################