from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg,Max,Min
# Create your views here.

def index(request):
    data = Book.objects.all().order_by("-ratings") # - trurns it to desending order
    num_books = data.count()
    avg = data.aggregate(Avg("ratings"),Max("ratings"),Min("ratings"))
    return render(request,"book/index.html",{
        "data":data,
        "total_number_of_books":num_books,
        "average":avg
    })

def book_detail(request,slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404("Book not found")
    return render(request,"book/book_detail.html",{
        "title":book.title ,
        "ratings":book.ratings ,
        "author":book.author ,
        "is_bestseller":book.is_bestselling 
    })