from math import sqrt
from random import randint

"""
Dado un conjunto de puntos en un plano cartesiano, se te pide encontrar los dos puntos más cercanos entre sí. 
Implementa una función llamada pares_cercanos que tome una lista de coordenadas (puntos en el plano) 
y devuelva las coordenadas de los dos puntos más cercanos junto con su distancia. 
Este ejercicio deberá usar Decoradores, como args y kwargs.
"""

def cords_generator():
    cords = []

    # Genero 5 cordenadas diferentes
    for i in range(5):
        cords.append( (randint(0, 20), randint(0, 20)))


    print("| Plano carteciano generado |")
    print(cords)

    return cords


def calcular_distancias(function):

    """
    Esta funcion me ayudará a calcular cada una de las distancias entre cada punto
    """
    
    def wrapper(*args, **kwargs):   

        cords = args[0] # Obtengo el array de cordenadas
        distances = [] # Preparo el array donde guardaré las distancias
        
        # Recorro las cordenadas
        for i in range(len(cords)):

            cord1 = cords[i]

            # Teniendo como referencia la primera iteración, comienzo a iterar sobre las otras cordenadas
            for j in range(len(cords)):

                # verifico para no calcular el mismo punto en el que me encuentro
                if j != i:

                    cord2 = cords[j]

                    x1 = cord1[0]
                    y1 = cord1[1]

                    x2 = cord2[0]
                    y2 = cord2[1]

                    # Aplico la formula de distacia entre dos puntos
                    d = sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

                    # Agrego la distacia calculada con sus respectivas cordenadas para tener facil acceso
                    distances.append({ 'cord1': cord1, 'cord2': cord2, 'distance': d })

        return function(distances)
    
    return wrapper


@calcular_distancias
def pares_cercanos(distances):

    # Ordeno todos los datos que calculé respecto al campo "distance" de cada diccionario de menor a mayor
    sorted_distances = sorted(distances, key = lambda distance: distance['distance'])

    # Devuelvo el de la posición 0, asumiendo que esa es la distancia más cercana
    return sorted_distances[0]
    


def main():



    cords = cords_generator()
    resultado = pares_cercanos(cords)

    print(f"""
    Los puntos mas cercanos son:
        
        P1{resultado['cord1']} 
        P2{resultado['cord2']}
        Distancia: {resultado['distance']}
    """)


if __name__ == "__main__":
    main()