from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import urldetails
from .forms import urldetailsForm
from .documents import urldetailsDocument
import pdb
import random
import string
import json


class UrlCreateView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': urldetailsForm()}
        return render(request, 'shortner/operation.html', context)

    def post(self, request, *args, **kwargs):
        username = request.user.username
        
        fullurl = request.POST.get("fullurl")
        urlname = request.POST.get("urlname")
        userdetailsObj, created = urldetails.objects.get_or_create(fullurl=fullurl ,user__username=username)
        userdetailsObj.shorturl = request.META['HTTP_REFERER'].replace("operations/", "") + "shorturl" + str(userdetailsObj.id)
        userdetailsObj.urlname = urlname
        userdetailsObj.user = User.objects.get(username=username)
        userdetailsObj.save()
    
        data = {}
        data["fullurl"] = userdetailsObj.fullurl
        data["urlname"] = userdetailsObj.urlname
        data["shorturl"] = userdetailsObj.shorturl
        
        return JsonResponse(data)
        return HttpResponse(json.dumps(data), content_type='application/json')


class UrlListView(LoginRequiredMixin,ListView):
    template_name = "shortner/urllist.html"
    
    def get_queryset(self):
        search = urldetailsDocument.search()
        new_context = search.filter('match', user__username=self.request.user.username)
        return new_context
    