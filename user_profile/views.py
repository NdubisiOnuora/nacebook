# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.list import ListView

from user_profile.models import Person


class PersonCreateView(CreateView, FormView):
    model = Person
    success_url = reverse('user_profile:index')


class PersonListView(ListView):
    model = Person
    template_name = 'user_profile/people.html'


class PersonUpdateView(UpdateView, FormView):
    model = Person
    template_name = 'user_profile/people.html'
    success_url = reverse('user_profile:user-profile-update')
