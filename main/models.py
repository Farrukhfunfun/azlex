from django.db import models


class Education(models.Model):
    uni_name = models.CharField(max_length=60)
    degree = models.CharField(max_length=40)

    def __str__(self):
        return self.uni_name

class Employee(models.Model):
    photo = models.ImageField(upload_to="images")
    surename = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    practice_area = models.TextField()
    edu_info = models.ManyToManyField(Education)
    experience = models.TextField(default="no experience yet")
    languages = models.TextField()
    other = models.TextField()
    email = models.CharField(max_length=70)

    def __str__(self):
        return self.name