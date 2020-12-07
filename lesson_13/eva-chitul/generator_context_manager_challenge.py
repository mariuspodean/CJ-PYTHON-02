
import contextlib


@contextlib.contextmanager
def just_some_exceptions():

    print('We are going to handle some exceptions')

    try:
        yield 'Here we go:'
    except KeyError:
        error_message = 'The Key does not exist. That is a DO NOT'
    except IndexError:
        error_message = 'Index is out of range! Back to the drawing board'
    finally:
        if error_message:
            print(error_message)


with just_some_exceptions() as exceptions_challenge:
    print('Finding exceptions')
    print(exceptions_challenge)

    list_example = ['one', 'two', 'three', 'four', 5, 6, 7, 8]
    print(list_example[0])
    print(list_example[20])


with just_some_exceptions() as other_exceptions_challenge:
    print('Finding more exceptions')
    print(other_exceptions_challenge)

    dict_example = {'Germany': 'Berlin', 'Belgium': 'Brussels', 'Romania': 'Cluj-Napoca'}
    print(dict_example['Germany'])
    print(dict_example['USA'])

with just_some_exceptions() as non_handled_exception:
    print('This exception may be a problem')
    print(non_handled_exception)

    divide = 100/0
    print('Do we see the problem?')