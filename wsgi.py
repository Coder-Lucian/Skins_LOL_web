# -*- coding: utf-8 -*-
import os
import leancloud

APP_ID = os.environ['LEANCLOUD_APP_ID']
APP_KEY = os.environ['LEANCLOUD_APP_KEY']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)


# if __name__ == '__main__':
#     from gevent.pywsgi import WSGIServer
#     from geventwebsocket.handler import WebSocketHandler
#     from werkzeug.serving import run_with_reloader
#     from werkzeug.debug import DebuggedApplication
#     from leancloud import Engine
#     from app import app
#
#     from gevent import monkey
#
#     monkey.patch_all()
#     application = Engine(app)
#     PORT = int(os.environ['LEANCLOUD_APP_PORT'])
#
#     @run_with_reloader
#     def run():
#         global application
#         app.debug = True
#         application = DebuggedApplication(application, evalex=True)
#         server = WSGIServer(('localhost', PORT), application, handler_class=WebSocketHandler)
#         server.serve_forever()
#     run()
