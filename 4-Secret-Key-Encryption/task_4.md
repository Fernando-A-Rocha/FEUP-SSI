# Task 4

* The modes that require padding are _EBC_ and _CBC_, while _CBF_ and _OBF_ do not. This happens because the first two modes need the key to be a multiple of the ciphers block size, for AES is 16 bytes. In contrary, the last two mentioned modes can encrypt and decrypt messages of any size, eliminating the need of fulfilling the previous condition and thus the necessity of using padding.


All of the encrypted files of 5, 10 and 15 bytes were respectivelly padded in order for their size to be a multiple of 16 during the AES encryption with the CBC mode.

* 5 bytes -> 16 bytes
* 10 bytes -> 16 bytes
* 16 bytes -> 32 bytes

Interestingly, the last file already had size 16 but was still padded with 16 bytes. This is because of PKCS padding rules that state that there must always be padding applied.

After decryption with the special flag _-nopad_ to prevent the removal of padding it was observed that the algorithm used the size of padding in bytes as the padding byte for each file respectively, the first used 0b which is 11 in hexadecimal, second was 06 which is 6 and third was 10 for 16.

```
earth ~/desktop/Labsetup % hexdump -C five.new
00000000  31 32 33 34 35 0b 0b 0b  0b 0b 0b 0b 0b 0b 0b 0b  |12345...........|
00000010
earth ~/desktop/Labsetup % hexdump -C ten.new
00000000  30 31 32 33 34 35 36 37  38 39 06 06 06 06 06 06  |0123456789......|
00000010
earth ~/desktop/Labsetup % hexdump -C sixteen.new
00000000  31 31 32 32 33 33 34 34  35 35 36 36 37 37 38 38  |1122334455667788|
00000010  10 10 10 10 10 10 10 10  10 10 10 10 10 10 10 10  |................|
00000020
```


