## Task 1: TLS Client

### Task 1.a: TLS Handshake

Before a client and a server can communicate securely, several things need to be set up first, including what
encryption algorithm and key will be used, what MAC algorithm will be used, what algorithm should be
used for the key exchange, etc. These cryptographic parameters need to be agreed upon by the client and
the server. That is the primary purpose of the TLS Handshake Protocol. In this task, we focus on the TLS
handshake protocol.

#### Questions  

- What is the cipher used between the client and the server?

We can know the cipher used between the client and the server by looking at the output of the print statement on line 22.
This statement prints the cipher suite that was negotiated during the handshake. A cipher suite is a combination of encryption and authentication algorithms that are used for securing the communication.

In this case the cipher used between the client and the server was ('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)

This means that the cipher suite is TLS_AES_256_GCM_SHA384, which uses AES-256 for encryption, GCM for mode of operation, and SHA-384 for message authentication. It also means that the TLS version is TLSv1.3 and the encryption key size is 256 bits.



- Please print out the server certificate in the program

rust```

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

- Explain the purpose of /etc/ssl/certs

The purpose of /etc/ssl/certs is to store the certificates of trusted Certificate Authorities (CAs) that are used to verify the identity of servers and encrypt the communication using TLS. The directory contains PEM files of CA certificates that are installed by default or by the user. The context.load_verify_locations(capath=cadir) line in the code tells the TLS context to load the certificates from this directory and use them to validate the server certificate.

- Use Wireshark to capture the network traffics during the execution of the program, and explain your
observation. In particular, explain which step triggers the TCP handshake, and which step triggers the
TLS handshake. Explain the relationship between the TLS handshake and the TCP handshake.

In this code, the TCP handshake is triggered by the sock.connect((hostname, port)) line, which establishes a TCP connection to the server at the specified hostname and port. The TLS handshake is triggered by the ssock.do_handshake() line, which initiates the TLS protocol negotiation with the server using the established TCP connection. The relationship between the TLS handshake and the TCP handshake is that the former relies on the latter to provide a reliable and ordered data transmission channel. The TLS handshake cannot start until the TCP handshake is completed.

Using wireshark to capture the network traffics during the execution we were able to see the exchange of packets on the TCP handshake and TLS Handshake.
The TCP handshake consists of three packets: SYN, SYN-ACK and ACK. The TLS handshake consists of several packets, such as Client Hello, Server Hello, Certificate, Server Key Exchange, Client Key Exchange, Change Cipher Spec and Finished.