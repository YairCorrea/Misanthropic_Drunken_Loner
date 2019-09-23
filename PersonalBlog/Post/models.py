from django.db import models
from datetime import datetime
class Post(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('Date published',default=datetime.now)
    paragraph=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='media',null=True,blank=True)
