from django.contrib import admin

from .models import Message, Chat


# Register your models here.    
class MessageAdmin(admin.ModelAdmin):  #  admin modeladmin in der doc gefunden
    fields = [ 'chat','created_at','author', 'text' , 'receiver'] # die felder in message drin
    list_display = ( 'created_at','author', 'text' , 'receiver') # hier auf ebene messages 
    search_fields = ('text',) #inputfield mich such funktion 
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
