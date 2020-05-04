from django.urls import path
from . import views
from .views import SignupView
#from django.conf.urls import url
#from mysite.core import views as core_views

urlpatterns = [
    path('signup/',views.SignupView.as_view() , name='signup'),
    


]
