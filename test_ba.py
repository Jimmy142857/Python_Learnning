##########################################
def get_formatted_name(first,last):
    """生成简洁的姓名"""
    full_name=f"{first} {last}"
    return full_name.title()


def get_formatted_name_1(first,middle,last):
    """生成简洁的姓名"""
    full_name=f"{first} {middle} {last}"
    return full_name.title()


def get_formatted_name_2(first,last,middle=''):
    """生成简洁的姓名"""
    if middle:
        full_name=f"{first} {middle} {last}"
    else:
        full_name=f"{first} {last}"
    return full_name.title()
############################################



###########################################
def city_country(city,country):
    """返回城市国家简洁信息"""
    full_information=f"{city}, {country}"
    return full_information.title()


def city_country_1(city,country,population=''):
    """返回城市国家简洁信息"""
    if population:
        full_information=f"{city}, {country} - population:{population}"
    else:
        full_information=f"{city}, {country}"
    return full_information.title()
##########################################



############################################
class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
        
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response.title())
        
    def show_results(self):
        """显示收到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


class Employee:
    """雇员姓名年薪调查"""

    def __init__(self,first,last,pay):
        """存储姓名、年薪"""
        self.first=first
        self.last=last
        self.pay=pay

    def give_raise(self,add=5000):
        """默认将年薪增加5000"""
        self.pay+=add
###############################################