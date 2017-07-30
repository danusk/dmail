#############
# server.py #
#############

import argparse
import socketserver
import json
import logging
import sqlite3


class MyServer(socketserver.BaseRequestHandler):
    """
   The request handler class for our server.
   It is instantiated once per connection to the server, and must
   override the handle() method to implement communication to the
   client.
   """

    # FIXME: Don't use class level variable
    DB_CONN = sqlite3.connect('logdata.db')

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        logging.info("{} wrote:".format(self.client_address[0]))
        logging.info(data)

        raw_request = data.decode(encoding='UTF-8')
        # log the raw message
        # turn into json object
        request = json.loads(raw_request)
        self.log_message(request)
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

    # TODO: Actually do DB_CONN.close() before shutting down
    def log_message(self, message):
        name = message['whoami']
        body = message['data']
        self.DB_CONN.cursor().execute(
            'INSERT INTO messages VALUES ("{}", "{}")'.format(name, body)
        )
        return


def server_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help='host to connect to', type=str)
    parser.add_argument("port", help='port to connect to', type=int)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((args.host, args.port), MyServer)
    # create a Connection object that represents the database
    # create table
    MyServer.DB_CONN.cursor().execute(
        'CREATE TABLE IF NOT EXISTS messages (name text, body text)'
    )
    # save the changes
    MyServer.DB_CONN.commit()
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    logging.info("Running on {}:{}".format(args.host, args.port))
    server.serve_forever()


if __name__ == "__main__":
    server_main()
