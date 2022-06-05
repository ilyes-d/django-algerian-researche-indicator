import csv
from apps.home.models import Location
with open('C:/Users/Meoruane/Desktop/wilaya.csv', 'r', encoding="latin1") as wilaya_file:
    reader = csv.reader(wilaya_file)
    next(reader, None)  # to jump a line
    for row in reader:
        a = Location.objects.create(state_name=row[0], state_number=row[1])
        """ 
        This code do an insert SQL statement behind the scenes 
        An alternative code -->
            a = Location.objects.create(state_number=i[0], state_name=i[1])
            a.save() 
        """

a = {'CERIST': {'chef_eta': 'BADACHE Nadjib',
                'nbr_researchers': 5,
                '_citations': 4670},
     'Centre de Développement des Energies Renouvelables': {'chef_eta': 'HADJ-ARAB Amar',
                                                            'nbr_researchers': 8,
                                                            '_citations': 4315},
     'Centre national de Recherche en biotechnologie': {'chef_eta': 'AZIOUNE Ammar',
                                                        'nbr_researchers': 1,
                                                        '_citations': 2993},
     "Centre de Recherche en Technologie des Semi-conducteurs pour l'Energétique (CRTSE)": {'chef_eta': 'BENBOUZA Halima',
                                                                                            'nbr_researchers': 1,
                                                                                            '_citations': 724},
     'Centre de recherche en technologies industrielles -CRTI-': {'chef_eta': 'BADJI Riad',
                                                                  'nbr_researchers': 1,
                                                                  '_citations': 1104},
     'Centre de Recherche Scientifique et Technique en Analyses Physico – Chimique': {'chef_eta': 'BACHARI Khaldoun',
                                                                                      'nbr_researchers': 1,
                                                                                      '_citations': 2164},
     'Centre de Recherche en Anthropologie Sociale et Culturelle CRASC': {'chef_eta': 'MANAA Ammar',
                                                                          'nbr_researchers': 1,
                                                                          '_citations': 2}}

