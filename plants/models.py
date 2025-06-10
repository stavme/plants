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
