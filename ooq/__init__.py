from ooq.ooq_utils import ModuleNotFoundIgnore

module_not_found_ignore = ModuleNotFoundIgnore()

source_module_names = [
    'tw'
]

# TODO: automate the following from source_module_names specs
with module_not_found_ignore:
    from ooq.tw import *
    from ooq import tw

