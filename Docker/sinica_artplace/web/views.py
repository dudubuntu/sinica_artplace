from django.shortcuts import render
from django.views.generic import View

from contactus.forms import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = ContactUsForm()
        return render(request, 'web/index.html', context={'form': form})