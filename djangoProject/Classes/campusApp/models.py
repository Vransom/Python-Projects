from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    #creates model manager
    object = models.Manager()

    #displays the object output values in the form of a string
    def __str__(self):
        return self.campus_name


    # removes added 's' that Django adds to the model name in the  broswer display
    class Meta:
        verbose_name_plural = "University Campus"
