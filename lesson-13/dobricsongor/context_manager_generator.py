
from contextlib import contextmanager

@contextmanager
def just_some_exceptions(file):

    try:
        yield file
    except KeyError:
        print('Key error!!!')
    except IndexError:
        print('Index error!!!')
    finally:
        print('bye bye')
        print('*'*20)

     
my_list = [1,2,3,4,5] 

with just_some_exceptions(my_list) as f:
    print(f)
    print(f[0])
    print(f[5])

my_dict = {'first':1,'second':2}

with just_some_exceptions(my_dict) as g:
    print(g)
    print(g['second'])
    print(g['third'])

with just_some_exceptions('hello boss') as h:
    print(h)
    print(h+2)