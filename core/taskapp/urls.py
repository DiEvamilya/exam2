from django.urls import path

from .views import start_view, category_view


urlpatterns = [
    path('', start_view, name='start'),
    path('category/', category_view, name='category'),

]
