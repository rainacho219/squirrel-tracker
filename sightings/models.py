from django.db import models
from django.urls import reverse

class Sightings(models.Model):
    Latitude = models.FloatField(
        help_text=('Latitude of sighting'),
        blank=True,
    )

    Longitude = models.FloatField(
        help_text=('Longitude of sighting'),
        blank=True,
    )

    UniqueSquirrelID = models.CharField(
        max_length=100,
        help_text=('Unique squirrel ID'),
        blank=True,
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        help_text=('Shift of sighting'),
        blank=True,
    )

    Date = models.DateField(
        help_text=('Date of sighting'),
        blank=True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    Age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
        help_text=('Age of squirrel'),
        blank=True,
    )

    BLACK = 'Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'

    PRIMARYFURCOLOR_CHOICES = (
        (BLACK, 'Black'),
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
    )

    PrimaryFurColor = models.CharField(
        max_length=10,
        choices=PRIMARYFURCOLOR_CHOICES,
        help_text=('Primary fur color'),
        blank=True,
    )

    ABOVEGROUND = 'Above Ground'
    GROUNDPLANE = 'Ground Plane'

    LOCATION_CHOICES = (
        (ABOVEGROUND, 'Above Ground'),
        (GROUNDPLANE, 'Ground Plane'),
    )

    Location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        help_text=('Sighting location'),
        blank=True,
    )

    SpecificLocation = models.CharField(
        max_length=100,
        help_text=('Specific location of sighting'),
        blank=True,
    )

    OtherActivities = models.CharField(
        max_length=100,
        help_text=('Other activities'),
        blank=True,
    )
    
    true = 'true'
    false = 'false'

    TF_CHOICES = (
        (true, 'true'),
        (false, 'false'),
    )

    Running = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Running? T/F'),
        blank=True,
    )

    Chasing = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Chasing? T/F'),
        blank=True,
    )

    Climbing = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Climbing? T/F'),
        blank=True,
    )

    Eating = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Eating? T/F'),
        blank=True,
    )

    Foraging = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Foraging? T/F'),
        blank=True,
    )

    Kuks = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Kuks? T/F'),
        blank=True,
    )

    Quaas = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Quaas? T/F'),
        blank=True,
    )

    Moans = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Moans? T/F'),
        blank=True,
    )

    TailFlags = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Tail Flags? T/F'),
        blank=True,
    )

    TailTwitches = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Tail Twitches? T/F'),
        blank=True,
    )

    Approaches = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Approaches? T/F'),
        blank=True,
    )

    Indifferent = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Indifferent? T/F'),
        blank=True,
    )

    RunsFrom = models.CharField(
        max_length=10,
        choices=TF_CHOICES,
        help_text=('Runs From? T/F'),
        blank=True,
    )

    def __str__(self):
        return self.UniqueSquirrelID
    
    def get_absolute_url(self):
        return reverse('index')

# Create your models here.
