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