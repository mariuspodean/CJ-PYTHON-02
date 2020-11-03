# %load extending_mutable_sequence.py
from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __str__(self):
        return f'CrayonsBox contains: {self._crayons}'

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, index, crayon):
        self._crayons[index] = crayon
        return crayon

    def __delitem__(self, item):
        del self._crayons[item]
        return self._crayons

    def insert(self, index, new_crayon):
        return self._crayons.insert(index, new_crayon)

crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
print(crayons_box)

crayons_box.remove('Green')
print(crayons_box)

print(crayons_box[0])

crayons_box.insert(0, 'Black')
print(crayons_box)

print(len(crayons_box))

crayons_box[2] = "Orange"
print(crayons_box)

print(f'Is this a MutableSequence? {isinstance(crayons_box, MutableSequence)}')