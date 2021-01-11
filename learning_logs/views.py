from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm


def index(request):
	return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
	"""adiciona um novo assunto."""
	if request.method != 'POST':
		# Nenhum dado submetido; cria um formulário em branco 
		form = TopicForm()
	else:
		# Dados do POST submetidos; processa os Dados
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topics')	

	# formulário em branco ou inválido 
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)




	
