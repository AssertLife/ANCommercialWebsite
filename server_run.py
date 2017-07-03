"""
https://docs.python.org/2/library/simplehttpserver.html
"""
import SimpleHTTPServer
import socketserver

PORT = 8000


handler = SimpleHTTPServer.SimpleHTTPRequestHandler
sstcps = socketserver.TCPServer(("", PORT), handler)

print "Forever serving at port ", PORT
sstcps.serve_forever()