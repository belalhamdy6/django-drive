from django.urls import path
from . import views


app_name = 'zoho'
urlpatterns = [
    path('book/', views.booklist, name='book'),
    path('add_book/', views.add_book, name='add'),
]