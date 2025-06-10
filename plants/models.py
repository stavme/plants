from django.db import models

class Species(models.Model):
    WATER_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    SOIL_CHOICES = [
        ('sandy', 'Sandy'),
        ('loamy', 'Loamy'),
        ('clay', 'Clay'),
    ]
    FERTILIZER_CHOICES = [
        ('none', 'None'),
        ('organic', 'Organic'),
        ('chemical', 'Chemical'),
    ]
    SUN_CHOICES = [
        ('shade', 'Shade'),
        ('partial', 'Partial Sun'),
        ('full', 'Full Sun'),
    ]

    name = models.CharField(max_length=100)
    water = models.CharField(max_length=10, choices=WATER_CHOICES)
    soil = models.CharField(max_length=10, choices=SOIL_CHOICES)
    fertilizer = models.CharField(max_length=10, choices=FERTILIZER_CHOICES)
    sun = models.CharField(max_length=10, choices=SUN_CHOICES)

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

class Event(models.Model):
    EVENT_CHOICE= [
    ('water', 'Water'),
    ('fertilize', 'Fertilize'),
    ('repot', 'Repot'),
    ('death', 'Plant Died'),
    ]

    plant=models.ForeignKey(Plant,on_delete=models.PROTECT, null=False, blank=False)
    date =models.DateField(verbose_name="תאריך",null=False, blank=False)
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICE)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
