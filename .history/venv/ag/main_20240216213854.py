# Este algoritmo genetico intentara encontrar la combinacion
# de eventos en su "vida" que maximizen su "exito"


'''
Representacion:

Chromosoma contara con entre 5-15 (por definir) genes

Cada gene representa un tipo de evento distinto

La representacion a nivel gene sera con numeros reales 
ya que de esta manera tambien puede tomarse en cuenta
cuantas veces repitio un evento en particular.

Categorias de eventos, sus valores y pesos:

Familia
Dia de trabajo
Dia de estudio
Crear una empresa de exito


Fitness Function:
'''

POPULATION_SIZE = 100
INDIVIDUAL_SIZE = 10



def random_init():
    
    
