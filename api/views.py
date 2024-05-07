from rest_framework.generics import ListAPIView
from books.models import Books
from .serializers import *

class BookAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer