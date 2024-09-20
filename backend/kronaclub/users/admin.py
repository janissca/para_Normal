from django.contrib import admin
from users.models import ( CustomUser, TypeOfUser, UserType )


admin.site.register(CustomUser)
admin.site.register(TypeOfUser)
admin.site.register(UserType)
