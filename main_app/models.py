from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})

class butterfly(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    wingspan = models.FloatField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('butterflies-detail', kwargs={'butterflies_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])   
    butterfly = models.ForeignKey(butterfly, on_delete=models.CASCADE)
    # new code below
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
# Define the default order of feedings
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})
class Meta:
    ordering = ['-date']  # This line makes the newest feedings appear first

class Photo(models.Model):
    url = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    # this will add a property with the date when created
    created_at = models.DateField(auto_now_add=True) 
    # below will add an update property that will update the date each time the object is updated.
    updated_at = models.DateField(auto_now=True)
    # like the feeding model - we will delete any related images if a Cat is deleted
    cat = models.OneToOneField(butterfly, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat.id} @{self.url}"