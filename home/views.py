from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {'iterators': [0,1,2,3,4,5,6,7]})