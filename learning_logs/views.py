# from django.shortcuts import render, redirect
# # from django.http import HttpResponseRedirect
# # from django.urls import reverse
# from .models import Topic, Entry
# from .forms import TopicForm, EntryForm


from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
	return render(request, 'learning_logs/index.html')
	
@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
	"""adiciona um novo assunto."""
	if request.method != 'POST':
		# Nenhum dado submetido; cria um formulário em branco 
		form = TopicForm()
	else:
		# Dados do POST submetidos; processa os Dados
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics')

	# formulário em branco ou inválido 
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	"""Acrescenta uma nova entrada para um assunto em particular."""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# Nenhum dado submetido; cria um formulário em branco 
		form = EntryForm()
	else:
		# Dados de POST submetidos; processa os Dados
		form = EntryForm(data=request.POST)
		if form.is_valid:
			new_entry = form.save(commit=False)
			new_entry.topic = topic 
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id)

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)









	
