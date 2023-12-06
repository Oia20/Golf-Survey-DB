from django.db import models

COLOR_CHOICES = (
    ('less than one.','less than one.'),
    ('one', 'one'),
    ('three','three'),
    ('four','four'),
    ('five','five'),
    ('six or more.', 'six or more.')
)

seasons = (
    ('summer', 'SUMMER'),
    ('spring', 'SPRING'),
    ('winter', 'WINTER'),
    ('fall', 'FALL')

)
# Create your models here.
class surverySubmit(models.Model):
    fname = models.CharField(max_length=30, null=False, blank=False)
    strokes= models.IntegerField(null=False, blank=False)
    years = models.CharField(max_length=30, choices=COLOR_CHOICES, default='one')
    season = models.CharField(max_length=30, choices=seasons, default='summer')
    areas = models.BooleanField()