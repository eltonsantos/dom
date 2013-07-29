#-*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from launch.models import LaunchUser

class LaunchSignUpView(CreateView):
    model = LaunchUser
    template_name = "dom/launch_signup.html"
    success_url = reverse_lazy('launch:index')

    def form_valid(self, form):
        response = super(LaunchSignUpView, self).form_valid(form)
        messages.success(self.request, 'Cadastro realizado com sucesso. Aguarde novidades!')
        return response
