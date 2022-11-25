from django.db import models

# Create your models here.
class Banner_video(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        # Description = models.CharField(max_length=100)
        Video = models.FileField(upload_to='video/%y/')
        def __str__(self):
            return self.Title

class FMCG(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        # Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title

class Jewellery(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        # Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title

class FB(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        # Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title


class Contact(models.Model):
            Name=models.CharField(max_length=100)
            Email=models.EmailField()
            Subject = models.CharField(max_length=50)
            Message = models.CharField(max_length=500)
            def __str__(self):
                return self.Name