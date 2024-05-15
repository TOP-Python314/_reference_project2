from pathlib import Path
from pickle import dump
from sys import path

from model import *


kinds = [
    Kind(
        'cat',
        'кошка',
        MatureStage(
            5,
            KindParameter(Health, 0, 20, 0.5, 8),
            KindParameter(Satiety, 0, 25, 1.5, 0),
        ),
        MatureStage(
            40,
            KindParameter(Health, 0, 50, 0.4, None),
            KindParameter(Satiety, 0, 40, 1, None),
        ),
        MatureStage(
            20,
            KindParameter(Health, 0, 35, 0.6, None),
            KindParameter(Satiety, 0, 30, 0.8, None),
        ),
    ),
]


if __name__ == '__main__':
    
    test_data_dir = Path(path[0]).parent.parent / 'data'
    kinds_dir = test_data_dir / 'kinds'
    
    for kind in kinds:
        with open(kinds_dir / f'{kind.file_name}.kind', 'wb') as fileout:
            dump(kind, fileout)
    
    from pickle import load
    from pprint import pprint

    # >>> filein = open(kinds_dir / 'cat.kind', 'rb')
    # >>> obj = load(filein)
    # >>>
    # >>> type(obj)
    # <class 'model.kind.Kind'>
    # >>>
    # >>> pprint(obj)
    # {(0, 4): <model.kind.MatureStage object at 0x00000187E157A900>,
    # (5, 44): <model.kind.MatureStage object at 0x00000187E17E6C60>,
    # (45, 64): <model.kind.MatureStage object at 0x00000187E17E6BA0>}
    # >>>
    # >>> obj[2]
    # <model.kind.MatureStage object at 0x00000187E157A900>
    # >>>
    # >>> pprint(obj[2].params)
    # {<class 'model.params.Health'>: <model.kind.KindParameter object at 0x00000187E157BD40>,
    # <class 'model.params.Satiety'>: <model.kind.KindParameter object at 0x00000187E17E6C90>}

