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
sio = socketio.Server(async_mode='eventlet')
application = get_wsgi_application()
app = socketio.WSGIApp(sio,application)


#original
#application = get_wsgi_application()

y=socket.gethostname()
s = socket.gethostbyname(y)
print(s)


eventlet.wsgi.server(eventlet.listen((f'{s}', 8000)), app)