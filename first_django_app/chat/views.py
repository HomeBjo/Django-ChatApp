from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from chat.models import Chat
from chat.models import Message

@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        print("Received data= " +  request.POST ['textmessage'])
        myChat = Chat.objects.get(id=1)
        message = Message.objects.create(text=request.POST ['textmessage'],chat=myChat, author=request.user, receiver=request.user)
        
        response_data = {
            'created_at': message.created_at.strftime('[%B %d, %Y]'),  # Datum im gewünschten Format
            'author': message.author.username,  # oder ein anderer relevanter Feldname
            'text': message.text,
        }
        return JsonResponse(response_data)
        
    chatMessages = Message.objects.filter(chat__id=1) # also hier gehen wir von message auf das objekt chat mit der id 1  was ein array ist    
    return render(request, 'chat/index.html', {'messages': chatMessages})  #hier brauch man template pfad nicht angeben weil der da immmer von alleine rein guckt 

# def login_view(request):
#     redirect = request.GET.get('next', '/chat/')
#     if request.method == 'POST':
#         user = authenticate(username= request.POST.get('username'), password=request.POST.get('password')) 
#         if user:
#             login(request, user)
#             return HttpResponseRedirect(request.POST.get('redirect')) # ob jetzt so drin steht oder nur ('redirect') ist rigednwie das selbe
#         else:
#             return render(request, 'auth/login.html', {'wrongPassword' : True , 'redirect': redirect})
#     return render(request, 'auth/login.html',{'redirect': redirect})
# hier die funktion drüber ist der ursprung und mit einem http request den wir jetzt in der unteren funktion als json machen damit die seite nicht neu geladen wird

def login_view(request):
    redirect = request.GET.get('next', '/chat/')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password')) 
        if user:
            login(request, user)
            return JsonResponse({'success': True, 'redirect': redirect})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return render(request, 'auth/login.html', {'redirect': redirect})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user = authenticate(username= request.POST.get('username'), password=request.POST.get('password'))
            if user:
             login(request, user)
            return HttpResponseRedirect(request.POST.get('next', '/chat/'))
        else:
            return render(request, 'auth/register.html', {'error': 'Passwords do not match'})
    return render(request, 'auth/register.html')