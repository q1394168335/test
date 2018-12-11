from flask import Flask, request 
import socket

app = Flask(__name__)


@app.route('/')
def index():
	h = request.headers
    	h = str(h).replace('\n', '</br>')
    	return f'{h}'


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
