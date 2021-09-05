# maths/urls.py
from django.urls import path
from .views import main, me, contact, dzieki

urlpatterns = [
   path('', main),
   path('me/', me),
   path('contact/', contact),
   path('contact/thanks/', dzieki),
]