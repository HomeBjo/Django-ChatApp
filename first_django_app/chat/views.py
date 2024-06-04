from django.shortcuts import render

from chat.models import Chat
from chat.models import Message

def index(request):
    if request.method == 'POST':
        print("Received data= " +  request.POST ['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST ['textmessage'],chat=myChat, author=request.user, receiver=request.user)
    return render(request, 'chat/index.html')  #hier brauch man template pfad nicht angeben weil der da immmer von alleine rein guckt 
