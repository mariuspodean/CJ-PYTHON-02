import unittest
from decorators import *

class TestDecorators(unittest.TestCase):
    
    def test_uppercase_decorator_is_returning_uppercased_string(self):
        expected_result = "GREETINGS WORLD!"
        assert greet("world") == expected_result, "Uppercase decorator did not transform the argument to uppercase"

    def test_if_division_is_safe(self):
        n1 = 4
        n2 = 0
        assert isinstance(divide(n1, n2), str), "The safe_divide decorator is not stopping division by 0"
    
    def test_division_is_correct(self):
        n1 = 4
        n2 = 2
        assert divide(n1, n2) == n1/n2, "The divide function returns an incorrect result"
    
    def test_second_greet_works_with_register_name_decorator(self):
        name = "John"
        assert greet_(name) == "Greetings John!", "The second greet function is not using the name parameter as expected"
        assert 'greet_' in print_registry, "The register decorator didn't add the greet_ function name to print_registry"
    
    def test_say_hello_function_takes_name_argument_and_returns_greeting(self):
        name = "John"
        assert say_hello(name) == "Hello John!", "The say_hello function is not using the name parameter as expected"

    def test_say_goodbye_function_works_with_register_decorator(self):
        name="John"
        assert say_goodbye(name) == "Goodbye John!", "The say_goodbye function is not using the name parameter as expected"
        assert 'say_goodbye' in print_registry, "The register decorator didn't add the say_goodbye function name to print_registry"

unittest.main()