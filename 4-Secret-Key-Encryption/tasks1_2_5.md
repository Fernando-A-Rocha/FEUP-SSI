## Task 1: Frequency Analysis

In this task the objective is to find the original text behind a cipher-text and the encription key using frequency analysis.

Portion of the original Cipher text:

```
ytn xqavhq yzhu  xu qzupvd ltmat qnncq vgxzy hmrty vbynh ytmq ixur qyhvurn
vlvhpq yhme ytn gvrrnh bnniq imsn v uxuvrnuvhmvu yxx

ytn vlvhpq hvan lvq gxxsnupnp gd ytn pncmqn xb tvhfnd lnmuqynmu vy myq xzyqny
vup ytn veevhnuy mceixqmxu xb tmq bmic axcevud vy ytn nup vup my lvq qtvenp gd
ytn ncnhrnuan xb cnyxx ymcnq ze givasrxlu eximymaq vhcavupd vaymfmqc vup
v uvymxuvi axufnhqvymxu vq ghmnb vup cvp vq v bnfnh phnvc vgxzy ltnytnh ytnhn
xzrty yx gn v ehnqmpnuy lmubhnd ytn qnvqxu pmpuy ozqy qnnc nkyhv ixur my lvq
nkyhv ixur gnavzqn ytn xqavhq lnhn cxfnp yx ytn bmhqy lnnsnup mu cvhat yx
vfxmp axubimaymur lmyt ytn aixqmur anhncxud xb ytn lmuynh xidcemaq ytvusq
ednxuratvur

```

First, we ran the *freq.py* file to receive the statistics for n-grams present in the cipher text.

The partial oredered results that we obtained were:

- 1-gram: 'n', 'y', 'v'
- 2-gram: 'yt', 'tn', 'mu'
- 3-gram: 'ytn','vup','mur'

According to the resources given by the lab guide related to frequency analysis, the letter 'e' is at the top of the distribution of letters in the english language so the letter 'e' should correspond to the letter 'n' in the cipher text. Also, the top bigram is 'th' so that should correspond to the letters 'yt'.

Making this changes in the cipher text we reach this partial result:

So we know that 'y' should be letter 't' and 't' equals 'h'. Next, we look at the 1-gram 'v', 2-grams 'tn', 'mu', 3-grams 'vup', 'mur'.

- 'tn' -> 'he'
- 'v' -> 'a' as 'a' is the third letter at the top of the frequency distribution in the english language.
- 'mu' -> 'in' as 'in' is the third bigram to appear in the bigram frquency.
- That leads us to 'vup' -> 'and'.


Making this changes in the cipher text we reach this partial result:

```

THE xqaAhq TzhN  xN qzNDAd lHIaH qEEcq AgxzT hIrHT AbTEh THIq ixNr qThANrE
AlAhDq ThIe THE gArrEh bEEiq iIsE A NxNArENAhIAN Txx

THE AlAhDq hAaE lAq gxxsENDED gd THE DEcIqE xb HAhfEd lEINqTEIN AT ITq xzTqET
AND THE AeeAhENT IceixqIxN xb HIq bIic axceANd AT THE END AND IT lAq qHAeED gd
THE EcEhrENaE xb cETxx TIcEq ze giAasrxlN exiITIaq AhcaANDd AaTIfIqc AND
A NATIxNAi axNfEhqATIxN Aq ghIEb AND cAD Aq A bEfEh DhEAc AgxzT lHETHEh THEhE
xzrHT Tx gE A ehEqIDENT lINbhEd THE qEAqxN DIDNT ozqT qEEc EkThA ixNr IT lAq
EkThA ixNr gEaAzqE THE xqaAhq lEhE cxfED Tx THE bIhqT lEEsEND IN cAhaH Tx
AfxID axNbiIaTINr lITH THE aixqINr aEhEcxNd xb THE lINTEh xidceIaq THANsq
edExNraHANr

```

Having some partial words completed we have know more clues and looking at the frequency distribution resources we can finally complete our plain text discovery and find the encription key:

