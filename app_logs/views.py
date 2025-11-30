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

def topic(request,  topic_id):
    """Mostra um único assunto"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order.by("-date_added")
    context = {'topic': topic, 'entries':entries}
    return render(request, 'app_logs/topic.html', context)