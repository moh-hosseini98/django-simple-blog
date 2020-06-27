from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)