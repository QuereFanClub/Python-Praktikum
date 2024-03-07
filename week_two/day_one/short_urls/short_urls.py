import http.server
import socketserver
from http.server import SimpleHTTPRequestHandler

htmlpage = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Kurze URLs</title>
    <style>
    body { padding: 10vh 10vw; background: #eee; color: #444; font-family: sans; font-size: 12pt; }
    input[type=text] { padding: 5px 10px; font-size: 12pt; width: 80%; height: 30px; background: #eef; }
    input[type=submit] { padding: 10px 20px; font-size: 16pt; }
    </style>
</head>
<body>
    <form action="/create.html" method="POST">
    <h1>Kurze URL Erstellen</h1>
    <input type="text" name="long" placeholder="lange URL"/>
    <input type="submit" value="erstellen"/>
    </form>
</body>
</html>
"""

MAPPEDS_URLS = {}
request_id = 0


class DynamicRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global MAPPEDS_URLS
        path_param = self.path.lstrip('/')
        print(f"Path: {path_param}")

        if path_param == "create.html":
            # "programmierte" Seite senden
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(htmlpage, 'utf-8'))

        elif path_param.isdigit() and len(path_param) <= 5:
            path_id = int(path_param)
            print(f"Path ID: {path_id}")
            if path_id in MAPPEDS_URLS:
                long_url = MAPPEDS_URLS[path_id]
                print(f"Redirecting to {long_url}")
                self.send_response(302)
                self.send_header("Location", long_url)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        else:
            # Weiterleitung an die Oberklasse
            SimpleHTTPRequestHandler.do_GET(self)
            print("SimpleHTTPRequestHandler.do_GET(self)")

    def do_POST(self):
        # Globale Variablen für die Zuordnung von IDs zu URLs und die Anfragen-Zählung
        global MAPPEDS_URLS, request_id

        # Import der Funktion parse_qs zum Parsen von Query-Strings
        from urllib.parse import parse_qs

        # Extrahiere die Länge des POST-Dateninhalts aus den HTTP-Headern
        content_length = int(self.headers['content-length'])
        print(content_length)
        print(self.headers['content-length'])

        # Lese den POST-Datenstrom entsprechend der Länge
        post_data = self.rfile.read(content_length)
        print(f"Post data: {post_data}")

        # Parse die POST-Daten in ein Dictionary von Feldern
        fields = parse_qs(post_data)
        print(f"Fields: {fields}")

        # Extrahiere die lange URL aus den geparsten Feldern und dekodiere sie von Bytes zu UTF-8
        long_url = fields[b'long'][0].decode("utf-8")
        print(f"Long url: {post_data}")

        # Speichere die Zuordnung der neuen langen URL zu einer eindeutigen ID im globalen Dictionary
        MAPPEDS_URLS[request_id] = long_url
        print(MAPPEDS_URLS)

        # Erstelle die kurze URL durch Hinzufügen der eindeutigen ID zur Basis-URL
        short_url = f"http://localhost:8000/{request_id}"

        # Erstelle den HTML-Code für die Antwortseite, ersetze Platzhalter mit den Werten
        response_text = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <title>Kurze URLs</title>
            <style>
            body {{ padding: 10vh 10vw; background: #eee; color: #444; font-family: sans; font-size: 12pt; }}
            input[type=text], input[type=submit] {{ padding: 5px 10px; font-size: 12pt; }}
            </style>
        </head>
        <body>
            <h1>Kurze URL erstellt</h1>
            <p>{0}</p>
            <p>{1}</p>
        </body>
        </html>
        """.format(short_url, long_url)

        # Sende eine HTTP-Antwort mit dem Statuscode 200 (OK)
        self.send_response(200)

        # Setze den HTTP-Header für den Inhaltstyp auf HTML
        self.send_header("Content-type", "text/html")

        # Beende die Header-Sektion der HTTP-Antwort
        self.end_headers()

        # Sende den erstellten HTML-Code als Bytes über den Datenstrom zum Client
        self.wfile.write(bytes(response_text, 'utf-8'))


if __name__ == "__main__":
    PORT = 8000
    Handler = DynamicRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server started at localhost:{PORT}")
        httpd.serve_forever()
