from django.db import models

# Create your models here.
class Route(models.Model):
    original_url = models.URLField(help_text= "Write the Original URL Which you want to shorten.")
    key = models.CharField(max_length=10,unique= True, help_text= "Write the customize key or text")

    def __str__(self):
        return f"{self.key}"