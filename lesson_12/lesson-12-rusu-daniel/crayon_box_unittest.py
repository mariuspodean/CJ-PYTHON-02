from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self.crayons = list(iterable)

    def __len__(self):
        return len(self.crayons)

    def __getitem__(self, index):
        return self.crayons[index]
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value
        
    def __delitem__(self, key):
        del self.__dict__[key]
        
    def insert(self, ii, val):
        self.crayons.insert(ii, val)
        
    


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
print(crayons_box)
print(crayons)
