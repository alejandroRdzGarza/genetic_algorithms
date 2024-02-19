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
Esta es la heuristica que vamos a seguir para poder aproximar esta escenario tan complejo.

Entonces un individuo debe de elegir en que vale la pena poner su tiempo, debe de pensar a largo plazo, algunos eventos tienen recompensas a corto
plazo, pero otros eventos son mas tardados pero su recompensa es mayor

Cada individuo contara con 35,000 dias de vida, osea que cada generacion dura 35,000 dias

Categorias de eventos            valor        dias de vida requeridos:

Familia                          10           5000
Dia de trabajo                   2            15000
Dia de estudio                   10           1000
Crear una empresa de exito       100          1800
ETC



Fitness Function:
'''

import 

POPULATION_SIZE = 100
INDIVIDUAL_SIZE = 10



def random_init(numero_de_genes):
    
    
    
