from django.core.management.base import BaseCommand, CommandError
from polls.models import Produit as Prod
import openfoodfacts


class Command(BaseCommand):
    args = '<team_id>'
    help = 'Affiche la liste des backlogs'

    def handle(self, *args, **options):
        boissons, viandes, produits_laitiers, pains, plats_prepares  = [], [], [], [], []
        counter = 0

        for product in openfoodfacts.products.get_all_by_category('Boissons'):
            if counter < 3:
                boissons.append(product)
            counter += 1
        
            for boisson in boissons:
                m = Prod(name=boisson['product_name_fr'],
                        countries=boisson['countries'],
                        nutri_score=boisson['nutrition_grades'],
                        marque=boisson['brands']
                        )
                m.save()
        self.stdout.write('Boisson update with success in bdd')
        
        counter = 0 
        for product in openfoodfacts.products.get_all_by_category('Produits laitiers'):
            if counter < 3:
                produits_laitiers.append(product)
            counter += 1

            for produits_laitier in produits_laitiers:
                try:
                    m = Prod(name=produits_laitier['product_name_fr'],
                            countries=produits_laitier['countries'],
                            nutri_score=produits_laitier['nutrition_grades'],
                            marque=produits_laitier['brands']
                            )
                    m.save()
                except:
                    pass
        self.stdout.write('milk product with success in bdd')
        
        
        counter = 0 
        for product in openfoodfacts.products.get_all_by_category('Viandes'):
            if counter < 2:
                viandes.append(product)
            counter += 1

            for viande in viandes:
                try:
                    m = Prod(
                            name=viande['product_name_fr'],
                            countries=viande['countries'],
                            nutri_score=viande['nutrition_grade_fr'],
                            marque=viande['brands']
                            )
                    m.save()
                except:
                    pass
        self.stdout.write('meat product with success in bdd')
    
        counter = 0 
        for product in openfoodfacts.products.get_all_by_category('Pains'):
            if counter < 3:
                pains.append(product)
            counter += 1

            for pain in pains:
                try:
                    m = Prod(name=pain['product_name_fr'],
                            countries=pain['countries'],
                            nutri_score=pain['nutrition_grades'],
                            marque=pain['brands']
                            )
                    m.save()
                except:
                    pass
        self.stdout.write('Pains update with success in bdd')
        
        counter = 0 
        for product in openfoodfacts.products.get_all_by_category('Plats préparés'):
            if counter < 3:
                plats_prepares.append(product)
            counter += 1

            for plats_prepare in plats_prepares:
                try:
                    m = Prod(name=plats_prepare['product_name_fr'],
                            countries=plats_prepare['countries'],
                            nutri_score=plats_prepare['nutrition_grades'],
                            marque=plats_prepare['brands']
                            )
                    m.save()
                except:
                    pass
        self.stdout.write('Meal update with success in bdd')