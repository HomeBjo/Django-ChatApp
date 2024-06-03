from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        print("Received data= " +  request.POST ['textmessage'])
    return render(request, 'chat/index.html')  #hier brauch man template pfad nicht angeben weil der da immmer von alleine rein guckt 
