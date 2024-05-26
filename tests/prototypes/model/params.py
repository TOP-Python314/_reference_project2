__all__ = [
    'Health',
    'Satiety',
    'Emotion',
    # '',
]


import model.base as base


class Health(base.CreatureParameter):
    name = 'здоровье'
    
    def update(self) -> None:
        satiety = self._params[Satiety]
        satiety_crit = 0.25 * satiety._max
        if satiety.value <= satiety_crit:
            self.value -= self._delta


class Satiety(base.CreatureParameter):
    name = 'сытость'
    
    def update(self):
        self.value -= self._delta


class Emotion(base.CreatureParameter):
    ...

