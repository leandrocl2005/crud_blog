from django.urls import path
from .views import home, contato, plot, dmat

urlpatterns = [
    path('contato', contato, name='contato'),
    path('', home, name='home'),
    path('plot', plot, name='plot'),
    path('dmat', dmat, name='dmat'),
]