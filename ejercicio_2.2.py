# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from sunau import Au_read

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))
if texto_1 > texto_2:
    print('{} es mayor que {}'. format(texto_1, texto_2))
else:
    print('{} es menor que {}'. format(texto_1, texto_2))

# Coloque en pantalla los dos nombres e imprima
# Cual de los dos tiene mas cantidad de letras
# Imprima en pantalla según corresponda

letra_1 = 'elisa'
letra_2 = 'rodulfo'
elisa_len = len(letra_1)
rodulfo_len = len(letra_2)
print(letra_2,'tiene mas caracteres que',letra_1)

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

letra_1 = 'elisa'
letra_2 = 'rodulfo'
if (letra_1[0]) > (letra_2[0]):
    print(letra_1[0],'mayor que', letra_2[0])
else: 
    print(letra_2[0],'mayor que', letra_1[0])

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

copia_texto_1 == texto_1
print(copia_texto_1,'es igual que', texto_1)

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

copia_texto_1 =str(input())
texto_2 =str(input())

if copia_texto_1 != texto_2:
    print(copia_texto_1,'es distinto que', texto_2)
else:
    print(copia_texto_1,'es mayor que', texto_2)

print('terminamos!')