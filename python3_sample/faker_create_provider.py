# -*- coding: utf-8 -*-

__author__ = "苦叶子"


"""
    实现一个简单的faker provider
"""

from faker import Faker


# 导入provider基类，我们的provider需要继承该类
from faker.providers import BaseProvider


# 创建一个我们的provider
class MyProvider(BaseProvider):
    def my_name(self):
        return "DeepTest"


if __name__ == "__main__":
    print("使用自定义Provider实例")

    fake = Faker('zh_CN')

    # 将自定义provider添加至fake
    fake.add_provider(MyProvider)

    # 调用自定义provider中方法，生成数据
    my_name = fake.my_name()

    print(my_name)
