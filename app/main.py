from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {"status": "healthy"}
        else:
            response = {
                "message": "Hello from Sagar to Itvedant, here is my DevOps assignment!",
                "path": self.path
            }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on port 8000")
    server.serve_forever()