```
THE OSCARS TURN  ON SUNDAY WHICH SEEMS ABOUT RIGHT AFTER THIS LONG STRANGE
AWARDS TRIP THE BAGGER FEELS LIKE A NONAGENARIAN TOO

THE AWARDS RACE WAS BOOKENDED BY THE DEMISE OF HARVEY WEINSTEIN AT ITS OUTSET
AND THE APPARENT IMPLOSION OF HIS FILM COMPANY AT THE END AND IT WAS SHAPED BY
THE EMERGENCE OF METOO TIMES UP BLACKGOWN POLITICS ARMCANDY ACTIVISM AND
A NATIONAL CONVERSATION AS BRIEF AND MAD AS A FEVER DREAM ABOUT WHETHER THERE
OUGHT TO BE A PRESIDENT WINFREY THE SEASON DIDNT JUST SEEM EXTRA LONG IT WAS
EXTRA LONG BECAUSE THE OSCARS WERE MOVED TO THE FIRST WEEKEND IN MARCH TO
AVOID CONFLICTING WITH THE CLOSING CEREMONY OF THE WINTER OLYMPICS THANKS
PYEONGCHANG
```

## Task 2: Encryption using Different Ciphers and Modes

In this task the objective is to play with various encryption algorithms and modes.

More specifically we tried three different cipher types: *-aes-128-cbc, -bf-cbc,-aes-128-cfb*

*Out10.txt* being our output file from the previous task.

- 128 bit Advanced Encryption Service in Cipher Block Chaining Mode:

```sh

openssl enc -aes-128-cbc -e -in out10.txt -out cipher.bin \
-K 00112233445566778889aabbccddeeff \
-iv 01020304050607080102030405060708


```

- Blowfish in Cipher Block Chaining Mode:

```sh

openssl enc -bf-cbc -e -in out10.txt -out cipher.bin \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708


```

- 128 bit Advanced Encryption Service in Cipher Feedback Mode:

```sh

openssl enc -aes-128-cfb -e -in out10.txt -out cipher.bin \
-K 00112233445566778889aabbccddeeff \
-iv 01020304050607080102030405060708


```

Each of this commands produces a output file *cipher.bin* encrypted by each algorithm in a certain mode.



## Task 5: Error Propagation – Corrupted Cipher Text

- Create a file with at least 1000 bytes.

- Encrypt it with AES-128 cipher.

```sh

openssl enc -aes-128-... -e -in 1000bytes.txt -out cipherCorrupt.bin \
-K 00112233445566778889aabbccddeeff \
-iv 01020304050607080102030405060708


```


- Corrupt one byte (55th) using the Hess editor.

- Decrypt the corruption file using these four encryption modes.

```sh

openssl enc -aes-128-... -d -in cipherCorrupt.bin -out outText.txt \
-K 00112233445566778889aabbccddeeff \
-iv 01020304050607080102030405060708


```

- Before executing task:

### ECB encryption mode:

- Before executing task:

In ECB, the input plaintext is broken into numerious blocks and then each block is encrypted using a encryption key. So if a single byte in the cipher text is corrupted then only the corresponding plain text block is corrupted, the rest of the plain text is correct.

- Final answer:

After executing the task we verified that our answer before was correct since only the corresponding plain text block to the corrupt cipher block was corrupted.
The corrupted byte will affect only the decrypted block and not the rest of the file.

### CBC encryption mode:

- Before executing task:

We assume that since CBC uses the current block as input for the next block, decrypting a corrupted file may lead to more extensive damage than ECB mode (corrupt the rest of the plain text blocks).

- Final answer:

Our answer before executing the task was going in fact in the wrong direction since the CBC the corruption only propagates at most to two blocks.
As you only need the current and previous block for decryptin in CBC mode, the effect of a changed byte in the ciphertext, would only affect the present block and the following block.

### CFB encryption mode:

- Before executing task:

In CFB mode, a previous ciphertext block is encrypted and then combined with the plain text block to produce the next ciphertext block. Each ciphertext block depends on the previous one. Since the corruption size is 1 byte the decryption process can  recover all of the information that was not affected by the corruption which means that only the portion of the file up to the corrupted block will be recovered.

- Final answer:

Our answer was the correct one, using the CFB mode the corruption propagates to the rest of the blocks as the initial value for the feedback mechanism will be incorrect, leading to the incorrect decryption of the rest of the file.

### OFB encryption mode:

- Before executing task:

In OFB mode, the encryption process generates a key stream that is XORed with the plain text to produce the ciphertext. The key stream is generated independently of the plaintext. Since the corruption is only one byte on the cipher block that means that the corruption will not occur in other plain text blocks as the cipher block is not shared.

- Final answer:

Our answer was the correct since the corruption didn't propagate for reasons explained above.






