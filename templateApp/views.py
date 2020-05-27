from django.shortcuts import render
from .forms import templateForm
from .models import templateModel


def templateView(request):
	name='Você pode me alterar na view.'
	return render(request, "templateApp/templateView.html", {'nome':name})
