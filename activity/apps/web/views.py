# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View

from django.shortcuts import render

# Create your views here.


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
