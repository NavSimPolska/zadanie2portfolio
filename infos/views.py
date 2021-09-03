from django.http import HttpResponse
from django.template import Context, loader

def main(request):
   return HttpResponse("Tu będzie Home")

def me(request):
   return HttpResponse("Tu będzie O mnie")

def contact(request):
   return HttpResponse("Tu będzie Contact")