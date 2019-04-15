from django.db import models

class plot(models.Model):
    msg=models.CharField(max_length=250)
    sender=models.CharField(max_length=20)
    receiver=models.CharField(max_length=20)
    timestamp=models.DateTimeField()
    read=models.IntegerField(default=0)
    '''group=models.CharField(max_length=20)'''