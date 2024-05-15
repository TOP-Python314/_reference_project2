from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from numbers import Integral, Real
from typing import Any


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
            self.min = min_
            self.max = max_
        else:
            raise ValueError("'min' arg must be lower or equal than 'max' arg")
        self.delta = delta


class CreatureParameter(Parameter):
    ...

