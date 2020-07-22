import sys
from .pychangecase import pascal_case, camel_case, snake_case, capital_case, constant_case, dot_case, header_case, param_case, path_case, sentence_case, swap_case, upper_case_fist, upper_case, lower_case_fist, lower_case

_G = globals()
if len(sys.argv) >= 3 and sys.argv[1] in _G:
    case_func = _G[sys.argv[1]]
    for s in sys.argv[2:]:
        print(case_func(s))
