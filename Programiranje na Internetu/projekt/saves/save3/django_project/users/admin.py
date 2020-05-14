from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Predmeti, Upisi

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role', 'status', 
                    'is_staff', 'date_joined', 'last_login')

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Upisi)