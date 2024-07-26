"""
Python 中 @注解是否引入 wrapper 的原因及区别?
注解（装饰器）本质上是一个函数，它接收另一个函数作为参数，并返回一个新的函数。这个返回的函数就是我们常说的 wrapper。
1，引入 wrapper 的主要原因有：
修改函数的行为：
在函数执行前、后插入额外的逻辑，比如日志记录、性能监控、权限验证等。
改变函数的输入或输出参数。
添加元数据：
为函数添加额外的信息，方便后续处理，比如类型提示、文档字符串等。
AOP（面向切面编程）：
将横切关注点（如日志、事务）从业务逻辑中分离，提高代码模块化。
有 wrapper 和没有 wrapper 的区别
有 wrapper 的注解：
动态修改函数行为： 通过 wrapper 函数，可以在原函数执行前后插入自定义逻辑。
AOP 实现： wrapper 函数是实现 AOP 的核心机制。
灵活度高： 可以根据需要定制化 wrapper 函数。
2，没有 wrapper 的注解：
静态元数据： 主要用于提供函数的元数据信息，如类型提示、文档字符串等。
不改变函数行为： 不会影响函数的执行逻辑。
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before function call")
        result = func(*args, **kwargs)
        print("after function call")
        return result

    return wrapper
