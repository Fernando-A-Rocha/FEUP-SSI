from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def find_key(plaintext, ciphertext, wordlist, iv):

    plaintext = pad(plaintext.encode(), AES.block_size)
    biv = bytearray.fromhex(iv)
    
    for word in wordlist:
        key = word.rstrip('\n')
        key += '#' * (17 - len(word))
        key = bytes(key, 'utf-8')
        if(len(key) > 16):
            continue
        cipher = AES.new(key, AES.MODE_CBC, biv)
        enc_text = cipher.encrypt(plaintext)
        if(enc_text.hex() == ciphertext):
            return word

    return None

plaintext = "This is a top secret."
ciphertext = "764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2"
iv = "aabbccddeeff00998877665544332211"
dictionary = open('./4-Secret-Key-Encryption/Labsetup/Files/words.txt', 'r')

words = dictionary.readlines()

res = find_key(plaintext, ciphertext, words, iv)

print("The key is: " + str(res))


    

