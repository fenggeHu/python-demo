# py中args、kwargs用法
def say(tag, *args, **kwargs) -> str:
    msg = f'[{tag}]: {args} ->> {kwargs}'
    return msg


# 调用方式
m1 = say('tag', 1, 2, 3, name='my name', age=28)
print(m1)
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
