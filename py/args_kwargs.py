# py中args、kwargs用法
def say(tag, *args, **kwargs) -> str:  # python不会强制检查返回类型，此处指定的返回类型与实际返回值不符，不影响程序运行
    msg = f'[{tag}]: {args} ->> {kwargs}'
    return tag, msg


# 调用方式
t, m1 = say('tag', 1, 2, 3, name='my name', age=28)
print(t)
# *args解包
tpl = (1, 2, 3)
m2 = say('tag', *tpl, name='my name', age=28)
print(m2)
# **kwargs解包
kv = {"name": "my name", 'age': 28}
m3 = say('tag', 1, 2, 3, **kv)
print(m3)
#
m4 = say('tag', *tpl, **kv)
print(m4)
