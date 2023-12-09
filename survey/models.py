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
    ('summer', "Summer"),
    ('spring', 'Spring'),
    ('winter', 'Winter'),
    ('fall', 'Fall')
)

area = (
    ('putting', 'Putting'),
    ('approuching', 'Approuching'),
    ('driving', 'Driving'),
    ('chipping', 'Chipping'),
    ('idk', 'IDK'),

)
# Create your models here.
class surverySubmit(models.Model):
    fname = models.CharField(max_length=30, null=False, blank=False)
    strokes= models.IntegerField(null=False, blank=False)
    years = models.CharField(max_length=30, choices=COLOR_CHOICES, default='one')
    seasons = models.CharField(max_length=30, choices=seasons, default='summer')
    areas = models.CharField(max_length=30, choices=area, default='putting')