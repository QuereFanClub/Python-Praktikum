# Bearbeitung mit Sandro Schusters, Luca Stoltenberg

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import time


class DynamicRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        current_time = time.ctime()

        if self.path == "/week_two/day_one/time_server/uhrzeit.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
                """
                <!DOCTYPE html>
                <html>
                <head>
                <title>Mein Python Web-Server</title>
                </head>""", "utf-8"))
            self.wfile.write(bytes(
                """
                <body>
                <h1>Request: """ + self.path + """</h1>
                <p>Uhrzeit: """ + current_time + """</p>
				<p>Diese Server-Antwort wurde von einem Python-Programm erzeugt.</p>
				</body>
				</html>
				""", "utf-8"))
        else:
            SimpleHTTPRequestHandler.do_GET(self)


TCPServer.allow_reuse_address = True
with TCPServer(("", 8000), DynamicRequestHandler) as httpd:
    httpd.serve_forever()
