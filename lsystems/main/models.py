from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SystemParameters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rules = models.TextField(default='F->G-F-G, G->F+G+F')
    axiom = models.CharField(default='F', max_length=20)
    iterations = models.IntegerField(default=4)
    segment_length = models.IntegerField(default=3)
    initial_heading = models.IntegerField(default=90)
    angle_increment = models.IntegerField(default=60)
    thickness = models.IntegerField(default=3)
    color = models.TextField(default='#000000')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image by {self.user.username}"
