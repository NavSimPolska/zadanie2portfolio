# maths/urls.py
from django.urls import path
from .views import main, me, contact

urlpatterns = [
   path('', main),
   path('me/', me),
   path('contact/', contact),
]