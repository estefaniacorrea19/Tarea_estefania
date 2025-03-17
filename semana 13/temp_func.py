#Declaramos nuestra lista 3D

temperatura = [
    [  #Arreglo ciudad 1
    [23,15,14,15,18,19,21],
    [15,12,14,25,22,23,26],
    [15,18,19,20,22,26,27],
    [17,19,29,22,22,29,18]
],
    [ #Arreglo ciudad 2
    [25,27,22,23,24,25,26],
    [21,23,24,25,19,18,15 ],
    [24,27,24,23,28,29,25]
    ],
[ #Arreglo ciudad 3
    [24,29,22,27,22,30,25],
    [21,29,24,29,12,18,15 ],
    [33,32,30,25,27,27,27],
    [12,14,17,18,22,25,24]

    ]
]


#Creamos la función y pasamos los parametros que vamos a necesitar

def promedio (temp,ciudad,sem):
    suma =0  #Creamos la variable y la inicializamos en cero
    for i in range(len(temp)): #Recorremos nuestra lista
     if i == sem: #Comprobamos si al recorrer i una iteración es igual a semana
            for j in range(len(temp[i])): # Recorremos los dias dentro de nuestra lista ciudad actual
                 if j == sem : #Comprobamos si al recorrer j una iteración es igual a dia
                    for k in range(len(temp[i][j])):  #La iteración temperatura recorre cada temperatura registrada en el día actual.
                        suma+= temp[i][j][k]   #Sumamos las posiciones que escojemos

                    prom = suma / len(temp[i][j])  #Calculamos el promedio dividinedo la suma total para la longitud de mi lista en la posición i y j
                    return f"La ciudad {ciudad} de la semana {sem} tiene un promedio de {prom} °C"  #Retornamos el promedio con un mensaje


#Llamamos una variable que guardara la función con los parametros que elijamos
prom_final = (promedio(temperatura,0,0))
print(prom_final) #Imprimimos la temperatura final