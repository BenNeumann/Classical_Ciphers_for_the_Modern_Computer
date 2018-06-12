#-------------------------------Vars-------------------------------
text = "test"                  #text you want to encrypt/decrypt
fileLocation = "test.jpg"          #location of the file you want to encrypt/decrypt
key = [1,1]                   #pick a key between [0-72,0-94]

#-------------------------------Constants-------------------------------

import binascii
keyAlphaDict = {1:1,2:48,3:32,4:24,6:16,7:68,8:12,9:74,11:26,12:8,13:22,
14:34,16:6,17:28,18:37,21:86,22:13,23:62,24:4,26:11,27:88,28:17,29:59,
31:46,32:3,33:72,34:14,36:66,37:18,39:39,41:51,42:43,43:42,44:54,46:31,
47:93,48:2,49:64,51:41,52:53,53:52,54:44,56:56,58:77,59:29,61:81,62:23,
63:92,64:49,66:36,67:78,68:7,69:84,71:91,72:33,73:82,74:9,77:58,78:67,
79:89,81:61,82:73,83:87,84:69,86:21,87:83,88:27,89:79,91:71,92:63,93:47,
94:94}

#-------------------------------Functions-------------------------------
def validKeyCheck(key):
	if 0 <= key[0] <= 71 and 0 <= key[1] <= 94:
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
		keyl = [list(keyAlphaDict)[key[0]],key[1]]
		ciphertext = ""
		for c in plaintext:
			cDec = ascii2Dec(c)
			if cDec<32 or cDec>126 : 
				ciphertext += c 
			else: 
				ciphertext += Dec2ascii(((((cDec-32) * keyl[0])+keyl[1])%95)+32)
		return ciphertext

def decryptText(ciphertext,key):
	if validKeyCheck(key)== False :
		return "Key is Not Valid!"
	else:
		keyl = [keyAlphaDict.values()[key[0]],key[1]]
		plaintext = ""
		for c in ciphertext:
			cDec = ascii2Dec(c)
			if cDec<32 or cDec>126 : 
				plaintext += c 
			else: 
				plaintext += Dec2ascii(((keyl[0]*(cDec-32 - keyl[1]))%95)+32)
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