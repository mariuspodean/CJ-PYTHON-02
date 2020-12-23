class just_some_exceptions():
    def __init__(self, item):
        self.item = item

    def __enter__(self):
        return self.item

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyError:
            print("KeyError: This key does not exist")
            return True
        if exc_type is IndexError:
            print("IndexError: Index out of range")
            return True


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
