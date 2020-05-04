from django.contrib import admin
from .models import python,student,Login
from firstapp.models import Candidate

admin.site.register(Login)
admin.site.register(python)
admin.site.register(student)

admin.site.register(Candidate)