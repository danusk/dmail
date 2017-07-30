#############
# client.py #
#############


import socket
import json
import logging

def client_main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    HOST, PORT = "localhost", 9999
    data = "hi blah blah blah"

    request = json.dumps(
        {
            'whoami': 'name',
            'parameter': 'upper',
            'data': data,
        }
    )
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send UTF-8 data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(request + "\n", "utf-8"))
        logging.info("Sent:     {}".format(data))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        logging.info("Received: {}".format(received))


if __name__ == "__main__":
    client_main()
