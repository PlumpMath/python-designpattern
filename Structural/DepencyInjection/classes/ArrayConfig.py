from .Parameters import Parameters
from .AbstractConfig import AbstractConfig


class ArrayConfig (Parameters, AbstractConfig):

    def get(self, key):
        if self.storage[key]:
            return self.storage[key]

    def set(self, key, value):
        self.storage[key] = value
