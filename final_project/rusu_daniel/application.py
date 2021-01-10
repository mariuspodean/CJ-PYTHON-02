from collections.abc import Sequence
from collections.abc import MutableMapping
from cryptography.fernet import Fernet
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename='test.log')
logging.basicConfig(level=logging.INFO, filename='test.log')
logging.basicConfig(level=logging.critical, filename='test.log')


class AuthenticationMixin:
    user_pass = {}
    logger.info(f'Prepare dict')

    def check_account(self):
        counter = 0
        logger.debug(f'{counter} is starting ...')
        while counter < 6:
            logger.debug('While loop with 6 tries')
            user = input('Enter username:')
            passw = input('Enter password:')
            counter += 1
            if user in self.user_pass and self.user_pass[user] == passw:
                logger.debug(f'handling dict: {self.user_pass}')
                print(f'Valid Account')
                if counter == 5:
                    logger.info(
                        'If all accounts were checked succesfully stop while loop'
                    )
                    print('All the existing accounts were verified')
                    break
            else:
                print(f'Invalid Account!!! Wrong username or password!!!')
                if counter == 3:
                    logger.info('If 3 incorect accounts were introduced break')
                    print('The credentials were wrong 3 times, no more tries')
                    break


class Database(Sequence):
    def __init__(self, acc_name, acc_pass):
        self.acc_name = acc_name
        self.acc_pass = acc_pass
        logger.info(f'is initializing variables for the class')

    def __len__(self):
        return len(self.acc_name)

    def __getitem__(self, item):
        return self.acc_name[item]

    def __repr__(self):
        return f'Data for user account({self.acc_name},{self.acc_pass})'

    def __str__(self):
        logger.debug(f'return the {self.acc_name} and {self.acc_pass}')
        return f'Data for user account:\n-> Username: {self.acc_name},\n-> Password: {self.acc_pass}'

    #Overloading operator to create database from the users name
    def __add__(self, other):
        acc_name = self.acc_name + other.acc_name
        logger.debug(f'is overloading and return {acc_name}')
        return f'\nDatabase users: {acc_name}'

    def __radd__(self, other):
        acc_name = other + self.acc_name
        logger.debug(f'is overloading reverse add and return ...{acc_name}')
        return f'{acc_name}'


class Users(AuthenticationMixin, MutableMapping):
    def __init__(self):
        self.user_pass = {}
        logger.debug(f'{self.user_pass} is starting')

    def get_name(self):
        return self.user_pass

    def __getitem__(self, index):
        return self.user_pass[index]

    def __setitem__(self, user, passw):
        self.user_pass[user] = passw

    def __delitem__(self, item):
        del self.user_pass[item]

    def __iter__(self):
        return iter(self.user_pass)

    def __len__(self):
        return len(self.user_pass)

    def keys(self):
        return self.user_pass.keys()

    def items(self):
        return self.user_pass.items()

    def values(self):
        return self.user_pass.values()

    def __contains__(self, item):
        return item in self.user_pass

    def add_account(self, account):
        self.user_pass[account.acc_name] = account.acc_pass

    def remove_account(self, account):
        del self.user_pass[account.acc_name]

    def __repr__(self):
        return f'User({self.user_pass})'

    def __str__(self):
        logger.debug(f'is done and returning: {self.user_pass} ')
        return f'Accounts{self.user_pass}'


class Encryptor():
    def key_create(self):
        key = Fernet.generate_key()  # The key will be type bytes
        logger.debug(f'Is done and generates key {key}')
        return key

    def key_write(self, key, key_name):
        logger.info(f'Writes key')
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        logger.info(f'Loads key')
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def file_encrypt(self, key, original_file, encrypted_file):

        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()  # Read the bytes of the input file

        try:
            encrypted = f.encrypt(original)

            with open(encrypted_file, 'wb') as file:
                file.write(encrypted)  # Write the bytes of the input file

        except UnicodeEncodeError:
            logger.critical('Unicode error appeard for encoding')
            print('Encode related error')

    def file_decrypt(self, key, encrypted_file, decrypted_file):

        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()  # Read the bytes of the input file

        try:
            decrypted = f.decrypt(encrypted)
            with open(decrypted_file, 'wb') as file:
                file.write(decrypted)  # Write the bytes of the input file
        except UnicodeDecodeError:
            logger.critical('Unicode error appeard for decoding')
            print('Decode relate error')


@contextmanager
def customFileOpen(filename, method):
    """Custom context manager for opening a file."""
    f = open(filename, method)
    try:
        yield f
    except ValueError:
        logger.critical(f'Value error')
        print("Oops!  That was not a valid value.  Try again...")
    finally:
        f.close()
