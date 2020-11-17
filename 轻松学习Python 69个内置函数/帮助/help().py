# help([object])
# 启动内置的帮助系统（此函数主要在交互式中使用）。如果没有实参，解释器控制台里会启动交互式帮助系统。
#
# 如果实参是一个字符串，则在模块、函数、类、方法、关键字或文档主题中搜索该字符串，并在控制台上打印帮助信息。
#
# 如果实参是其他任意对象，则会生成该对象的帮助页。
def function(a, b):
    """这是测试函数的文档"""
    return a + b
# help(function)

class C:
    """这是测试类的文档"""
    attr = 123
    def m(self):
        """这是测试方法"""
        return 123
# help(C)
#
# 请注意如果在函数的形参列表中出现了斜杠 (/)，则它在发起调用 help() 的时候意味着斜杠之前的均为仅限位置形参。 更多相关信息，请参阅 有关仅限位置形参的 FAQ 条目。
#
# 请注意如果在函数的形参列表中出现了斜杠 (/)，则它在发起调用 help() 的时候意味着斜杠之前的均为仅限位置形参。
help(sum)
# 该函数通过 site 模块加入到内置命名空间。
#
# 在 3.4 版更改: pydoc 和 inspect 的变更使得可调用对象的签名信息更加全面和一致。