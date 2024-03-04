from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

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

        if path_param == "create.html":
            # "programmierte" Seite senden
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(htmlpage, 'utf-8'))

        elif path_param.isdigit() and len(path_param) <= 5:
            path_id = int(path_param)
            if path_id in MAPPEDS_URLS:
                long_url = MAPPEDS_URLS[path_id]
                self.send_response(302)
                self.send_header("Location", long_url)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        else:
            # Weiterleitung an die Oberklasse
            SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        global MAPPEDS_URLS, request_id
        from urllib.parse import parse_qs
        # print(int(self.headers['Content-Length']))
        content_length = int(self.headers['content-length'])
        post_data = self.rfile.read(content_length)
        fields = parse_qs(post_data)
        long_url = fields[b'long'][0].decode("utf-8")

        MAPPEDS_URLS[request_id] = long_url
        short_url = f"http://localhost:8000/{request_id}"
        request_id += 1

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
            <p>{0} <a href="{0}">{0}</a></p>
            <p>{1} <a href="{1}">{1}</a></p>
        </body>
        </html>
        """.format(short_url, long_url)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header()
        self.wfile.write(bytes(response_text, 'utf-8'))


TCPServer.allow_reuse_address = True
with TCPServer(("", 8000), DynamicRequestHandler) as httpd:
    print("running")
    httpd.serve_forever()
