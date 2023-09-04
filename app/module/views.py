from django.shortcuts import render
from .models import article

# Create your views here.
def show(request) :
    data = article.objects.all().order_by('body')
    return render(request,"article.html", {'data':data})

def detail(request, article_id):
    data = article.objects.get(id=article_id)
    return render(request, 'detail.html', {'x': data})