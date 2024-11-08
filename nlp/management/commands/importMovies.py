import logging
import pandas as pd
from django.core.management.base import BaseCommand
from ...models import Movie

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Import movies from Excel'

    def handle(self, *args, **kwargs):
        
        # Elimina todos los registros actuales de la base de datos
        # Movie.objects.all().delete()
        # self.stdout.write(self.style.WARNING('Todos los registros de películas han sido eliminados'))
        
        # Lee el archivo de Excel
        df = pd.read_excel('./film_dataset/moviesClean.xlsx')

        for _, row in df.iterrows():
            try:
                title = row['title']
                if len(title) > 255:
                    title = title[:255]
                Movie.objects.update_or_create(
                    defaults={
                        'overview': row.get('overview', ''),
                        'poster_path': row.get('poster_path', ''),
                        'genres': row.get('genres', ''),
                        'original_language': row.get('original_language', ''),
                        'tagline': row.get('tagline', ''),
                        'keywords': row.get('keywords', ''),
                        'normalizedOverview': row.get('normalizedOverview', '')
                    }
                )
            except Exception as e:
                # Si ocurre un error, registra el error y los datos que causaron el problema
                logger.error(f"Error al procesar la película con título '{row['title']}': {e}")
                logger.error(f"Datos que causaron el error: {row}")
                continue
        self.stdout.write(self.style.SUCCESS('Datos importados correctamente'))
