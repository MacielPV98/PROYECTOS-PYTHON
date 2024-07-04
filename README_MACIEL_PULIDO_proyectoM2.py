#En esta parte coloqué una pequeña variable para poner un mensaje de introducción, este paso se puede saltar, puedes poner directamente el mensaje que quieres que aparezca.

inicio = "Introduce una palabra que contenga de 4 a 8 letras: "
palabra = input(inicio)

#Aquí coloqué fórmulas en el que si la palabra contiene menos de 4 letras, no la va a aceptar y te va a indicar cuántas letras te faltan.

if len(palabra) < 4:
    print("Tu palabra contiene", len(palabra), "letras, ingresa", 4 - len(palabra), "más.")

#Si contiene más de 8 letras, tampoco te la va a aceptar y te va a indicar cuántas debes eliminar.

if len(palabra) > 8:
    print("Tu palabra contiene", len(palabra), "letras, elimina", len(palabra) - 8, "de ellas.")

#Finalmente, si ingresas correctamente lo que pidió, te agradecerá y dirá cuántas letras contiene tu palabra aceptada.

if len(palabra) > 4 and len(palabra) < 8:
    print("Tu palabra es correcta, gracias por ingresar una palabra con", len(palabra), "letras.")

#Espero les sirva éste código, es muy corto pero funciona.
