#!/usr/bin/python
from cryptography.fernet import Fernet
import sys

#Generate Fernet Key
def genFernet():
	global key
	global crypter
	key=Fernet.generate_key() #Symmetric Key generation
	#print(key)
	crypter=Fernet(key) #Fernet Object

	#Write Key to file
	with open('fernet_key.txt','wb') as f:
		f.write(key)

#Encrypt file using Fernet Key
def encryptFile(filename):
	global key
	global crypter
	newname="enc-"+filename
	
	with open(filename,'rb') as f :
		data = f.read()

	with open(newname,'wb') as n :
		crypt_data=crypter.encrypt(data)
		n.write(crypt_data)
		#print(f"[+] Encrypted {filename}")

#Decrypt file using Fernet Key
def decryptFile(filename):
	global key
	global crypter
#	with open('fernet_key.txt','wb') as f:
#		key=f.read()
#	crypter=Fernet(key)

	newname="dec-"+filename[4:]

	with open(filename,'rb') as f :
		data = f.read()

	with open(newname,'wb') as n :
		crypt_data=crypter.decrypt(data)
		n.write(crypt_data)
	#print(f"[+] Encrypted {filename}")


if __name__ == '__main__':
	genFernet()
	encryptFile("test.txt")
	decryptFile("enc-test.txt")