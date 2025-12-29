from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import os

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SONALI MUSIC BOT RUNNING")

def run():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

threading.Thread(target=run, daemon=True).start()
