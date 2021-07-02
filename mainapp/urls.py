from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns=[
    path('', views.index, name='index'),
    # path('sklearn_LinearRegression/', views.sklearnLinearRegression, name='sklearnLinearRegression'),
    path('tensorflow_neuralNetworks/', views.tensorflowNeuralNetworks, name='tensorflowNeuralNetworks'),
]