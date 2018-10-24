# -*- coding: utf-8 -*-

__author__ = "苦叶子"

"""

公众号: 开源优测

Email: lymking@foxmail.com

"""

import sys


# 定义print输出级别, 用于控制print输出
# 优先级 DEBUG > INFO > WARNING > ERROR
class Print:
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    PRINT_TIP = {DEBUG: "Debug", INFO: "Info", WARNING: "Warn", ERROR: "Error"}


# 全局print控制标志
PRINT_LEVEL = Print.ERROR


# 自定义print输出
# msg - 输出内容
# level - 输出级别控制
def print_console(msg, level=Print.INFO):
    filename = sys._getframe().f_code.co_filename
    func = sys._getframe().f_code.co_name
    line = sys._getframe().f_lineno
    if level >= PRINT_LEVEL:
        print("In File: %s, Function: %s @line: %s  %s: %s" % (filename, func, line, Print.PRINT_TIP[level], msg))


# 测试print_console
def test_print_console():
    print_console("这是debug输出...", Print.DEBUG)

    print_console("这是info输出....", Print.INFO)

    print_console("这是warning输出...", Print.WARNING)

    print_console("这是error输出", Print.ERROR)

    print("---" * 10)


if __name__ == "__main__":
    print("print输出示例")

    # 设置输出为DEBUG级别
    PRINT_LEVEL = Print.DEBUG
    test_print_console()

    # 设置输出为INFO级别
    PRINT_LEVEL = Print.INFO
    test_print_console()

    # 设置输出为Warning级别
    PRINT_LEVEL = Print.WARNING
    test_print_console()

    # 设置输出为ERROR级别
    PRINT_LEVEL = Print.ERROR
    test_print_console()

