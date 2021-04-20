from django.conf.urls import include, url
from django.urls import path

from .views import HomePageView, points_dataset, lines_dataset, main_view, client_detail, client_detail,bspd_circle, PointAutocomplete

urlpatterns = [

    url("points/", points_dataset, name='points'),
    url('point-autocomplete/$', PointAutocomplete.as_view(), name='point-autocomplete'),
    path('clients/<int:client_id>', client_detail, name='client_detail'),

    url("circle/", bspd_circle, name='circle'),
    url("lines/", lines_dataset, name='lines'),

    url("", main_view, name='home'),


]