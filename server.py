#############
# server.py #
#############

import socketserver
import json
import logging


class MyServer(socketserver.BaseRequestHandler):
    """
   The request handler class for our server.
   It is instantiated once per connection to the server, and must
   override the handle() method to implement communication to the
   client.
   """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        logging.info("{} wrote:".format(self.client_address[0]))
        logging.info(self.data)
        # just send back the same data, but upper-
        raw_request = self.data.decode(encoding='UTF-8')
        # log the raw message
        self.log_message(raw_request)
        # turn into json object
        request = json.loads(raw_request)
        # process the message
        processed = self.process_message(request)
        # send response
        self.request.sendall(bytes(processed, "utf-8"))

    def process_message(self, message):
        param = message['parameter']
        body = message['data']
        if param == 'upper':
            return body.upper()
        elif param == 'lower':
            return body.lower()
        else:
            return body

    def log_message(self, message):
        with open('logfile.txt', 'a') as f:
            f.write(message + '\n')
        return


def server_main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyServer)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    logging.info("Running on {}:{}".format(HOST, PORT))
    server.serve_forever()


if __name__ == "__main__":
    server_main()
