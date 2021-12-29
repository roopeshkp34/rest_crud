from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tags(models.Model):
    tag_title = models.CharField(max_length=30,unique=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'

class Snippest(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    short_text = models.CharField(max_length=30,null=True)
    time_stamp = models.DateTimeField(auto_now=True)


