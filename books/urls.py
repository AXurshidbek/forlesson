from django.urls import path, include
from .views import *

urlpatterns=[
    path('',BookListView.as_view(), name='home')
]