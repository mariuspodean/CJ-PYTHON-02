          
class PrettyPrinter:

    def prettyprint(self):
        pretty_string = r'''
  _______________________________
 / \                             \
|   |                            |
 \_ |                            | '''
        if hasattr(self, 'ingredients'):

            pretty_name_string = '\n    |      ' + self.name  # pylint: disable=maybe-no-member
            nstr_len = len(pretty_name_string)
            pretty_string += pretty_name_string + ' ' * (34 - nstr_len) + '|'
            pretty_string += '\n    |                            |'

            for index, (key, value) in enumerate(self.ingredients.items(), start = 1):  # pylint: disable=maybe-no-member
                pretty_ingredient_string = '\n    |    ' + str(index) + '. ' + key.title() + ': ' + str(value)
                istr_len = len(pretty_ingredient_string)
                pretty_string += pretty_ingredient_string + ' ' * (34 - istr_len) + '|'

        else:
            pretty_name_string = '\n    |      The Fridge Contains:'
            nstr_len = len(pretty_name_string)
            pretty_string += pretty_string + ' ' * (34 - nstr_len) + '|'
            pretty_string += '\n    |                            |'

            for index, (key, value) in enumerate(self.products_fridge.items(), start=1): # pylint: disable=maybe-no-member
                pretty_ingredient_string = '\n    |    ' + str(index) + '. ' + key.title() + ': ' + str(value)
                istr_len = len(pretty_ingredient_string)
                pretty_string += pretty_ingredient_string + ' ' * (34 - istr_len) + '|'

        pretty_string += r'''
    |   _________________________|___
    |  /                            /
    \_/____________________________/ '''
        print(pretty_string)                      

