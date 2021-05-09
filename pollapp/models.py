from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30,blank=True)
    option_two = models.CharField(max_length=30,blank=True)
    option_three = models.CharField(max_length=30,blank=True)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question