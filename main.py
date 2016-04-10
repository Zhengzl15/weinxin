from flask import Flask
from flask import abort
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'] )
def wechat_auth():
	if request.method == 'GET':
		token = 'zzlfoo'
		query = request.args
		signature = query.get('signature', '')
		timestamp = query.get('timestamp', '')
		nonce = query.get('nonce', '')
		echostr = query.get('echostr', '')
		print(signature)
		try:
			

		try:
			check_signature(token, signature, timestamp, nonce)
		except InvalidSignatureException:
			abort(403)
		return echostr

if __name__ == '__main__':
	server_ip = '0.0.0.0'
	server_port = 80
	app.run(host=server_ip, port=server_port, debug=True)
