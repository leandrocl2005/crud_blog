from django.shortcuts import render
import json

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contato(request):
    return render(request, 'home/contato.html')

def plot(request):
    names = ['A', 'B', 'C']
    prices = [100,300,200]

    context = {
        'names': json.dumps(names),
        'prices': json.dumps(prices),
    }
    return render(request, 'home/plot.html', context)

def dmat(request):
	return render(request, 'dmat/score.html')