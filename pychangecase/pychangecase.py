import re
from typing import Union, List, Tuple, Callable
from random import random

TransformHandler = Callable[[int, str], str]
Delimiter = str
Options = Tuple[str, str, TransformHandler, Delimiter]

DEFAULT_SPLIT_REGEXP = [r'([a-z0-9])([A-Z])', r'([A-Z])([A-Z][a-z])']


def replace(input: str, rule: Union[str, List[str]], value: str) -> str:
    if not type(rule) is list:
        rule = [rule]

    for r in rule:
        input = re.sub(r, value, input)

    return input


def no_case(input: str, options) -> str:
    result = replace(input, options['split_regex'],  r'\1\0\2')
    result = replace(result, re.compile(r'[^A-Z0-9]+', re.IGNORECASE), "\0")

    result = filter(lambda v: len(v) > 0, result.split("\0"))
    map_result = []
    for i, v in enumerate(result):
        map_result.append(options['transform'](v, i))

    return options['delimiter'].join(map_result)


def default_transform(input: str, index: int) -> str:
    return input.lower()


def snake_case(input: str) -> str:
    '''PascalCase => pascal_case'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': default_transform, 'delimiter': '_'})


def pascal_transform(input: str, index: int) -> str:
    first_char = input[0].upper()
    lower_chars = input[1:].lower()
    if index > 0 and first_char.isnumeric():
        return f'_{first_char}{lower_chars}'

    return f'{first_char}{lower_chars}'


def pascal_case(input: str) -> str:
    '''helloWorld => HelloWorld'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': pascal_transform, 'delimiter': ''})


def camel_transform(input: str, index: int) -> str:
    if index == 0:
        return input.lower()
    return pascal_transform(input, index)


def camel_case(input: str) -> str:
    '''PascalCase => pascalCase'''
    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': camel_transform, 'delimiter': ''})


def capital_transform(input: str, index: int) -> str:
    return upper_case_fist(input.lower())


def capital_case(input: str) -> str:
    '''PascalCase => Pascal Case'''
    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': capital_transform, 'delimiter': ' '})


def constant_transform(input: str, index: int) -> str:
    return input.upper()


def constant_case(input: str) -> str:
    '''PascalCase => PASCAL_CASE'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': constant_transform, 'delimiter': '_'})


def dot_case(input: str) -> str:
    '''PascalCase => pascal.case'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': default_transform, 'delimiter': '.'})


def header_case(input: str) -> str:
    '''PascalCase => Pascal-Case'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': capital_transform, 'delimiter': '-'})


def param_case(input: str) -> str:
    '''PascalCase => pascal-case'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': default_transform, 'delimiter': '-'})

def path_case(input: str) -> str:
    '''PascalCase => pascal/case'''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': default_transform, 'delimiter': '/'})


def sentence_transform(input: str, index: int) -> str:
    input = input.lower()
    if index == 0:
        return upper_case_fist(input)
    return input

def sentence_case(input: str) -> str:
    '''PascalCase => Pascal case
    
    Transform into a lower case with spaces between words, then capitalize the string.
    '''

    return no_case(input, {'split_regex': DEFAULT_SPLIT_REGEXP, 'transform': sentence_transform, 'delimiter': ' '})


def upper_case_fist(input: str) -> str:
    '''helloworld => Helloworld'''

    return input[0].upper() + input[1:]


def upper_case(input: str) -> str:
    return input.upper()


def lower_case_fist(input: str) -> str:
    '''helloworld => Helloworld'''

    return input[0].lower() + input[1:]


def lower_case(input: str) -> str:
    return input.lower()

def sponge_case(input: str) -> str:
    result = []
    for ch in input:
        if random()>0.5:
            result.append(ch.upper())
        else:
            result.append(ch.lower())
    return ''.join(result)

def swap_case(input: str) -> str:
    result = []
    for ch in input:
        ch_lower = ch.lower()
        if ch == ch_lower:
            result.append(ch.upper())
        else:
            result.append(ch_lower)
    return ''.join(result)

def title_case(input: str) -> str:
    '''

    @see https://github.com/blakeembrey/change-case/blob/master/packages/title-case/src/index.ts
    '''
    SMALL_WORDS = re.compile(r'\b(?:an?d?|a[st]|because|but|by|en|for|i[fn]|neither|nor|o[fnr]|only|over|per|so|some|tha[tn]|the|to|up|upon|vs?\.?|versus|via|when|with|without|yet)\b', re.IGNORECASE)
    TOKENS = r'[^\s:–—-]+|.'
    WHITESPACE = r'\s'
    IS_MANUAL_CASE = r'.(?=[A-Z]|\..)'
    ALPHANUMERIC_PATTERN = r'[A-Za-z0-9\u00C0-\u00FF]'

    result = []
    # TODO
    return ''.join(result)
