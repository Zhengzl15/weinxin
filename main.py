#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import os
from flask import Flask, request, abort, render_template
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.exceptions import InvalidAppIdException
try: 
	import xml.etree.cElementTree as ET 
except ImportError: 
	import xml.etree.ElementTree as ET 

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
		return make_response(echostr)

	else:
		rec = request.stream.read()
		xml_rec = ET.fromstring(rec)
		msgtype = xml_rec.find('MsgType').text
		tou = xml_rec.find('ToUserName').text
		fromu = xml_rec.find('FromUserName').text
		xml_rep_img = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><![CDATA[%s]]></Title><Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl></item></Articles><FuncFlag>1</FuncFlag></xml>"
		xml_rep_mutiimg = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>6</ArticleCount><Articles><item><Title><![CDATA[%s]]></Title><PicUrl><![CDATA[%s]]></PicUrl></item><item><Title><![CDATA[我的冰箱]]></Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[定制早餐]]></Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[定制午餐]]></Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[定制晚餐]]></Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[结伴购物]]></Title><Url><![CDATA[%s]]></Url></item></Articles></xml>"

        #用户一旦关注改公众账号，自动回复以下图文消息
        if msgtype == "event":
        	msgcontent = xml_rec.find('Event').text
        	if msgcontent == "subscribe":
        		msgcontent = tips
        	else:
        		msgcontent = error_msg
        		msg_title = u"美食助手，您的私人定制"
        		msg_imag_url = "http://gourmetmaster.sinaapp.com/static/main_meitu_3.jpg"
        		response = make_response(xml_rep_img % (fromu,tou,str(int(time.time())),msg_title,msgcontent,msg_imag_url))
        		response.content_type='application/xml'
        		return response


if __name__ == '__main__':
	server_ip = '0.0.0.0'
	server_port = 80
	app.run(host=server_ip, port=server_port, debug=True)