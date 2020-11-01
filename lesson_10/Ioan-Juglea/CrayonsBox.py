from collections.abc import MutableSequence

class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]
    
    def __setitem__(self, index, value):
        self._crayons[index] = value
    
    def __delitem__(self, index):
        del self._crayons[index]
    
    def __str__(self):
        return str(self._crayons)
    
    def insert(self, index, value):
        self._crayons.insert(index, value)

crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
print(crayons_box[0])
crayons_box[1] = 'Orange'
print(crayons_box)
del crayons_box[2]
print(crayons_box)
crayons_box.insert(2, 'Aqua')
print(crayons_box)