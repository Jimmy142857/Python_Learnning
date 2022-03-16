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
