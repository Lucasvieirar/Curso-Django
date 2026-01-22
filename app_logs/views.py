from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    """Página principal do app_log"""
    return render(request, 'app_logs/index.html')
@login_required
def topics(request):
    """Mostra os assuntos"""
    topic = Topic.objects.order_by('date_added')

    context = {'topics': topics}

    return render(request, 'app_logs/topics.html', context)
@login_required
def topic(request,  topic_id):
    """Mostra um único assunto"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order.by("-date_added")
    context = {'topic': topic, 'entries':entries}
    return render(request, 'app_logs/topic.html', context)
@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = TopicForm()
    
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'app_logs/.html', context)
@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada par aum assunto e particular"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado submetio; cria um formalario:
        form = EntryForm()
    else:
        # Dados de POST submetidos; porcessa os dados:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        
    context = {'topic':topic, 'form': form}
    return render(request, 'app_logs/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente"""     
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        # Requesição inicial; preenche previamente o formulario com a entrada atual
        form = EntryForm(instance=entry) #formulario preenchdio com o que tem no entry
    else:
        # Dados de Post submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.isvalid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id])) 
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)