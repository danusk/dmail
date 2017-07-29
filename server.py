#############
# server.py #
#############

import socketserver


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
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        processed = self.process_message(str(self.data))
        self.request.sendall(bytes(processed, "utf-8"))

    def process_message(self, data):
        if "lower" in data:
            return data.lower()
        elif "upper" in data:
            return data.upper()
        else:
            return data


def server_main():
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyServer)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print("Running on :", HOST, PORT)
    server.serve_forever()


if __name__ == "__main__":
    server_main()
