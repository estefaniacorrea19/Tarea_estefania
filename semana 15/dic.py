# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Estafania",
    "edad": 26,
    "ciudad": "Puyo",
    "profesion": "Software"
}

# Imprimir el diccionario original
print("\nDICCIONARIO ORIGINAL:")
print(informacion_personal)

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número ficticio
    informacion_personal["telefono"] = "0998765432"
    print("Se ha agregado un número de teléfono")
else:
    print("Ya existe la clave de teléfono")

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante después de realizar todas las operaciones
print("\nDICCIONARIO ACTUALIZADO:")
print(informacion_personal)