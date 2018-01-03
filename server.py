import http.server
import socketserver
import os

PORT = os.environ.get('PORT', 80)

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        with open('./index.html', 'rb') as f:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f.read())
            return

    def do_HEAD(self):
        with open('./index.html', 'rb') as f:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f.read())
            return

httpd = socketserver.TCPServer(("", int(PORT)), CustomRequestHandler)
print("Python web server listening on port {}...".format(PORT))
httpd.serve_forever()
