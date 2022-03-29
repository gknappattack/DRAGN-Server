from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
from chatbots.Echo import Echo
from datetime import datetime
import socket

chatbots = ["ECHO"]
echo = Echo()

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        #print(self.path)
        #print(parse_qs(self.path[2:]))
        #self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")
    def do_POST(self):
        #self._set_headers
        if self.path == "/":
            self._set_headers()
            root_text = "Currently no implementation at the base level.. \n Please try: /chatbot/<chatbotID or chatbotNAME>"
            data = {"text":root_text}
            data_json = json.dumps(data)
            self.wfile.write(bytes(data_json, "utf-8"))
        elif self.path == "/chatbot" or self.path == "/chatbot/":
            data = {"text":"current list of chatbots", "chatbots":chatbots}
            data_json = json.dumps(data)
            self._set_headers()
            self.wfile.write(bytes(data_json, "utf-8"))
        elif self.path == "/chatbot/echo":
            print("Echo sent a message @: ", str(datetime.now()))
            #data = {"text":"we are at ECHO"}
            
            req_json = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            echo.recv_message(req_json)
            #print(req_json)
            data = echo.send_message()
            data_json = json.dumps(data)
            self._set_headers()
            self.wfile.write(bytes(data_json, "utf-8"))
        


def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = (socket.gethostbyname(socket.gethostname()), port)
    httpd = server_class(server_address, handler_class)
    print('Server running at {}:{}...'.format(socket.gethostbyname(socket.gethostname()), port))
    httpd.serve_forever()

run()