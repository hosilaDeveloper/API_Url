from django.contrib import admin
from .models import Post, Category, Tag, Experience, Comment, Skills, Service, Works, About, Contact
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title', 'category', 'created_at')
    list_filter = ('title',)
    filter_horizontal = ('tags',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_place', 'occupation')
    list_display_links = ('id', 'work_place', 'occupation')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Skills)
admin.site.register(Service)
admin.site.register(Works)
admin.site.register(About)
