from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

trials = 0
target = 0


class DynamicRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global target, trials

        from random import randrange

        if self.path == "/start":
            target = randrange(1, 101)
            trials = 0
            response_text = """
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8" />
                    <title>Zahlen raten</title>
                    <style>
                    body { padding: 10vh 10vw; background: #def; text-align: center; font-size: 400%; }
                    input { font-size: 100%; padding: 10px 20px; width: 30%; }
                    </style>
                </head>
                <body>
                    <h1>Willkommen</h1>
                    <p>beim Zahlen-Raten!</p>
                    <p><a href="/guess">zum Spiel</a></p>
                </body>
            </html>
            """
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(response_text, 'utf-8'))
        elif self.path == "/guess":
            response_text = """
            <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8" />
                    <title>Zahlen raten</title>
                    <style>
                    body {{ padding: 10vh 10vw; background: #def; text-align: center; font-size: 400%; }}
                    input {{ font-size: 100%; padding: 10px 20px; width: 30%; }}
                    </style>
                </head>
                    <body>
                        <p>Bisherige Versuche: {0}</p>
                        <p><form method="POST" action="/result">
                        <input type="number" name="guess" min="1" max="100" step="1"/>
                        <input type="submit" value="Raten"/>
                        </form></p>
                    </body>
                </html>
                """.format(trials)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(response_text, 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        global trials, target

        if self.path == "/result":

            from urllib.parse import parse_qs
            fields = {}
            for key, value in parse_qs(self.rfile.read(int(self.headers['content-length']))).items():
                fields[key.decode("utf-8")] = value[0].decode("utf-8")

            trials += 1
            guess_num = int(fields['guess'])
            if guess_num != target:
                relation = "kleiner" if guess_num > target else "größer"
                response_text = """
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8" />
                    <title>Zahlen raten</title>
                    <style>
                    body {{ padding: 10vh 10vw; background: #def; text-align: center; font-size: 400%; }}
                    input {{ font-size: 100%; padding: 10px 20px; width: 30%; }}
                    </style>
                </head>
                    <body>
                        <h1>Falsch!</h1>
                        <p>Die richtige Zahl ist {0} als {1}.</p>
                        <p><a href="/guess">weiter raten</a></p>
                    </body>
                </html>
                    """.format(relation, guess_num)
            else:

                response_text = """
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8" />
                    <title>Zahlen raten</title>
                    <style>
                    body {{ padding: 10vh 10vw; background: #def; text-align: center; font-size: 400%; }}
                    input {{ font-size: 100%; padding: 10px 20px; width: 30%; }}
                    </style>
                </head>
                    <body>
                        <h1>Richtig!</h1>
                        <p>Du hast das Rätsel nach {0} Versuchen gelöst!</p>
                        <p><a href="/start">noch einmal spielen</a></p>
                    </body>
                </html>
                    """.format(trials)

            print(response_text)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(response_text, 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


TCPServer.allow_reuse_address = True
with TCPServer(("", 8000), DynamicRequestHandler) as httpd:
    print("running")
    httpd.serve_forever()