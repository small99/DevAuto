# -*- coding: utf-8 -*-

__author__ = "苦叶子"

"""
    faker providers基本实例
"""

from faker import Faker

# 从providers中导入internet组件
from faker.providers import internet


if __name__ == "__main__":
    fake = Faker("zh_CN")

    # 添加provider组件
    fake.add_provider(internet)

    # 生成一个私有的ip
    ip = fake.ipv4_private()

    print(ip)
