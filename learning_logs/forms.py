from django import forms

from  .models import Topic, Entry


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''} 



# classe que eu digite, NAO FUNCONOU

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Entrada'} # nao tinha func., tinha posto chaves.
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}


