
from __future__ import absolute_import, unicode_literals
import os
from flask import Flask, request, abort, render_template
from wechatpy.crypto import WeChatCrypto
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.exceptions import InvalidAppIdException

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
		print(signature)

		try:
			check_signature(token, signature, timestamp, nonce)
		except InvalidSignatureException:
			abort(403)
		return echostr

if __name__ == '__main__':
	server_ip = '0.0.0.0'
	server_port = 80
	app.run(host=server_ip, port=server_port, debug=True)