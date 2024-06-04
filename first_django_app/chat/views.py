from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


from chat.models import Chat
from chat.models import Message

def index(request):
    if request.method == 'POST':
        print("Received data= " +  request.POST ['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST ['textmessage'],chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1) # also hier gehen wir von message auf das objekt chat mit der id 1  was ein array ist    
    return render(request, 'chat/index.html', {'messages': chatMessages})  #hier brauch man template pfad nicht angeben weil der da immmer von alleine rein guckt 

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username= request.POST.get('username'), password=request.POST.get('password')) 
        if user:
            login(request, user)
            return HttpResponseRedirect('/chat')
        else:
            return render(request, 'auth/login.html', {'wrongPassword' : True})
    return render(request, 'auth/login.html')