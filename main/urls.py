from django.urls import path
from .views import PostView, ContactView, ExperienceView, CommentView, SkillsView, ServiceView, WorksView, \
    AboutView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('contact/', ContactView.as_view(), name='contact-list'),
    path('experience/', ExperienceView.as_view(), name='experience-list'),
    path('comment/', CommentView.as_view(), name='comment-list'),
    path('skill/', SkillsView.as_view(), name='skill-list'),
    path('service/', ServiceView.as_view(), name='service-list'),
    path('work/', WorksView.as_view(), name='work-list'),
    path('about/', AboutView.as_view(), name='about-list'),
]
