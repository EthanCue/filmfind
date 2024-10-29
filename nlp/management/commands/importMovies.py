import pandas as pd
from django.core.management.base import BaseCommand
from ...models import Movie

class Command(BaseCommand):
    help = 'Import movies from Excel'

    def handle(self, *args, **kwargs):
        
        # Elimina todos los registros actuales de la base de datos
        # Movie.objects.all().delete()
        # self.stdout.write(self.style.WARNING('Todos los registros de películas han sido eliminados'))
        
        # Lee el archivo de Excel
        df = pd.read_excel('C:/Users/ethan/OneDrive/Desktop/ESCOM/ESCOM_6/Ingenieria_de_Software/FilmFind/film_dataset/moviesShortClean.xlsx')

        for _, row in df.iterrows():
            Movie.objects.update_or_create(
                title=row['title'],  # Campo clave para identificar la película
                defaults={
                    'overview': row.get('overview', ''),
                    'poster_path': row.get('poster_path', ''),
                    'genres': row.get('genres', ''),
                    'original_language': row.get('original_language', ''),
                    'release_date': row.get('release_date', None),
                    'tagline': row.get('tagline', ''),
                    'keywords': row.get('keywords', '')
                }
            )
        self.stdout.write(self.style.SUCCESS('Datos importados correctamente'))
