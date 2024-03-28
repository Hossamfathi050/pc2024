from django.db import models

# Create your models here.



class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post_desc= models.CharField(max_length=450)
    post_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


