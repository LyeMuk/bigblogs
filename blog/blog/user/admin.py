from django.contrib import admin

# Register your models here.
from user.models import Userdb,Post

# Register your models here.
admin.site.register((Userdb,Post))
