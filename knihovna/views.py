from django.shortcuts import render
from .models import Kniha, Zanr
from django.views.generic import ListView, DetailView



def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)

class BooksListView(ListView):
    model = Kniha
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    ordering = ['-rok_vydani']

class BooksDetailView(DetailView):
    model = Kniha
    template_name = 'books/books_detail.html'
    context_object_name = 'book'