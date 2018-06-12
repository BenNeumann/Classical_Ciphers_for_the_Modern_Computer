#-------------------------------Vars-------------------------------
text = ""                  #text you want to encrypt/decrypt
fileLocation = "test.jpg"          #location of the file you want to encrypt/decrypt
key = 10                    #pick a key between 0-94

#-------------------------------Constants-------------------------------

import binascii

#-------------------------------Functions-------------------------------
def validKeyCheck(key):
	if 0 <= key <= 94:
		check = True
	else: 
		check = False
	return check

def ascii2Dec(ascii):
	return int(bin(int(binascii.hexlify(ascii), 16)),2)

def Dec2ascii(dec):
	return binascii.unhexlify('%x' % dec)

def encryptText(plaintext,key):
	if validKeyCheck(key)== False :
		return "Key is Not Valid!"
	else: 
		ciphertext = ""
		for c in plaintext:
			cDec = ascii2Dec(c)
			if cDec<32 or cDec>126 : 
				ciphertext += c 
			else: 
				ciphertext += Dec2ascii(((cDec + key-32)%95)+32)
		return ciphertext

def decryptText(ciphertext,key):
	if validKeyCheck(key)== False :
		return "Key is Not Valid!"
	else:
		plaintext = ""
		for c in ciphertext:
			cDec = ascii2Dec(c)
			if cDec<32 or cDec>126 : 
				plaintext += c 
			else: 
				plaintext += Dec2ascii(((cDec - key-32)%95)+32)
		return plaintext

def encryptFile(fileLocation,key):
	if validKeyCheck(key)== False :
		return "Key is Not Valid!"
	else:
		fileRead = open(fileLocation,'rb')
		encrypted = encryptText(fileRead.read().encode('base64'),key)
		fileRead.close()
		fileWrite = open(fileLocation,'wb')
		fileWrite.write(encrypted)
		return "File Encrypted!"

def decryptFile(fileLocation,key):
	if validKeyCheck(key)== False :
		return "Key is Not Valid!"
	else: 
		fileRead = open(fileLocation,'rb')
		decrypted = decryptText(fileRead.read(),key).decode('base64')
		fileRead.close()
		fileWrite = open(fileLocation,'wb')
		fileWrite.write(decrypted)
		return "File Decrypted!"

#-------------------------------Operators-------------------------------

#print encryptFile(fileLocation,key)
#print decryptFile(fileLocation,key)
#print encryptText(text,key)
#print decryptText(text,key)

#-----------------------------------------------------------------------