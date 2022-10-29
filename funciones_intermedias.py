x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]



 # Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

x[1][0] = 15

print(x)
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
directorio_deportes['basketball'][1] = 'Bryant'

print(directorio_deportes)

# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)

# Cambia el valor 20 en z a 30.
z[0]['y']=30
print(z)

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes):
    for i in estudiantes:
        print( list(i.keys())[0]+' - '+list(i.values())[0]+', '+list(i.keys())[1]+' - '+list(i.values())[1] )


iterateDictionary(estudiantes)

# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(key_name,some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('last_name',estudiantes)


