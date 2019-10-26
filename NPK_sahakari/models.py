from django.db import models

class PersonDetail(models.Model):

    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank = True, null = True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    age = models.IntegerField()
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    grand_father_name = models.CharField(max_length=255)

    class Meta:
        abstract = True
