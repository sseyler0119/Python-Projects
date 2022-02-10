from django.db import models


# define class called djangoClasses
class djangoClasses(models.Model):
    # define attributes
    title = models.CharField(max_length=255, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.title # returns course title to admin page
