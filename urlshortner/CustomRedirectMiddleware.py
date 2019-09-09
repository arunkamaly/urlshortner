from django.conf import settings
from django.shortcuts import redirect
from shortner.documents import urldetailsDocument
from django.urls import resolve
import pdb


class CustomRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info.replace("/", "")
        print(path)
        print(request.user.username)
        response = self.get_response(request)
        print("AAA")
        search = urldetailsDocument.search()
        search = search.filter('match', shorturl=path)
        for item in search:
            redirect_url = item.fullurl
            return redirect(redirect_url)
    
        return response 