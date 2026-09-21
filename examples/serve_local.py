'''Serve a G0DM0D3 checkout on a chosen port and open the browser.

Equivalent to running python3 -m http.server 8000 inside the repo, which is
the local setup the project documents, plus a check that index.html exists,
a loopback-only bind, and an automatic browser launch.
'''
import http.server
import os
import socketserver
import sys
import webbrowser

root = os.environ.get('GODMODE_DIR', 'G0DM0D3')
port = int(os.environ.get('GODMODE_PORT', '8000'))

if not os.path.isfile(os.path.join(root, 'index.html')):
    sys.exit(f'no index.html in {root!r}; clone https://github.com/elder-plinius/G0DM0D3 first')

os.chdir(root)
handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(('127.0.0.1', port), handler) as httpd:
    url = f'http://127.0.0.1:{port}/'
    print(f'serving {root} at {url}')
    print('paste your OpenRouter API key in Settings once the page loads;')
    print('it stays in localStorage and never reaches this process')
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('stopped')
