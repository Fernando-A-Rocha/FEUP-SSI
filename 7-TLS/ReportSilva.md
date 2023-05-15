## Task 1: TLS Client

### Task 1.a: TLS Handshake

Before a client and a server can communicate securely, several things need to be set up first, including what
encryption algorithm and key will be used, what MAC algorithm will be used, what algorithm should be
used for the key exchange, etc. These cryptographic parameters need to be agreed upon by the client and
the server. That is the primary purpose of the TLS Handshake Protocol. In this task, we focus on the TLS
handshake protocol.

#### Questions  

##### What is the cipher used between the client and the server?

We can know the cipher used between the client and the server by looking at the output of the print statement on line 22.
This statement prints the cipher suite that was negotiated during the handshake. A cipher suite is a combination of encryption and authentication algorithms that are used for securing the communication.

In this case the cipher used between the client and the server was ('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)

This means that the cipher suite is TLS_AES_256_GCM_SHA384, which uses AES-256 for encryption, GCM for mode of operation, and SHA-384 for message authentication. It also means that the TLS version is TLSv1.3 and the encryption key size is 256 bits.



##### Please print out the server certificate in the program.

```rust

Server certificate:
{'OCSP': ('http://ocsp.digicert.com',),
 'caIssuers': ('http://cacerts.digicert.com/DigiCertTLSRSASHA2562020CA1-1.crt',),
 'crlDistributionPoints': ('http://crl3.digicert.com/DigiCertTLSRSASHA2562020CA1-4.crl',
                           'http://crl4.digicert.com/DigiCertTLSRSASHA2562020CA1-4.crl'),
 'issuer': ((('countryName', 'US'),),
            (('organizationName', 'DigiCert Inc'),),
            (('commonName', 'DigiCert TLS RSA SHA256 2020 CA1'),)),
 'notAfter': 'Feb 13 23:59:59 2024 GMT',
 'notBefore': 'Jan 13 00:00:00 2023 GMT',
 'serialNumber': '0C1FCB184518C7E3866741236D6B73F1',
 'subject': ((('countryName', 'US'),),
             (('stateOrProvinceName', 'California'),),
             (('localityName', 'Los Angeles'),),
             (('organizationName',
               'Internet\xa0Corporation\xa0for\xa0Assigned\xa0Names\xa0and\xa0'
               'Numbers'),),
             (('commonName', 'www.example.org'),)),
 'subjectAltName': (('DNS', 'www.example.org'),
                    ('DNS', 'example.net'),
                    ('DNS', 'example.edu'),
                    ('DNS', 'example.com'),
                    ('DNS', 'example.org'),
                    ('DNS', 'www.example.com'),
                    ('DNS', 'www.example.edu'),
                    ('DNS', 'www.example.net')),
 'version': 3}
[{'issuer': ((('countryName', 'US'),),
             (('organizationName', 'DigiCert Inc'),),
             (('organizationalUnitName', 'www.digicert.com'),),
             (('commonName', 'DigiCert Global Root CA'),)),
  'notAfter': 'Nov 10 00:00:00 2031 GMT',
  'notBefore': 'Nov 10 00:00:00 2006 GMT',
  'serialNumber': '083BE056904246B1A1756AC95991C74A',
  'subject': ((('countryName', 'US'),),
              (('organizationName', 'DigiCert Inc'),),
              (('organizationalUnitName', 'www.digicert.com'),),
              (('commonName', 'DigiCert Global Root CA'),)),
  'version': 3}]

```


The client program has received and verified the server's certificate during the TLS handshake. The server's certificate contains information about the server's identity and public key, as well as the signature of a trusted certificate authority (CA) that vouches for the server. The client program prints a dictionary containing the following fields from the server's certificate:

•  OCSP: This is the URL of the Online Certificate Status Protocol (OCSP) responder, which can be used to check whether the certificate has been revoked or not.

•  caIssuers: This is the URL of the CA that issued the certificate. The client can download the CA's certificate from this URL if it does not have it already.

•  crlDistributionPoints: This is a list of URLs where the Certificate Revocation List (CRL) can be obtained. The CRL contains a list of certificates that have been revoked by the CA.

•  issuer: This is a tuple of tuples containing the name of the CA that issued the certificate. Each tuple consists of a type and a value, such as ('countryName', 'US') or ('commonName', 'DigiCert TLS RSA SHA256 2020 CA1').

•  notAfter: This is the expiration date of the certificate, in GMT format. The certificate is valid until this date.

•  notBefore: This is the issuance date of the certificate, in GMT format. The certificate is valid from this date.

•  serialNumber: This is a hexadecimal string representing the serial number of the certificate. The serial number is unique within each CA and can be used to identify the certificate.

•  subject: This is a tuple of tuples containing the name of the server that owns the certificate. Each tuple consists of a type and a value, such as ('countryName', 'US') or ('commonName', 'www.example.org').

•  subjectAltName: This is a list of tuples containing alternative names for the server that owns the certificate. Each tuple consists of a type and a value, such as ('DNS', 'www.example.org') or ('DNS', 'example.net'). The client can use any of these names to connect to the server.

•  version: This is an integer representing the version number of the certificate. The current version is 3.

The client program also prints a list of dictionaries containing information about all the CA certificates loaded in the SSL context object. These are the certificates that the client trusts and uses to verify the server's certificate. Each dictionary contains similar fields as above, such as issuer, subject, notAfter, etc.

##### Explain the purpose of /etc/ssl/certs

The purpose of /etc/ssl/certs is to store the certificates of trusted Certificate Authorities (CAs) that are used to verify the identity of servers and encrypt the communication using TLS. The directory contains PEM files of CA certificates that are installed by default or by the user. The context.load_verify_locations(capath=cadir) line in the code tells the TLS context to load the certificates from this directory and use them to validate the server certificate.

##### Which step triggers the TCP handshake, and which step triggers the TLS handshake. Explain the relationship between the TLS handshake and the TCP handshake

In this code, the TCP handshake is triggered by the sock.connect((hostname, port)) line, which establishes a TCP connection to the server at the specified hostname and port. The TLS handshake is triggered by the ssock.do_handshake() line, which initiates the TLS protocol negotiation with the server using the established TCP connection. The relationship between the TLS handshake and the TCP handshake is that the former relies on the latter to provide a reliable and ordered data transmission channel. The TLS handshake cannot start until the TCP handshake is completed.

Using wireshark to capture the network traffics during the execution we were able to see the exchange of packets on the TCP handshake and TLS Handshake.
The TCP handshake consists of three packets: SYN, SYN-ACK and ACK. The TLS handshake consists of several packets, such as Client Hello, Server Hello, Certificate, Server Key Exchange, Client Key Exchange, Change Cipher Spec and Finished.


### Task 1.b: CA's Certificate

By changing the cadir directory to our custom directory, we encounter an error during the TLS handshake, since we don't have the correct CA certificates in the ./client-certs.
The error is something like "certificate verify failed: unable to get local issuer certificate". This means that the client cannot find the CA certificate that matches the issuer of the server certificate, and therefore cannot verify the server's identity. To fix this error, we need to copy the CA certificate from the /etc/ssl/certs directory and put it in the cadir directory. Also we need to make sure that the CA certificate has a .pem extension and a hash-based symbolic link, as explained in the lab description.

Procedure:

```bash

#Look for the CA certificate that matches the issuer of the server certificate, according to executions of the handshake.py script.
ls /etc/ssl/certs

#Copy the CA certificate to cadir directory
cp /etc/ssl/certs/DigiCert_Global_Root_CA.pem ./client-certs

#Create an hash value from the subject field -> 3513523f
openssl x509 -in DigiCert_Global_Root_CA.pem -noout -subject_hash

#Symbolic link between the file with hash value and CA file
ln -s DigiCert_Global_Root_CA.pem 3513523f.0

#Perform successfuly the handshake again

```

### Task 1.c:  Experiment with the hostname check


The objective of task 1.c is to help understand the importance of hostname checks at the client side(github.com)(moodle.up.pt). The hostname check is a mechanism to verify whether the server's hostname matches the one in its certificate.

##### Explain the importance of hostname check. If the client program does not perform the hostname check, what is the security consequence?

The hostname check is a process of verifying whether the server's hostname matches the one in its certificate. This is necessary to prevent man-in-the-middle attacks, where an attacker can intercept the TLS connection and present a fake certificate that is signed by a trusted CA, but belongs to a different domain name. If the client program does not perform the hostname check, it may accept the fake certificate and establish a secure connection with the attacker, instead of the intended server. The attacker can then decrypt and modify the data sent between the client and the server, without being detected. Therefore, hostname check is an essential part of TLS security.


We are connecting to the server using its IP address, but pretending that it is www.example2020.com. If our client program performs the hostname check correctly, it rejects the connection, because the server's certificate does not match www.example2020.com.

### Task 1.d:  Sending and getting Data

The purpose of task 1.d is to learn how to send and receive data over the secure connection established by TLS.

```python

#The tls client code for sending and receiving data over the secure connection

#!/usr/bin/env python3

import socket
import ssl
import sys
import pprint

hostname = sys.argv[1]
port = 443
#cadir = '/etc/ssl/certs'
cadir = './client-certs'

# Set up the TLS context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  # For Ubuntu 20.04 VM
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)      # For Ubuntu 16.04 VM

context.load_verify_locations(capath=cadir)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True

# Create TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))
input("After making TCP connection. Press any key to continue ...")

# Add the TLS
ssock = context.wrap_socket(sock, server_hostname=hostname,
                            do_handshake_on_connect=False)
ssock.do_handshake()   # Start the handshake
print("=== Cipher used: {}".format(ssock.cipher()))
print("=== Server hostname: {}".format(ssock.server_hostname))
print("=== Server certificate:")
pprint.pprint(ssock.getpeercert())
pprint.pprint(context.get_ca_certs())
input("After TLS handshake. Press any key to continue ...")

# Send HTTP Request to Server
request = b"GET / HTTP/1.0\r\nHost: " + \
hostname.encode('utf-8') + b"\r\n\r\n"
ssock.sendall(request)

# Send HTTP Request to Server to fetch an image
# request = b"GET /logo.png HTTP/1.1\r\nHost: " + \
# hostname.encode('utf-8') + b"\r\nConnection: close\r\n\r\n"
# ssock.sendall(request)

# Read HTTP Response from Server
response = ssock.recv(2048)
while response:
	pprint.pprint(response.split(b"\r\n"))
	response = ssock.recv(2048)

# Close the TLS Connection
ssock.shutdown(socket.SHUT_RDWR)
ssock.close()




```




