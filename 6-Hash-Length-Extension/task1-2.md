# Task 1

By using the correct hash and query for the server, a curl got the secret.txt information

```
earth ~/desktop % echo -n "123456:myname=Antonio&uid=1001&lstcmd=1&download=secret.txt" | sha256sum
0a3f6510d8aec68d8de6b55f5c346db7c0737038aa0e75f6d1491c061b7ae72f  -
earth ~/desktop % curl "http://www.seedlab-hashlen.com/?myname=Antonio&uid=1001&lstcmd=1&download=secret.txt&mac=0a3f6510d8aec68d8de6b55f5c346db7c0737038aa0e75f6d1491c061b7ae72f" > secret.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1174  100  1174    0     0   148k      0 --:--:-- --:--:-- --:--:--  191k
```

secret.txt displayed in the browser

![Result](screenshots/result1.png)


# Task 2

It's requested that we build padding for the following message:

```
123456:myname=Antonio&uid=1001&lstcmd=1
```

Length = 39
Padding = 64 - 39 = 25
Length bit = 0x138

```
"123456:myname=Antonio&uid=1001&lstcmd=1"
"\x80"
"\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00"
"\x00\x00\x00\x01\x38"
```
