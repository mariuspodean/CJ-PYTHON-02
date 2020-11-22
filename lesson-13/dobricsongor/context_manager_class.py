class JustSomeExceptions:

    def __init__(self,file):
        self.file = file
    
    def __enter__(self):
        print('welcome')
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        
        print('*'*20)
        if exc_type is IndexError:
            print('Index error!!!')
            return True
        if exc_type is KeyError:
            print('Key error!!!')
            return True
        

my_list = [1,2,3,4,5]
with JustSomeExceptions(my_list) as f:
    print(f)
    print(f[0])
    print(f[5])


my_dict = {'first':1, 'second':2}
with JustSomeExceptions(my_dict) as g:
    print(g)
    print(g['second'])
    print(g['third'])


my_string = 'abcd'
with JustSomeExceptions(my_string) as h:
    print(h)
    print(h+2)