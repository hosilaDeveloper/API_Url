from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='post/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    file = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to='service/')
    title = models.CharField(max_length=212)
    description = models.TextField()
    price = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='about/')
    full_name = models.CharField(max_length=212)
    description = models.TextField()
    cv_file = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    work_place = models.CharField(max_length=212)
    occupation = models.CharField(max_length=212)
    image = models.ImageField(upload_to='experience/')
    start_finish_year = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.start_finish_year


class Works(models.Model):
    image = models.ImageField(upload_to='work/')
    project_link = models.URLField()
    description = models.TextField()
    price = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price


class Skills(models.Model):
    title = models.CharField(max_length=212)
    percentage = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
