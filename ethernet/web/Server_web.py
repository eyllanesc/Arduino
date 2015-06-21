#!/usr/bin/python
 
import os
import socket
import sys
import random
import threading
import webbrowser
 
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi
import gevent
 
FILE = 'plot.html'
PORT = 8000
 
def handle(ws):
    if ws.path == '/echo':
        while True:
            m = ws.wait()
            if m is None:
                break
            ws.send(m)
    elif ws.path == '/data':
        i = 0
        while True:
            i+=1
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("192.168.0.177", 23))
	    client_socket.send("h")
            data = client_socket.recv(2048)
            print data
            client_socket.close()
	    ws.send("0 %s %s\n" % (i, data))
            gevent.sleep(0.1)
 
def app(environ, start_response):
    if environ['PATH_INFO'] == '/test':
        start_response("200 OK", [('Content-Type', 'text/plain')])
        return ["Yes this is a test!"]
    elif environ['PATH_INFO'] == "/data":
        handle(environ['wsgi.websocket'])
    else:
        response_body = open(FILE).read()
        status = '200 OK'
        headers = [('Content-type', 'text/html'), ('Content-Length', str(len(response_body)))]
        start_response(status, headers)
        return [response_body]
 
def start_server():
    print 'Serving on http://127.0.0.1:%s' % (PORT)
    server = pywsgi.WSGIServer(('0.0.0.0', PORT), app,
             handler_class=WebSocketHandler)
    server.serve_forever()
 
def start_browser():
    def _open_browser():
        wb = webbrowser.get('/usr/bin/google-chrome %s')
        wb.open_new_tab('http://localhost:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()
 
if __name__ == "__main__":
    print "version:", sys.version
    start_browser()
    start_server()
