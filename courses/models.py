from django.db import models

# Create your models here.
class Course(models.Model):
    # Whenever a model is first added or created, time now is automatically set
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='') # Set to non-null, if no input have empty string
    order = models.IntegerField(default=0) # Controls the order of steps, could have them autoincrement instead etc
    course = models.ForeignKey(Course) # Points to record in Course

    # Controls how the model does x, in this case ordering
    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title
