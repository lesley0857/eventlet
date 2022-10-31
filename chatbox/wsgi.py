"""
WSGI config for chatbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import socketio
import os
import eventlet
import socket

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbox.settings')

sio = socketio.Server(async_mode='eventlet',cors_allowed_origins='*')
application = get_wsgi_application()
app = socketio.WSGIApp(sio,application)


#original
#application = get_wsgi_application()


# o=socket.gethostname()
# s = socket.gethostbyname(o)
# print(s)
# ON_HEROKU = os.environ.get('ON_HEROKU')
# if ON_HEROKU:
#     # get the heroku port
#     port = int(os.environ.get("PORT", 17955))  # as per OP comments default is 17995
# else:
#     port = 8000

@sio.event
def connect(sid,environ):
    print('server connect')
    sio.emit('message', 'welcome')
    
@sio.event
def me(sid, data):
    sio.emit('me', 'live', to=sid)
    print('hello',data)

#eventlet.wsgi.server(eventlet.listen(('127.0.0.1',8000)), app)

