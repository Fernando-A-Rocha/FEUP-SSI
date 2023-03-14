## Task 3: Encryption Mode – ECB vs. CBC

For reference, we will be encrypting this image: `pic_original.bmp`

![pic_original.bmp](./Labsetup/Files/pic_original.bmp)

We start by encrypting the picture with ECB (Electronic Code Book) using:

```bash
openssl enc -aes-128-ecb -e -in pic_original.bmp -out pic_original_ecb.bmp -K 00112233445566778889aabbccddeeff # same key used in Task 2
```

We then use the following commands to preserve the header from the original BMP file, and keep the encrypted body so we can view it:

```bash
head -c 54 pic_original.bmp > header
tail -c +55 pic_original_ecb.bmp > body_cb
cat header body_cb > new_ecb.bmp
```

![new_ecb.bmp](./Labsetup/Files/new_ecb.bmp)

Same process but with CBC (Cipher Block Chaining):

```bash
openssl enc -aes-128-cbc -e -in pic_original.bmp -out pic_original_cbc.bmp -K 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708 # same key and IV used in Task 2
```

```bash
tail -c +55 pic_original_cbc.bmp > body_cbc
cat header body_cbc > new_cbc.bmp
```

![new_cbc.bmp](./Labsetup/Files/new_cbc.bmp)

The two shapes in the encrypted image are still clearly distinguishable when utilizing the ECB mode. This occurs because each ciphertext block in this mode is created by immediately applying the DES encryption process to the current plaintext block. Hence, there is no dependency between the present ciphertext block and any earlier plaintext blocks. This results in a significant drawback of this mode since similar plaintext blocks are converted to identical ciphertext blocks, which does not effectively conceal data patterns. Because of this, ECB mode offers no message confidentiality and is not advised for use with cryptographic protocols.

But, when utilizing the CBC method, the encrypted image is undetectable, making it impossible for someone without the encryption keys to decipher what is inside. In this method, the initialization vector (IV), which is a block of random bits of plaintext, is exclusive-OR'd (XOR'd) with the first block of the plaintext before the encryption key is applied. The first block of the ciphertext is the resulting block. The phrase "chaining" refers to the process of XORing each next block of plaintext with the one before it, followed by encryption. The same block of plaintext will no longer generate identical ciphertext as a result of this XOR operation.

---

The same experiment was repeated with a picture of FEUP to demonstrate this effect again.

![feup_original.bmp](./img/feup_original.bmp)

ECB mode:

![feup_ecb.bmp](./img/feup_ecb.bmp)

CBC mode:

![feup_cbc.bmp](./img/feup_cbc.bmp)

## Task 6: Initial Vector (IV) and Common Mistakes

### Task 6.1. IV Experiment

We create `lorem.txt` which contains some Lorem Ipsum text.

```bash
# different IVs
openssl enc -aes-128-cbc -e -in lorem.txt -out lorem_cbc1.txt -K 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
openssl enc -aes-128-cbc -e -in lorem.txt -out lorem_cbc2.txt -K 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060709
cmp -lb lorem_cbc1.txt lorem_cbc2.txt | wc -l # result: 2979 different bytes

# same IV
openssl enc -aes-128-cbc -e -in lorem.txt -out lorem_cbc3.txt -K 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
openssl enc -aes-128-cbc -e -in lorem.txt -out lorem_cbc4.txt -K 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
cmp -lb lorem_cbc3.txt lorem_cbc4.txt | wc -l # result: 0 different bytes
```

We can see the importance of using a different and unique IV for each encryption. If the same IV is used, the same ciphertext will be generated for the same plaintext.

### Task 6.2. Common Mistake: Use the Same IV

