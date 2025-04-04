#Creamos la lista bidimensional
lista = [
    [1,2,3],
    [5,6,7],
    [8,9,10]
    ]

#declaramos la funcion buscar con a¿párametro x ( valor que buscara)
def buscar(l,x):

    for i  in range(len(lista)):  #Iterador i recorre la lista
        for j in range(len(lista[i])) : #Iterador j recorre las columnas
          if lista[i][j]  == x :

              return i,j # retornamos ambos iteradores

    return None  # si no encuentra el numero que estamos buscando en la lista retorna None


def mostrar(l,x) :  # Creamos otra funcion en la cual vamos a mostrar y pasamos parametros
    listas = buscar(l,x) # Asignamos una variable y le igualamos a nuestra funcion llamada buscar
    if listas is None :  # Si nuestra función mostrar es None quiere decir que no se encontro en la lista el numero

        print("No se encontro")

    else:
        print(f"El numero {x} esta en la posicion {listas} ")  # Si no es None mandamos un print con el numero y la posicion en la lista

print("La lista es: ", lista)

print(mostrar (lista,7))# Llamaos a nuestra funcion y pasamos parametros