from dataclasses import dataclass

from annotation.anno import my_decorator


@dataclass
class User:
    id: str
    name: str
    age: int


def say(msg):
    print(f'Say: {msg}')


@my_decorator
def hello(name: str):
    say(f'Hello, {name}')
