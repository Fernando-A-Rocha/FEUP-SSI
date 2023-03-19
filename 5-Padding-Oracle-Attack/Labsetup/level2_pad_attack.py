#!/usr/bin/python3
import socket
from binascii import hexlify, unhexlify

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

class PaddingOracle:

    def __init__(self, host, port) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

        ciphertext = self.s.recv(4096).decode().strip()
        self.ctext = unhexlify(ciphertext)

    def decrypt(self, ctext: bytes) -> None:
        self._send(hexlify(ctext))
        return self._recv()

    def _recv(self):
        resp = self.s.recv(4096).decode().strip()
        return resp 

    def _send(self, hexstr: bytes):
        self.s.send(hexstr + b'\n')

    def __del__(self):
        self.s.close()


if __name__ == "__main__":
    oracle = PaddingOracle('10.9.0.80', 6000)

    # Get the IV + Ciphertext from the oracle
    iv_and_ctext = bytearray(oracle.ctext)
    IV    = iv_and_ctext[00:16]
    C1    = iv_and_ctext[16:32]  # 1st block of ciphertext
    C2    = iv_and_ctext[32:48]  # 2nd block of ciphertext
    C3    = iv_and_ctext[48:64]  # 3nd block of ciphertext
    print("C1:  " + C1.hex())
    print("C2:  " + C2.hex())
    print("C3:  " + C3.hex())

    ###############################################################
    # Here, we initialize D2 with C1, so when they are XOR-ed,
    # The result is 0. This is not required for the attack.
    # Its sole purpose is to make the printout look neat.
    # In the experiment, we will iteratively replace these values.
    D2 = bytearray(16)

    D2[0]  = C1[0]
    D2[1]  = C1[1]
    D2[2]  = C1[2]
    D2[3]  = C1[3]
    D2[4]  = C1[4]
    D2[5]  = C1[5]
    D2[6]  = C1[6]
    D2[7]  = C1[7]
    D2[8]  = C1[8]
    D2[9]  = C1[9]
    D2[10] = C1[10]
    D2[11] = C1[11]
    D2[12] = C1[12]
    D2[13] = C1[13]
    D2[14] = C1[14]
    D2[15] = C1[15]
    ###############################################################
    # In the experiment, we need to iteratively modify CC1
    # We will send this CC1 to the oracle, and see its response.
    CC1 = bytearray(16)

    CC1[0]  = 0x00
    CC1[1]  = 0x00
    CC1[2]  = 0x00
    CC1[3]  = 0x00
    CC1[4]  = 0x00
    CC1[5]  = 0x00
    CC1[6]  = 0x00
    CC1[7]  = 0x00
    CC1[8]  = 0x00
    CC1[9]  = 0x00
    CC1[10] = 0x00
    CC1[11] = 0x00
    CC1[12] = 0x00
    CC1[13] = 0x00
    CC1[14] = 0x00
    CC1[15] = 0x00

    ###############################################################
    # In each iteration, we focus on one byte of CC1.  
    # We will try all 256 possible values, and send the constructed
    # ciphertext CC1 + C2 (plus the IV) to the oracle, and see 
    # which value makes the padding valid. 
    # As long as our construction is correct, there will be 
    # one valid value. This value helps us get one byte of D2. 
    # Repeating the method for 16 times, we get all the 16 bytes of D2.
    
    secret = bytearray(16)
    
    Plain_text = ""

    secret[0]  = 0x00
    secret[1]  = 0x00
    secret[2]  = 0x00
    secret[3]  = 0x00
    secret[4]  = 0x00
    secret[5]  = 0x00
    secret[6]  = 0x00
    secret[7]  = 0x00
    secret[8]  = 0x00
    secret[9]  = 0x00
    secret[10] = 0x00
    secret[11] = 0x00
    secret[12] = 0x00
    secret[13] = 0x00
    secret[14] = 0x00
    secret[15] = 0x00
    
	
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
		              
    ###############################################################

    
    print("Plain_text:  " + Plain_text)
    print("\nPlain Text: " + bytes.fromhex(Plain_text).decode("ASCII"))
