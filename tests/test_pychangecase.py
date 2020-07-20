import unittest
from pychangecase import pascal_case, camel_case, snake_case, capital_case, constant_case, dot_case, header_case, param_case, path_case, sentence_case, swap_case, upper_case_fist, upper_case, lower_case_fist, lower_case


class TestMain(unittest.TestCase):
    def test_pascal_case(self):
        self.assertEqual(pascal_case('helloWorld'), 'HelloWorld')
        self.assertEqual(pascal_case('string'), 'String')
        self.assertEqual(pascal_case('dot.case'), 'DotCase')
        self.assertEqual(pascal_case('PascalCase'), 'PascalCase')
        self.assertEqual(pascal_case('version 1.2.10'), 'Version_1_2_10')

    def test_camel_case(self):
        self.assertEqual(camel_case('HelloWorld'), 'helloWorld')
        self.assertEqual(camel_case('string'), 'string')
        self.assertEqual(camel_case('dot.case'), 'dotCase')
        self.assertEqual(camel_case('PascalCase'), 'pascalCase')
        self.assertEqual(camel_case('version 1.2.10'), 'version_1_2_10')

    def test_snake_case(self):
        self.assertEqual(snake_case('helloWorld'), 'hello_world')
        self.assertEqual(snake_case('string'), 'string')
        self.assertEqual(snake_case('dot.case'), 'dot_case')
        self.assertEqual(snake_case('PascalCase'), 'pascal_case')
        self.assertEqual(snake_case('version 1.2.10'), 'version_1_2_10')

    def test_capital_case(self):
        self.assertEqual(capital_case('string'), 'String')
        self.assertEqual(capital_case('dot.case'), 'Dot Case')
        self.assertEqual(capital_case('PascalCase'), 'Pascal Case')
        self.assertEqual(capital_case('version 1.2.10'), 'Version 1 2 10')

    def test_constant_case(self):
        self.assertEqual(constant_case('string'), 'STRING')
        self.assertEqual(constant_case('dot.case'), 'DOT_CASE')
        self.assertEqual(constant_case('PascalCase'), 'PASCAL_CASE')
        self.assertEqual(constant_case('version 1.2.10'), 'VERSION_1_2_10')

    def test_dot_case(self):
        self.assertEqual(dot_case('string'), 'string')
        self.assertEqual(dot_case('dot.case'), 'dot.case')
        self.assertEqual(dot_case('PascalCase'), 'pascal.case')
        self.assertEqual(dot_case('version 1.2.10'), 'version.1.2.10')

    def test_header_case(self):
        self.assertEqual(header_case('string'), 'String')
        self.assertEqual(header_case('dot.case'), 'Dot-Case')
        self.assertEqual(header_case('PascalCase'), 'Pascal-Case')
        self.assertEqual(header_case('version 1.2.10'), 'Version-1-2-10')

    def test_param_case(self):
        self.assertEqual(param_case('string'), 'string')
        self.assertEqual(param_case('dot.case'), 'dot-case')
        self.assertEqual(param_case('PascalCase'), 'pascal-case')
        self.assertEqual(param_case('version 1.2.10'), 'version-1-2-10')

    def test_path_case(self):
        self.assertEqual(path_case('string'), 'string')
        self.assertEqual(path_case('dot.case'), 'dot/case')
        self.assertEqual(path_case('PascalCase'), 'pascal/case')
        self.assertEqual(path_case('version 1.2.10'), 'version/1/2/10')

    def test_sentence_case(self):
        self.assertEqual(sentence_case('string'), 'String')
        self.assertEqual(sentence_case('dot.case'), 'Dot case')
        self.assertEqual(sentence_case('PascalCase'), 'Pascal case')
        self.assertEqual(sentence_case('version 1.2.10'), 'Version 1 2 10')

    def test_swap_case(self):
        self.assertEqual(swap_case('string'), 'STRING')
        self.assertEqual(swap_case('dot.case'), 'DOT.CASE')
        self.assertEqual(swap_case('PascalCase'), 'pASCALcASE')

    # def test_title_case(self):
        # self.assertEqual(title_case('string'), 'String')
        # self.assertEqual(title_case('follow step-by-step instructions'), 'Follow Step-by-Step Instructions')

    def test_upper_case_fist(self):
        self.assertEqual(upper_case_fist('test'), 'Test')
        self.assertEqual(upper_case_fist('helloworld'), 'Helloworld')

    def test_upper_case(self):
        self.assertEqual(upper_case('test'), 'TEST')
        self.assertEqual(upper_case('helloworld'), 'HELLOWORLD')

    def test_lower_case_fist(self):
        self.assertEqual(lower_case_fist('TEST'), 'tEST')

    def test_lower_case(self):
        self.assertEqual(lower_case('TEST'), 'test')


if __name__ == '__main__':
    unittest.main()
