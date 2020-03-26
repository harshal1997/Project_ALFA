from django.shortcuts import render
#import form
from django.contrib.auth.forms import UserCreationForm
# import for rendering in URL
from django.urls import reverse_lazy
# import module generic views
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
