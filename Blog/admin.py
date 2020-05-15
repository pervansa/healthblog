from django.contrib import admin
from . models import Contact
from . models import Post
from comment.models import UserCommet

# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(UserCommet)