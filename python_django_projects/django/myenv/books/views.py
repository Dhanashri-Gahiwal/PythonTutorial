from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from books.forms import SaveBook

# Create your views here.
def index(request):
    # return HttpResponse("This is index page")
    # return render(request,'index.html')
    books = Book.objects
    return render(request,'index.html',{'books':books})