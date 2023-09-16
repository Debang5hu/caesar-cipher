#!/bin/bash/python

import getopt
from sys import argv


#encrypting
def ceasercipher(plaintext,shift):

    #ciphertext
    ciphertext=[]

    for character in plaintext:
        if character.islower()==True:
            ciphertext.append((ord(character) + shift - 97) % 26 +97)  #ascii value for lower alphabet is 97
        else:
            ciphertext.append((ord(character) + shift - 65) % 26 +65)  #65 for upper alphabet

    return ciphertext


if __name__=='__main__':
    
    #RULES!
    #Choose the value of "shift" between 1 and 25
    #L={a..z} || L={A..Z}

    #command line input
    arguments=argv[1:]
    try:
        args,null=getopt.getopt(arguments,"p:k:",["plaintext=","key="])
        for x,y in args:
            if x in ['-p','--plaintext']:
                plaintext=y
            if x in ['-k','--key']:
                shift=int(y)
    except:
        print('[+] Error!')
    
    
    #encrypting
    ciphertext=ceasercipher(plaintext,shift)
    
    encoded=[]

    for encodedtext in ciphertext:
        encoded.append(chr(encodedtext))

    #printing the cipher
    print(f'\n[+] cipher: {"".join(encoded)}')

