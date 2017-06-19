from django.shortcuts import render

# Create your views here.
from snippets.models import Snippet 
from snippets.forms import SnippetForm


def snippets_list(request): 
	snippets = Snippet.objects.all()
	forms = []

	for snippet in snippets: 
		forms.append(SnippetForm(instance=snippet))
	return render(request, 'snippets/snippets_list.html', {
		'snippets_list':snippets,
		'snippets_forms': forms,

		})