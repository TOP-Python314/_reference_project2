from pathlib import Path
from pprint import pprint
from sys import path

tests_dir = Path(path[0]).parent
path.insert(1, str(tests_dir / 'prototypes'))

import model
import controller
# import view

# >>> pprint(
# ...     {k: v for k, v in model.__dict__.items() if not k.startswith('_')},
# ...     sort_dicts=False
# ... )
# {'base': <module 'model.base' from '...\\tests\\prototypes\\model\\base.py'>,
#  'kind': <module 'model.kind' from '...\\tests\\prototypes\\model\\kind.py'>,
#  'params': <module 'model.params' from '...\\tests\\prototypes\\model\\params.py'>,
#  'KindParameter': <class 'model.kind.KindParameter'>,
#  'MatureStage': <class 'model.kind.MatureStage'>,
#  'Kind': <class 'model.kind.Kind'>,
#  'Health': <class 'model.params.Health'>,
#  'Satiety': <class 'model.params.Satiety'>,
#  'Emotion': <class 'model.params.Emotion'>}


