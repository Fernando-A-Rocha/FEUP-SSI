# Task 2

To perform this attack, we start by iterating all the possible values of the last byte of the first block of the cyphertext (C1[15]) in order to find the value for which the padding is valid according to the oracle.

![decrypt](decrypt.png)

The point is to force the cyphertext to decrypt to a plaintext message with a padding of one byte in order to determine the true last byte of plain text. When this value is determined (CC1[15]) the value of D2[15] can be calculated using the expression D2 = PAD ⊕ CC1 and P2 = C1 ⊕ D2. 
From this step, we repeat the same for each byte incrementing the padding and using the expression CC1 = PAD ⊕ D2 to calculate the new CC1 each time, bellow we can observe the values for 9 iterations with the purpose of decrypting 9 bytes of the message (3 bytes of padding and 6 of plaintext).


```python
# CC1 = PAD xor D2

# Iteration 2
    CC1[15] = 0xcc # 0x02 xor 0xce

# Iteration 3
    CC1[15] = 0xcd # 0x03 xor 0xce
    CC1[14] = 0x38 # 0x03 xor 0x3b

# Iteration 4
    CC1[15] = 0xca # 0x04 xor 0xce
    CC1[14] = 0x3f # 0x04 xor 0x3b
    CC1[13] = 0xf5 # 0x04 xor 0xf1

# Iteration 5
    CC1[15] = 0xcb # 0x05 xor 0xce
    CC1[14] = 0x3e # 0x05 xor 0x3b
    CC1[13] = 0xf4 # 0x05 xor 0xf1
    CC1[12] = 0x19 # 0x05 xor 0x1c

# Iteration 6
    CC1[15] = 0xc8 # 0x06 xor 0xce
    CC1[14] = 0x3d # 0x06 xor 0x3b
    CC1[13] = 0xf7 # 0x06 xor 0xf1
    CC1[12] = 0x1a # 0x06 xor 0x1c
    CC1[11] = 0x43 # 0x06 xor 0x45

# Iteration 7
    CC1[15] = 0xc9 # 0x07 xor 0xce
    CC1[14] = 0x3c # 0x07 xor 0x3b
    CC1[13] = 0xf6 # 0x07 xor 0xf1
    CC1[12] = 0x1b # 0x07 xor 0x1c
    CC1[11] = 0x42 # 0x07 xor 0x45
    CC1[10] = 0xeb # 0x07 xor 0xec

# Iteration 8
    CC1[15] = 0xc6 # 0x08 xor 0xce
    CC1[14] = 0x33 # 0x08 xor 0x3b
    CC1[13] = 0xf9 # 0x08 xor 0xf1
    CC1[12] = 0x14 # 0x08 xor 0x1c
    CC1[11] = 0x4d # 0x08 xor 0x45
    CC1[10] = 0xe4 # 0x08 xor 0xec
    CC1[9] = 0x92 # 0x08 xor 0x9a

# Iteration 9
    CC1[15] = 0xc7 # 0x09 xor 0xce
    CC1[14] = 0x32 # 0x09 xor 0x3b
    CC1[13] = 0xf8 # 0x09 xor 0xf1
    CC1[12] = 0x15 # 0x09 xor 0x1c
    CC1[11] = 0x4c # 0x09 xor 0x45
    CC1[10] = 0xe5 # 0x09 xor 0xec
    CC1[9] = 0x93 # 0x09 xor 0x9a
    CC1[8] = 0xc2 # 0x09 xor 0xcb

    
# D2 = PAD xor CC1
    D2[15] = 0xce # 0x01 xor 0xcf
    D2[14] = 0x3b # 0x02 xor 0x39
    D2[13] = 0xf1 # 0x03 xor 0xf2
    D2[12] = 0x1c # 0x04 xor 0x18
    D2[11] = 0x45 # 0x05 xor 0x40
    D2[10] = 0xec # 0x06 xor 0xea
    D2[9] = 0x9a # 0x07 xor 0x9d
    D2[8] = 0xcb # 0x08 xor 0xc3
    D2[7] = 0x08 # 0x09 xor 0x01
```

This makes our program output the true decrypted last 6 bytes of text, by xoring D2 and C1:
```
...
P2:  0000000000000088aabbccddee030303
```