from flask import request,Flask
import json
from SkypeAi import Skype_AI
from gevent import pywsgi
class Ai_web(Skype_AI):
    def __init__(self):
        super(Ai_web, self).__init__()


    def Skype_web(self,port):
        app = Flask(__name__)
        @app.route('/', methods=['get', 'post'])
        def index():
            prompet = request.values.get('prompet')
            if prompet:
                self.send_message(prompet)
                resu = {'code':0,"message":"{}".format(self.get_message())}
                return json.dumps(resu, ensure_ascii=False)
            else:
                resu = {'code': 9999, 'message': '参数不能为空！'}
                return json.dumps(resu,ensure_ascii=False)
        # app.run(host="0.0.0.0", port=port, debug=True,threaded=True)
        server = pywsgi.WSGIServer(('0.0.0.0', port), app)
        print('* SkypeAi WebServer Runing!')
        print('* Running on all addresses {}\n '.format(server.server_host))
        print('* Running on http://127.0.0.1:{}'.format(server.server_port))
        print('* To stop the server, press \'ctrl + c\'')
        server.serve_forever()
