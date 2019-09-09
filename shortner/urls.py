from django.urls import path

from . import views


urlpatterns = [
    path('urllist/', views.UrlListView.as_view(), name='urllist'),

    path('', views.UrlCreateView.as_view(), name='urlcreate'),
]