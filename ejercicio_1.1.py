# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2:
    print( numero_1, ' es mayor', numero_2 )
else: 
    print( numero_2,' es mayor', numero_1 )

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
numero_1 = int(input())

numero_2 =int(input())

if numero_1 == numero_2:
    print( numero_1, 'es igual', numero_2)
else:
    print( numero_1, not 'igual', numero_2)


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
numero_1 =int(input())

numero_2 =int(input())

if numero_1 > 0 < 100:
    print( numero_1, 'es mayor', 0 , 'menor', 100)
else:
    print(numero_1, 'es menor', 0 , 'mayor', 100)

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

numero_1 =int(input())

numero_2 =int(input())

if numero_1 < 10 or numero_2 > -2:
    print( numero_1, 'es menor', 10, numero_2, 'es mayor', -2)

    print('terminamos')