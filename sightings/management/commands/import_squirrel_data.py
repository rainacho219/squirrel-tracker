from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv, os, datetime

class Command(BaseCommand):
    help = 'Imports csv file from command line'
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        file_path = options['path']
        with open(file_path, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader)
            Sightings.objects.all().delete()
            for row in reader:
                try:
                    date = row[5][4:] + '-' +  row[5][0:2] + '-' + row[5][2:4]
                    p = Sightings(
                        Latitude = float(row[1]),
                        Longitude = float(row[0]),
                        UniqueSquirrelID = row[2],
                        Shift = row[4],
                        Date = date,
                        Age = row[7],
                        PrimaryFurColor = row[8],
                        Location = row[12],
                        SpecificLocation = row[14],
                        Running = str(row[15]).lower(),
                        Chasing = str(row[16]).lower(),
                        Climbing = str(row[17].lower()),
                        Eating = str(row[18]).lower(),
                        Foraging = str(row[19]).lower(),
                        OtherActivities = row[20],
                        Kuks = str(row[21]).lower(),
                        Quaas = str(row[22]).lower(),
                        Moans = str(row[23]).lower(),
                        TailFlags = str(row[24]).lower(),
                        TailTwitches = str(row[25]).lower(),
                        Approaches = str(row[26]).lower(),
                        Indifferent = str(row[27]).lower(),
                        RunsFrom = str(row[28]).lower(),
                    )
                    p.save()
                except:
                    return 'Something is wrong'
