from http.server import HTTPServer, BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    def get(self, request):
        pass


addr = "127.0.0.1"
port = 8090
server_address = (addr, port)
httpd = HTTPServer(server_address, MyServer)

print(f"Starting httpd server on {addr}:{port}")
httpd.serve_forever()