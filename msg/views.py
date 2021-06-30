from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.models import User
from .models import plot,contact_list
from django.utils import timezone

options=1

#options 0 will be of display all content and options 1 will be only of unread content.

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

def sent(request):
    ob=plot.objects.filter(sender=request.user.username)
    return render(request,"sent_all.html",{'obj':ob})

def cont_view(request):

    ob=contact_list.objects.filter(user=request.user.username)
    l=list()
    for each in ob:
        l.append(User.objects.get(username=each.contact))

    if request.method=='POST':
        try:
            obj=contact_list()

            rec=User.objects.get(username=request.POST['nm'])
            user=request.user.username
        
            verify=ob.filter(contact=rec)   #Checks whether already added or not
            if(verify):
                return render (request,"cont.html",{'error':'Username already added','list':l})

            obj.user=user
            obj.contact=rec
            obj.save()

            return render (request,"cont.html",{'list':l})

        except User.DoesNotExist:
            return render (request,"cont.html",{'error':'Username does not exist'},{'list':l})

    else:
        return render (request,"cont.html",{'list':l})