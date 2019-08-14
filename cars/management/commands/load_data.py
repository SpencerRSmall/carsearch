from django.core.management.base import BaseCommand, CommandError
from cars.models import Car
import csv

class Command(BaseCommand):
    help = 'loads data from file into database'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        print("hey", options["path"])
        carReader = csv.reader(open(options["path"][0]), delimiter=',')
        count = 0
        for row in carReader:
            if count == 0:
                print(row)
            else:
                Car.objects.create(mpg = row[])
            count = count + 1