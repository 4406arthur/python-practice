from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080

httpd = HTTPServer(('localhost',port),CGIHTTPRequestHandler)
print ("start====")
httpd.serve_forever()
