from django.urls import path
from .views import PostView, ContactView, TagView, ExperienceView, CommentView, SkillsView, ServiceView, WorksView, \
    AboutView, CategoryView

urlpatterns = [
    path('post/', PostView.as_view(), name='post-list'),
    path('contact/', ContactView.as_view(), name='contact-list'),
    path('tag/', TagView.as_view(), name='tag-list'),
    path('experience/', ExperienceView.as_view(), name='experience-list'),
    path('comment/', CommentView.as_view(), name='comment-list'),
    path('skill/', SkillsView.as_view(), name='skill-list'),
    path('service/', ServiceView.as_view(), name='service-list'),
    path('work/', WorksView.as_view(), name='work-list'),
    path('about/', AboutView.as_view(), name='about-list'),
    path('category/', CategoryView.as_view(), name='category-list'),
]
