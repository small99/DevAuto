# -*- coding: utf-8 -*-

__author__ = "苦叶子"


"""
    生成中文实例
"""

import random

# 直接基于unicode码生成
# 在unicode码中，汉字范围是(0x4E00, 0x9FBF)


def unicode_zh():
    # 随机生成一个汉字码
    zh = random.randint(0x4E00, 0x9FBF)

    # 转换下,返回
    return chr(zh)


# 基于gbk2312码生成
# 在gbk2312码中，字符的编码采用两个字节组合
# 汉字第一个字节范围是(0xB0, 0xF7)
# 汉字第二个字节范围是(0xA1, 0xFE)


def gbk2312_zh():
    # 生成第一个字节
    first = random.randint(0xB0, 0xF7)
    # 生成第二个字节
    last = random.randint(0xA1, 0xFE)

    # 组合一下
    s = f'{first:x}{last:x}'

    # 转换成汉字
    zh = bytes.fromhex(s).decode('gb2312')

    # 返回
    return zh


# 主函数
if __name__ == "__main__":
    # 基于unicode模式生成10个汉字
    for _ in range(10):
        print(unicode_zh())

    print("------上面的汉字是不是很多不认识, 哈哈哈------\n\n")

    print("------下面的汉字是不是认识很多-------")

    # 基于gb2312模式生成10个汉字
    for _ in range(10):
        print(gbk2312_zh())
