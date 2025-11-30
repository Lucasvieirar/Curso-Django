from django.shortcuts import render
from .models import Topic
# Create your views here.
def index(request):
    """Página principal do app_log"""
    return render(request, 'app_logs/index.html')

def topics(request):
    """Mostra os assuntos"""
    topic = Topic.objects.order_by('date_added')

    context = {'topics': topics}

    return render(request, 'app_logs/topics.html', context)