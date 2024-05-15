__all__ = [
    'KindParameter',
    'MatureStage',
    'Kind',
    # '',
]


from collections.abc import Iterable
from numbers import Integral, Real
from typing import Type

import model.base as base


class KindParameter(base.Parameter):
    def __init__(
            self, 
            param_cls: Type[base.CreatureParameter], 
            min_: Real, 
            max_: Real, 
            delta: Real, 
            default: Real | None
    ):
        self.cls = param_cls
        super().__init__(min_, max_, delta)
        self.default = default


class MatureStage:
    def __init__(self, period: Integral, *parameters: KindParameter):
        self.days = period
        self.params = {
            param.cls: param
            for param in parameters
        }


class Kind(base.DictOfRanges):
    def __init__(self, filename: str, name: str, *mature_stages: MatureStage):
        self.file_name = filename.lower()
        self.str_name = name.title()
        
        phases = []
        left = right = 0
        for stage in mature_stages:
            right = left + stage.days - 1
            phases.append(((left, right), stage))
            left = right + 1
        super().__init__(phases)

