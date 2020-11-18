from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]
    
    def __delitem__(self, index):
        del self._crayons[index]
        print (f'The color {self._crayons[index]} has been deleted')
    
    def __setitem__(self, index, value):
        self._crayons[index]=value
        print (f'Position {index} has been filled with the {value} color')
        
    def insert(self, index, value):
        self._crayons.insert(index, value)
        print (f'{value} has been added at position {index}')
    
    def __str__(self):
        return f'CrayonsBox: {self._crayons}'
    


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
print(crayons_box)

del crayons_box[1]

crayons_box[3]='Pink'

crayons_box.insert(2, 'Gray')

print(crayons_box)