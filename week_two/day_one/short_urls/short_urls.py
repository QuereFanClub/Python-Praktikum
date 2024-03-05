from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


class DynamicRequestHandler(SimpleHTTPRequestHandler):
    # Global variable to store URL mappings
    url_data = {}

    # HTML page for the initial form
    create_page = """
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

    def do_GET(self):
        parsed_path = urlparse(self.path)

        # Wenn die Anfrage aus maximal 6 Zeichen besteht, interpretiere sie als kurze URL
        if len(parsed_path.path) <= 6:
            short_id = parsed_path.path[1:]
            if short_id.isdigit() and int(short_id) in self.url_data:
                long_url = self.url_data[int(short_id)]
                self.send_response(302)
                self.send_header("Location", long_url)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        else:
            # Andernfalls liefere eine 404 Fehlerseite aus
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        from urllib.parse import parse_qs

        # Parse the form data from the request
        content_length = int(self.headers['content-length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = parse_qs(post_data)

        # Process the form data
        if 'long' in form_data:
            long_url = form_data['long'][0]

            # Generate a unique ID for the short URL
            short_id = len(self.url_data)

            # Store the mapping between short ID and long URL
            self.url_data[short_id] = long_url

            # Respond with the confirmation page
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            confirmation_page = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8" />
                <title>Kurze URLs</title>
                <style>
                    body {{ padding: 10vh 10vw; background: #eee; color: #444; font-family: sans; font-size: 12pt; }}
                </style>
            </head>
            <body>
                <h1>Kurze URL erstellt</h1>
                <p>http://localhost:8000/{short_id}</p>
                <p>{long_url}</p>
            </body>
            </html>
            """

            self.wfile.write(confirmation_page.encode("utf-8"))
        else:
            # Handle the case where 'long' key is not present in form data
            self.send_response(400)
            self.end_headers()


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, DynamicRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()
