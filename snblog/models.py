from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #поле автора, в которое попадает имя юзера, который создает пост, а также способ удаления поста
    title = models.CharField(max_length=150) #поле названия поста с ограничением в 150 символов
    text = models.TextField() #поле текста
    created = models.DateTimeField(default=timezone.now) #поле даты создания поста с указанием времени создания поста по текущему часовому поясу
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    text = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Комментарий {} в теме {}".format(self.username, self.post)



