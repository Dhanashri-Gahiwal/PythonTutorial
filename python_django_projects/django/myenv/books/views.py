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

def bookdata(request):
    if request.method == 'POST':
        form = SaveBook(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'bookdata.html')