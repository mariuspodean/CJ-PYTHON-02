import application
from application import Database,Users,customFileOpen,Encryptor

account1_details=('daniel','clam')
username1,password1=account1_details

account2_details=('bolt','12345')
username2,password2=account2_details

account3_details=('jhon','asterix19')
username3,password3=account3_details

account4_details=('kyle','domm13')
username4,password4=account4_details

account5_details=('james','blocked')
username5,password5=account5_details

account1 = Database(username1,password1)
account2 = Database(username2,password2)
account3 = Database(username3,password3)
account4 = Database(username4,password4)
account5 = Database(username5,password5)
print(account1)
print(account2)
print(account3)
print(account4)
print(account5)


d_base1=account1+account2
d_base2=d_base1+account3
d_base3=d_base2+account4
d_base_f=d_base3+account5
print(d_base_f)

account_list=Users()
account_list.add_account(account1)
account_list.add_account(account2)
account_list.add_account(account3)
account_list.add_account(account4)
account_list.add_account(account5)
account_list.remove_account(account5)
account_list.add_account(account5)
print(account_list)

with customFileOpen("data.txt", "wt") as f:
    f.write(str(account_list))
    
with customFileOpen("data.txt","r") as fi:
    print(fi.read())

encryptor=Encryptor()

mykey=encryptor.key_create()

encryptor.key_write(mykey, 'mykey.key')
#if other file or not a file is given loggin will show critical error

loaded_key=encryptor.key_load('mykey.key')

encryptor.file_encrypt(loaded_key, 'data.txt', 'encode_data.txt')

encryptor.file_decrypt(loaded_key, 'encode_data.txt', 'decode_data.txt')

account_list.check_account()