
# pychangecase

Porting nodejs [change-case](https://github.com/blakeembrey/change-case)

## Install

> pip install pychangecase

## Usage

```python
import pychangecase as cc
cc.snake_case('helloWorld') # hello_world
cc.camel_case('HelloWorld') # helloWorld
cc.constant_case('HelloWorld') # HELLO_WORLD
cc.capital_case('HelloWorld') # Hello World
cc.dot_case('HelloWorld') # hello.world
cc.header_case('HelloWorld') # Hello-World
cc.param_case('HelloWorld') # hello-world
cc.pascal_case('hello_world') # HelloWorld
cc.path_case('hello_world') # hello/world
cc.sentence_case('hello_world') # 'Hello world
cc.swap_case('helloWorld') # HELLOwORLD
```

## Test

> python -m unittest

## Build

> python setup.py sdist bdist_wheel
