from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Primer(models.Model):
    fp = models.CharField(max_length=512, null=False, verbose_name="前向引物")
    rp = models.CharField(max_length=512, null=False, verbose_name="反向引物")
    submitter = models.ForeignKey(User, related_name="submitter", null=True, verbose_name="提交人")
