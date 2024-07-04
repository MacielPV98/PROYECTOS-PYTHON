#Primero que nada te pedirá que ingreses un valor designado a cada variable, X y Y:

x = int (input ('Ingresa el valor de X: '))
y = int (input ('Ingresa el valor de Y: '))

#Si ambas coordenadas tienen el valor de 0, verificará que no se encuentra en ningún cuadrante y te pedirá que les des otro valor.

if x==0 and y==0:
    print ('Tu coordenada no se encuentra en ningún cuadrante. Está localizada en el punto de origen.')

#No te va a permitir que ninguna variable tenga el valor de 0, así sea solo una...

if x==0:
    print ('Ingresa otro valor de X que no sea 0.')

#u otra.

if y==0:
    print ('Ingresa otro valor de Y que no sea 0.')

#Finalmente las fórmulas para la designación de los cuadrantes.

if x>0 and y>0:
    print ('Tu coordenada se encuentra en el cuadrante I.')
if x<0 and y>0:
    print ('Tu coordenada se encuentra en el cuadrante II.')
if x<0 and y<0:
    print ('Tu coordenada se encuentra en el cuadrante III.')
if x>0 and y<0:
    print ('Tu coordenada se encuentra en el cuadrante IV.')

#Y fin :)
