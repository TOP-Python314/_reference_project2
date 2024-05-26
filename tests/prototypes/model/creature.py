__all__ = [
    'Creature',
    # '',
]


import model.base as base
import model.kind as kind


class Creature:
    def __init__(self, kind: kind.Kind, name: str):
        self.kind = kind
        self.name = name
        self.__age = 0
        self.params = self._params_dict()
    
    def _params_dict(self) -> base.Parameters:
        return base.Parameters(*(
            cls_cr_par(
                k_par._min, 
                k_par._max, 
                k_par._delta, 
                self.params[cls_cr_par].value if self.__age else k_par.default
            )
            for cls_cr_par, k_par in self.kind[self.__age].params.items()
        ))
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, new_age: int):
        old_MS = self.kind[self.__age]
        new_MS = self.kind[new_age]
        self.__age = new_age
        if old_MS is not new_MS:
            self.params = self._params_dict()
    
    def __repr__(self):
        params = ', '.join(
            f'{p.value}/{p._max}'
            for p in self.params.values()
        )
        return f'<{self.name} ({self.__age}): {params}>'
    
    def __str__(self):
        return '\n'.join(
            f'{p.name}: {p.value}'
            for p in self.params.values()
        )


