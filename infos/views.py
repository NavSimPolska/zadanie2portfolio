from django.http import HttpResponse
from django.template import Context, loader

def main(request):
   t = loader.get_template("infos/main.html")
   c = {"title": "Homepage"}
   return HttpResponse(t.render(c))

def me(request):
   t = loader.get_template("infos/main.html")
   c = {"title": "O mnie"}
   return HttpResponse(t.render(c))

def contact(request):
   t = loader.get_template("infos/main.html")
   c = {"title": "Kontakt ze mną"}
   return HttpResponse(t.render(c))

def dzieki(request):
   t = loader.get_template("infos/main.html")
   c = {"title": "Dziekuje"}
   return HttpResponse(t.render(c))