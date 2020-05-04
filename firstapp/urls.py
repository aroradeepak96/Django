from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'loginapi',views.LoginViewset)
router.register(r'pythonapi',views.pythonViewset)
router.register(r'studentapi',views.studentViewset)

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:domain_id>/',views.training_domain,name="domain"),
    #path('<int:domain_id>/candidate/', views.candidate,name="candidate"),
    path('json/',views.random,name='json'),
    path('api/',views.LoginList.as_view(),name='api'),
    path('apis/',include(router.urls)),
]

