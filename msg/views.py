from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.models import User
from .models import plot 
from django.utils import timezone

options=0


def chat(request):
    ob=plot.objects.filter(receiver=request.user.username)
    if request.method=='POST':
        if request.POST['ms']:
            try:
                rec=User.objects.get(username=request.POST['rc'])
                sen=request.user.username
                m=request.POST['ms']
                tmp=timezone.datetime.now()

                obj=plot()
                obj.msg=m
                obj.sender=sen
                obj.receiver=rec
                obj.timestamp=tmp

                obj.save()

                return render(request,'chatscr.html',{'docs':ob,'opt':options})
            except User.DoesNotExist:
                return render(request,"chatscr.html",{'error':'User does not exist'})

        else:
            return render(request,'chatscr.html',{'error':'Cannot send empty field message.'})
    else:       
        return render(request,'chatscr.html',{'docs':ob,'opt':options})


def view(request,chat_id):
    plot.objects.filter(pk=chat_id).update(read=1)
    return redirect('chatscreen')

def change_view(request):
    global options
    if options==1:
        options=0
    else:
        options=1
    return redirect('chatscreen')
