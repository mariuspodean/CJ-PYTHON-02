import contextlib


@contextlib.contextmanager
def just_some_exceptions(item):
    try:
        yield item
    except KeyError:
        error_message = "KeyError: This key does not exist"
    except IndexError:
        error_message = "IndexError: Index out of range"
    finally:
        if error_message:
            print(error_message)


my_dict = {
    'apple': 20,
    'orange': 30
}
with just_some_exceptions(my_dict) as ctx:
    print(ctx['apple'])
    print(ctx['pear'])

my_list = [10, 20, 30, 40, 50]
with just_some_exceptions(my_list) as ctx:
    print(ctx[0])
    print(ctx[100])
