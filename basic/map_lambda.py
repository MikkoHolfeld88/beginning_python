from math import sin, cos, tan

def quadrat(a):
    return a*a

numbers =  (1,2,3,4,5,6,7,8,9,10)

map_a = map(quadrat,numbers) # map(funktion,sequenz bzw. daten)

liste_map_a = list(map_a)

print(liste_map_a)

# using lambda

result = list(map(lambda a : a*a ,numbers))
print(result)

# multiple lists for map

num1 = [1,2,3,4]
num2 = [2,4,6,8,10,12,14,16]
num3 = [4,2,4,0]

result = list(map(lambda a,b,c : a + b + c, num1, num2, num3))
print(result)

# multiple functions

def map_functions(x, functions):
     result = []
     for func in functions:
         result.append(func(x))
     return result

family_of_functions = (sin, cos, tan)
final = map_functions(3, family_of_functions)
print(final)
