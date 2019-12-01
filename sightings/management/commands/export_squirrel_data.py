from django.core.management.base import BaseCommand, CommandError
import datetime, csv
from sightings.models import Sightings
from django.apps import apps

class Command(BaseCommand):
    help = 'Exports all squirrel objects to csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        file_path = options['path']
        model = apps.get_model('sightings', 'Sightings')
        fields = [i.name for i in model._meta.fields]

        with open(file_path, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(fields)
            for obj in model.objects.all():
                writer.writerow([getattr(obj, f) for f in fields])
