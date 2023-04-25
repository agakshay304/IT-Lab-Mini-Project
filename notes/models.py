from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    file=models.FileField(upload_to='files/', null=True,default=None)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    
    def __repr__(self) -> str:
        return self.file