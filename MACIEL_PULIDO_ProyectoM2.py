x = int (input ('Ingresa el valor de X: '))
y = int (input ('Ingresa el valor de Y: '))

if x==0 and y==0:
    print ('Tu coordenada no se encuentra en ningún cuadrante. Está localizada en el punto de origen.')
if x==0:
    print ('Ingresa otro valor de X que no sea 0.')
if y==0:
    print ('Ingresa otro valor de Y que no sea 0.')
if x>0 and y>0:
    print ('Tu coordenada se encuentra en el cuadrante I.')
if x<0 and y>0:
    print ('Tu coordenada se encuentra en el cuadrante II.')
if x<0 and y<0:
    print ('Tu coordenada se encuentra en el cuadrante III.')
if x>0 and y<0:
    print ('Tu coordenada se encuentra en el cuadrante IV.')
