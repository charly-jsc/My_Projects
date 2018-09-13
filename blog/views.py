from django.shortcuts import render
from django.http import HttpResponse
from .forms import SnippetForm
from django.views.generic import ListView
from .models import Snippet

def snippet_detail(request):


    if request.method == "POST":
        content = request.POST.get('content', '')
        if request.META.get('REMOTE_ADDR'):
            client_ip = request.META.get('REMOTE_ADDR')
        else:
            client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        snippet = Snippet(content=content,client_ip=client_ip)
        snippet.save()

    form = SnippetForm()
    return render(request, 'form.html', {'form': form})

class IndexView(ListView):

    template_name = 'index.html'
    def get_queryset(self):
        return Snippet.objects.all()
