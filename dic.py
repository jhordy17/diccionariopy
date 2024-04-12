#lista vacia llamada perro
perro = {}
#añadir  nombre, color, raza, patas y edad
perro['name']='scooby'
perro['color']='negro'
perro['raza']='pitbull'
perro['patas']= 4
perro['edad']= 34 
print(perro)
#diccionario estudiantes con nombre, apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección
estudiantes = {}
estudiantes['nombre']='jhordy'
estudiantes['apellido']='blanco'
estudiantes['sexo']= 'hombre'
estudiantes['edad']= 19
estudiantes['estado civil']= 'soltero'
estudiantes['habilidades']= ['java','pyton','c++']
estudiantes['pais']= 'colombia'
estudiantes['cuidad']= 'cartagena'
estudiantes['direccion']= 'pozon'
print(estudiantes)
# tamaño del diccionario
print(estudiantes.__len__())
#Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista
hab=[estudiantes['habilidades']]
print(hab)
print(type(hab))
#Modifique los valores de las habilidades añadiendo una o dos habilidades
hab.append("my sql")
hab.append("html")
print(hab)
#Obtener las claves del diccionario como una lista
valor = estudiantes.keys()
print(valor)
#Obtener los valores del diccionario como una lista
valor = estudiantes.values()
print(valor)
#Cambie el diccionario a una lista de tuplas utilizando el método items()
print(estudiantes.items())
# eliminar
estudiantes.pop('habilidades')
print(estudiantes)
# borrar uno de los diccionarios
del estudiantes
