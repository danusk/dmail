#!/usr/bin/env python3
#############
# client.py #
#############

import argparse
import socket
import logging
from common import into_raw_bytes, DmailRequest


def client_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help='host to connect to', type=str)
    parser.add_argument(
        "-p",
        "--port",
        default=9999,
        help='port to connect to',
        type=int
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    data = "hi blah blah blah"

    request = DmailRequest('name', 'upper', data)

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send UTF-8 data
        sock.connect((args.host, args.port))
        sock.sendall(into_raw_bytes(request))
        logging.info("Sent:     {}".format(data))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        logging.info("Received: {}".format(received))


if __name__ == "__main__":
    client_main()
