from django.shortcuts import render
from django.contrib.auth import views as auth_views
# Create your views here.
from .models import Book, Author, BookInstance, Genre

from django.shortcuts import render
from .models import Book, Author

def index(request):
    # Número de visitas a esta vista, contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Carga la plantilla index.html con la información adicional en la variable context.
    return render(request, 'index.html', context=context)

    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
    
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    template_name = 'book_list.html' 

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'       
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context