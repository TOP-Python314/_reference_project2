from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from numbers import Integral, Real
from typing import Any, Type


# переменные для аннотаций
RangesIterator = Iterable[tuple[tuple[Integral, Integral], Any]]


class DictOfRanges(dict):
    def __init__(self, iterator: RangesIterator):
        for elem in iterator:
            key, value = elem
            left, right = key
            if isinstance(left, Integral) and isinstance(right, Integral):
                if left < right:
                    continue
                else:
                    raise ValueError('first integer must be lower than second integer')
            else:
                raise TypeError('key for DictOfRanges must be iterable of two integers')
        super().__init__(iterator)
    
    def __getitem__(self, key_to_find):
        if isinstance(key_to_find, Integral):
            for key in self:
                left, right = key
                if left <= key_to_find <= right:
                    return super().__getitem__(key)
            raise KeyError(f'{key_to_find} is out of all ranges')
        else:
            return super().__getitem__(key_to_find)
    
    # def __setitem__(self, key, value):
    #     raise NotImplementedError


class Parameter(ABC):
    def __init__(self, min_: Real, max_: Real, delta: Real):
        if min_ <= max_:
            self._min = min_
            self._max = max_
        else:
            raise ValueError("'min' arg must be lower or equal than 'max' arg")
        self._delta = delta


class CreatureParameter(Parameter):
    name: str
    
    def __init__(
            self, 
            min_: Real, 
            max_: Real, 
            delta: Real, 
            value: Real,
    ):
        super().__init__(min_, max_, delta)
        self._params: 'Parameters'
        self.__value = value
    
    @property
    def range(self) -> tuple[Real, Real]:
        return self._min, self._max
    
    @property
    def value(self) -> Real:
        return self.__value
    
    @value.setter
    def value(self, new_value: Real):
        if new_value < self._min:
            self.__value = self._min
        elif self._max < new_value:
            self.__value = self._max
        else:
            self.__value = new_value
    
    @abstractmethod
    def update(self) -> None:
        pass


class Parameters(dict):
    def __init__(self, *params: CreatureParameter):
        for param in params:
            self[param.__class__] = param
    
    def __setitem__(
            self, 
            key: Type[CreatureParameter], 
            value: CreatureParameter
    ):
        value._params = self
        super().__setitem__(key, value)
    
    def update(self):
        for param in self.values():
            param.update()



