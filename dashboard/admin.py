from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Information)
admin.site.register(Skill)
# admin.site.register(Platform)
# admin.site.register(Social)