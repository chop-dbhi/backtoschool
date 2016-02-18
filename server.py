import sqlite3
import socketserver
import urllib.parse
from http.server import SimpleHTTPRequestHandler
PORT = 8000

# You can override this server by filling in any or all of three functions below:

def post(request):
    return False

def put(request):
    return False
    
def get(request):
    return False

# Begin server code

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

class SimpleAppRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if get(self):
            return

        clean_path = self.path.strip('/')
        
        if clean_path.startswith('db/'):
            conn = sqlite3.connect('keystore.db')
            c = conn.cursor()
            params = (clean_path[3:],)
            
            c.execute('SELECT value FROM keyvalue WHERE key=?', params)
            
            v = c.fetchone()
            if v:
                self.send_response(200)
                v = v[0]
            else:
                self.send_response(404)
                v = "%s NOT FOUND!" % params[0]
                
            self.send_header('Content-Type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(v, "utf8"))
        else:
            # This is just a request for a regular file
            super().do_GET()

    def do_POST(self):
        if post(self):
            return
        clean_path = self.path.strip('/')
        
        # To be flexible, we don't care if the post to /db or just /
        if clean_path.startswith('db/'):
            clean_path = clean_path[3:]
            
        length = int(self.headers['Content-Length'])
        
        # See if data was sent by form
        raw_data = self.rfile.read(length).decode('utf8')    
        if self.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            form_data =  urllib.parse.parse_qs(raw_data)
            try:
                key = form_data['key'][0] if 'key' in form_data else form_data['name'][0]
                value = form_data['value'][0]
            except KeyError:
                self.send_response(500)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(bytes("Bad Form Data", "utf8"))
                return
        else:
            key = clean_path
            value = raw_data
            
        conn = sqlite3.connect('keystore.db')
        c = conn.cursor()
        q = "INSERT OR REPLACE INTO keyvalue VALUES (?, ?)"
        
        c.execute(q, (key, value))
        conn.commit()
        conn.close()
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes("'%s' set." % key, "utf8"))
        
    def do_PUT(self):
        if put(self):
            return
        self.do_POST()

    # This is an insecure server    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods','POST, GET, OPTIONS, PUT')
        self.end_headers()

Handler = SimpleAppRequestHandler 
httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
print("Serving at port %d" % PORT)
httpd.serve_forever()
