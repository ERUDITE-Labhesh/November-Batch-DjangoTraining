from django.contrib import admin
from .models import LoginSystem
# Register your models here.


# Register your models here in to normal format 
# admin.site.register(LoginSystem)



class LoginSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'country', 'Immigration_Status')


admin.site.register(LoginSystem, LoginSystemAdmin)