import operator
from abc import ABC, abstractmethod

from notification.persistence.base import DB


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Predicator(Command):

    def __init__(self, value):
        self.value = value

    stack = []
    comparison_ops = ['==', '<=', '>=', '<', '>']
    logical_ops = ['and', 'or']
    def is_command(self, value: str):
        return (self.comparison_ops + self.logical_ops).count(value) < 1

    def execute(self):
        split: list[str] = self.value.split(' ')

        for s in split:
            if self.is_command(s):
                update(pre_op, num)
            elif s in '+-*/':
                # num = 10 * num + int(s)


class SQLCommand(Command):

    def __init__(self, value):
        self.value = value

    def execute(self):
        return DB.execute_sql(self.value)


class CustomQueryCommand(Command):
    def execute(self):
        pass
        # sqlparse(query)
