from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email_chek = models.CharField(max_length=255)
    email_cod = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class info(models.Model):
    user_prof = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pol = models.CharField(max_length=1)
    year = models.CharField(max_length=4)
    image = models.ImageField(default="media/imageses/prof_null.png", null=True, blank=True,upload_to = "imageses/")
    o_sebe = models.CharField(max_length=255)
    ville = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    usernames = models.CharField(default='Нетуc',max_length=30)


class Post(models.Model):
    user_prof = models.ForeignKey(User, on_delete=models.CASCADE)
    name_post = models.CharField(max_length=30)
    text_post = models.CharField(max_length=255)
    date_public = models.CharField(max_length=15)
class Comment(models.Model):

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    name_user =  models.CharField(max_length=255)
    id_user = models.CharField(max_length=255)
    text_comm = models.CharField(max_length=255)
    data_comment = models.CharField(max_length=255)
    def __str__(self):
        self.post_id_id = str(self.post_id_id)
        template = '{0.name_user} {0.text_comm} {0.post_id_id} {0.data_comment} {0.id_user}'
        return template.format(self)
class Chats(models.Model):
    id_create = models.ForeignKey(User, on_delete=models.CASCADE)
    id_friend = models.CharField(max_length=6)
    id_chat = models.CharField(max_length=255)
class Messages(models.Model):
    id_input = models.CharField(max_length=255)
    id_chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    text_message = models.CharField(max_length=255)
    data_message = models.CharField(max_length=15)
class Friend(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    if_friend = models.CharField(max_length=15)
    status = models.CharField(default='No',max_length=30)
    data_application = models.CharField(max_length=15)
    date_acceptance_application = models.CharField(max_length=15)


