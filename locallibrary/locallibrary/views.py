# locallibrary/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the locallibrary index.")
from django.contrib.auth import views as auth_views

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import redirect

def logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    # Lógica de cierre de sesión, por ejemplo:
    # logout(request)
    return redirect('home')
