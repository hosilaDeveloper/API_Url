from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .pagination import CustomPagination
from .serializers import *
from .models import Post, Experience, Comment, Skills, Service, Works, About, Contact


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classe = [permissions.IsAuthenticatedOrReadOnly]
    filter_backend = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filter_fields = ['category', 'tags']
    ordering_fields = ['created_at']
    search_fields = ['title', 'description']
    serializer_class = PostSerializer
    pagination_clas = CustomPagination


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExperienceView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SkillsView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class WorksView(generics.ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
