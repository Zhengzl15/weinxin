from flask import Flask
from flask import abort
from flask import redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'] )
def wechat_auth():
	if request.method == 'GET':
		token = 'zzl.foo'
		query = request.args
		signature = query.get('signature', '')
		timestamp = query.get('timestamp', '')
		nonce = query.get('nonce', '')
		echostr = query.get('echostr', '')

if __name__ == '__main__':
	server_ip = '0.0.0.0'
	server_port = 8000
	app.run(host=server_ip, port=server_port, debug=True)