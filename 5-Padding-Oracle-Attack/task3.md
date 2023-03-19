## Task 3: Padding Oracle Attack (Level 2)

In this task the objective is to automate the process done in the previous task to find out all blocks of the plaintext.

Since the level-2 server listens to port 6000 we had access to one more 16 byte block of ciphertext, so we added the C3 variable to keep the extra block:

```python

    oracle = PaddingOracle('10.9.0.80', 6000)

    # Get the IV + Ciphertext from the oracle
    iv_and_ctext = bytearray(oracle.ctext)
    IV    = iv_and_ctext[00:16]
    C1    = iv_and_ctext[16:32]  # 1st block of ciphertext
    C2    = iv_and_ctext[32:48]  # 2nd block of ciphertext
    C3    = iv_and_ctext[48:64]  # 3nd block of ciphertext

```

Our approach to this task was to write a python algorithm to derive all the blocks of the secret message in one run. For this a list of lists containing pairs of the blocks used in each iteration was created:

```python
    blocks = [[C3,C2],[C2,C1],[C1,IV]]
```

So the algorithm focus on iterating through these pairs of blocks since each one is used to decipher the next one.

In the algorithm we used the following calculations to discover the secret byte and the CC1 byte to use in next iteration:



```Secret =  D2  ^ PreviousBlock ```, with  ```D2 -> valid_i(0...255) ^ bit(1...16) ```

```CC1[index] =  D2[index]  ^ Next_padding ```

This results in the following code to perform the automated attack:


```python

    blocks = [[C3,C2],[C2,C1],[C1,IV]]
    
    for [input_block, xor_block] in blocks:
        for bit in range(1,17):
            for i in range(256):
                CC1[16 - bit] = i
                status = oracle.decrypt(IV + CC1 + input_block)
                if status == "Valid":
                    D2[16-bit] = i ^ bit
                    secret[16-bit] = D2[16-bit] ^ xor_block[16-bit]
                    next_pad = bit + 1
                    for rev_index in range(1,next_pad):
                        CC1[16 - rev_index] = 	next_pad ^ D2[16-rev_index]
                    break
        Plain_text = secret.hex() + Plain_text
    
```

Executing the attack it leads us to the secret message, even after a new connection to the oracle:

![ExecutionResults](screenshots/DockerSetup.png)






    
