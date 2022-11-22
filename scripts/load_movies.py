import csv

from OppositeSuggestor.models import Movies
import os
def run():
    print(os.path.join(os.path.dirname(os.path.realpath(__file__)),'movies_output.csv'))
   
    
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'movies_output.csv'),encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        Movies.objects.all().delete()
        counter = 0
        for row in reader:
            counter = counter +1
            film = Movies(movie_title=row[2])

            film.save()
            if counter % 1000==0:
                print(row)  