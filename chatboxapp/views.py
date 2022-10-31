from django.shortcuts import render
from django.views import View

import socketio
import os
import eventlet


from django.core.wsgi import get_wsgi_application


# Create your views here.
    

class home_view(View):
    def get(self,request):
        print('oppppppp')
        context={'i':'nht'}
        return render(request,'about.html',context)
    
    
    
