from django.shortcuts import render

# Create your views here.


def home_view(request):
    context={'i':'nht'}
    return render(request,'about.html',context)