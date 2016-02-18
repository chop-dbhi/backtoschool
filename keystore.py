import sqlite3
import socketserver
from http.server import SimpleHTTPRequestHandler

conn = sqlite3.connect('keystore.db')
c = conn.cursor()
try:
    #http://stackoverflow.com/questions/3634984/insert-if-not-exists-else-update
    c.execute('CREATE TABLE keyvalue(key text, value text)')
    c.execute('CREATE UNIQUE INDEX key_idx ON keyvalue(key)')
except sqlite3.OperationalError as e:
    pass

conn.commit()
conn.close()

PORT = 8000

class SimpleAppRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        conn = sqlite3.connect('keystore.db')
        c = conn.cursor()
        k = (self.path.strip('/'),)
        
        c.execute('SELECT value FROM keyvalue WHERE key=?', k )
        
        v = c.fetchone()
        if v:
            self.send_response(200)
            v = v[0]
        else:
            self.send_response(404)
            v = "%s NOT FOUND!" % k[0]
            
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(v, "utf8"))


    def do_POST(self):
        length = int(self.headers['Content-Length'])
        value =  self.rfile.read(length).decode('utf-8')
        conn = sqlite3.connect('keystore.db')
        c = conn.cursor()
        q = "INSERT OR REPLACE INTO keyvalue VALUES (?, ?)"
        key = self.path.strip('/')
        c.execute(q, (key, value))
        conn.commit()
        conn.close()
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("'%s' set." % key, "utf8"))


Handler = SimpleAppRequestHandler 
httpd = socketserver.TCPServer(("", PORT), Handler)
print("Serving at port %d" % PORT)
httpd.serve_forever()
