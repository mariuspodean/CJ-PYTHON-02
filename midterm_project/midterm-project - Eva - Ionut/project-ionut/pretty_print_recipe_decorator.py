def pretty_print_recipe(shop_list):

    def pretty_recipe(*args):
        if shop_list(*args):
            muffin_man_string = '''
 ........................................................
 :   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
 : _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
 :(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
 :  / o \    / o \    / o \    / o \    / o \    / o \  :
 : (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
 :   ,-.   ....................................   ,-.   :
 : _(*_*)_ :                                  : _(*_*)_ :
 :(_  o  _):          Shopping list:          :(_  o  _):
 :  / o \  :                                  :  / o \  :
 : (_/ \_) :                                  : (_/ \_) :'''

            list_shop = shop_list(*args)
            muffin_index = 1
            space_number = 46
            for index, (key, value) in enumerate(list_shop.items(), start=1):
                if muffin_index == 1:
                    muffin_string = ' :   ,-.   :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (space_number - len(muffin_string)) + ':   ,-.   :'
                elif muffin_index == 2:
                    muffin_string = ' : _(*_*)_ :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (space_number - len(muffin_string)) + ': _(*_*)_ :'
                elif muffin_index == 3:
                    muffin_string = ' :(_  o  _):   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (space_number - len(muffin_string)) + ':(_  o  _):'
                elif muffin_index == 4:
                    muffin_string = ' :  / o \  :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (space_number - len(muffin_string)) + ':  / o \  :'
                elif muffin_index == 5:
                    muffin_string = ' : (_/ \_) :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (space_number - len(muffin_string)) + ': (_/ \_) :'
                
                muffin_index += 1
                if(muffin_index > 5):
                    muffin_index = 1
            
            if muffin_index == 2:
                muffin_man_string += '\n : _(*_*)_ :                                  : _(*_*)_ :'
                muffin_index += 1
            if muffin_index == 3:
                muffin_man_string += '\n :(_  o  _):                                  :(_  o  _):'
                muffin_index += 1
            if muffin_index ==4:
                muffin_man_string += '\n :  / o \  :                                  :  / o \  :'
                muffin_index += 1
            if muffin_index == 5:
                muffin_man_string += '\n : (_/ \_) :                                  : (_/ \_) :'

            muffin_man_string += '''
 :   ,-.   :                                  :   ,-.   :
 : _(*_*)_ :                                  : _(*_*)_ :
 :(_  o  _):                                  :(_  o  _):
 :  / o \  :                                  :  / o \  :
 : (_/ \_) :..................................: (_/ \_) :
 :   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
 : _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
 :(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
 :  / o \    / o \    / o \    / o \    / o \    / o \  :
 : (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
 :......................................................: '''
            print(muffin_man_string)
        else:
            print('No shopping list!')
    return pretty_recipe