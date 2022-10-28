from django.shortcuts import render
from django.views import View

import socketio
import os
import eventlet
import socket

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbox.settings')
sio = socketio.Server(async_mode='eventlet')



# Create your views here.

@sio.event
def connect(sid):
    print('server conn')
    sio.emit('message', 'welcome')
    print('server conn')
    
class home_view(View):
    def get(self,request):
        context={'i':'nht'}
        return render(request,'about.html',context)
    
    @sio.event
    def connect(sid):
        print('server conn')
        sio.emit('message', 'welcome')
        print('server conn')

    @sio.event
    def me(sid, data):
        sio.emit('me', 'live', to=sid)
        print('hello',data)
