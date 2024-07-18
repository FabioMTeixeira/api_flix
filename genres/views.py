from genres.models import Genre
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from genres.serializers import GenreSerializer
from app.permissions import GlobalPermissionClass

# Create your views here.


class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
