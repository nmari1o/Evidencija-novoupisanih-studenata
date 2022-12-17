from django.urls import path
from . import views
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.main, name='main'),
    path('mjesta/', MjestoList.as_view()),
    path('sveucilista/', SveucilisteList.as_view()),
    path('srednja/', SrednjaList.as_view()),
    path('fakultet/', FakultetList.as_view()),
    path('smjer/', SmjerList.as_view()),
    path('maturant/',MaturantList.as_view()),
    path('student/',StudentList.as_view())
]
