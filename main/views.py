from rest_framework import generics

from .pagination import CustomPagination
from .serializers import *
from .models import Post, Category, Tag, Experience, Comment, Skills, Service, Works, About, Contact


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ExperienceView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SkillsView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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
