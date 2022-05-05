from django.contrib import admin
from .models import Quiz , questions , category , reponse
# Register your models here.

admin.site.register(Quiz)
admin.site.register(questions)
admin.site.register(category)
admin.site.register(reponse)