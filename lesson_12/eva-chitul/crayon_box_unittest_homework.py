
from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self.crayons = list(iterable)

    def __len__(self):
        return len(self.crayons)

    def __getitem__(self, index):
        return self.crayons[index]

    def __delitem__(self, index):
        print('Deleting the', self.crayons[index], 'crayon')
        del self.crayons[index]

    def __setitem__(self, index, item):
        print('Replacing the', self.crayons[index], 'crayon with', item)
        self.crayons[index] = item

    def insert(self, index, item):
        print('Adding', item, 'at position', index, 'in the crayon box')
        self.crayons.insert(index, item)

    def __str__(self):
        return f'The Crayon Box now contains: {self.crayons}'


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

