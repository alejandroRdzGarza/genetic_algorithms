# Este algoritmo genetico intentara encontrar la combinacion
# de eventos en su "vida" que maximizen su "exito"


'''
Representacion:

Chromosoma contara con entre 5-15 (por definir) genes

Cada gene representa un tipo de evento distinto

La representacion a nivel gene sera con numeros reales 
ya que de esta manera tambien puede tomarse en cuenta
cuantas veces repitio un evento en particular.

Cada vez que el individuo decida hacer cierto evento en un dia, se añade uno al slot de ese evento en el cromosoma

Tambien es importante poner requerimientos minimos, por ejemplo se necesitan 1000 dias de estudio para que valga la pena invertir el tiempo.
Esta es la heuristica que vamos a seguir

Categorias de eventos,          sus valores         y pesos:

Familia                             
Dia de trabajo
Dia de estudio
Crear una empresa de exito



Fitness Function:
'''

POPULATION_SIZE = 100
INDIVIDUAL_SIZE = 10



def random_init():
    
    
