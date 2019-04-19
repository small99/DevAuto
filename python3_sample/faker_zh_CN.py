# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from faker import Faker

""""
    基于Faker生成不同测试数据实例
"""


if __name__ == "__main__":

    # 创建faker实例，中文
    # 如果要生成其他语言，则将zh_CN改成对应的语言执行
    fake = Faker("zh_CN")

    print("------ 生成5个姓名-----")
    for _ in range(5):
        print(fake.name())

    print("\n------ 生成5个国家-----")
    for _ in range(5):
        print(fake.country())

    print("\n------ 生成5个条码-----")
    for _ in range(5):
        print(fake.ean8())  # 8位条形码
        print(fake.ean13())  # 13位条形码

    print("\n------ 生成5个颜色-----")
    for _ in range(5):
        print(fake.hex_color())

    print("\n------ 生成5个公司名-----")
    for _ in range(5):
        print(fake.company())

    print("\n------ 生成5个信用卡-----")
    for _ in range(5):
        print(fake.credit_card_number(card_type=None))  # 卡号
        print(fake.credit_card_provider(card_type=None))  # 卡的提供者
        print(fake.credit_card_security_code(card_type=None))  # 卡的安全密码
        print(fake.credit_card_expire())  # 卡的有效期
        print(fake.credit_card_full(card_type=None))  # 完整卡信息
        print("---" * 5)


    print("\n\n其他方法这里就不一一演示，请自信敲代码")
