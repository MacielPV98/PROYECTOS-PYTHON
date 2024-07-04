#Hola! te comparto el proceso de cómo fui armando mi código:

#Primero quise acomodar bien el texto de inicio (te puedes saltar este paso y ponerlo directamente en palabra en lugar de inicio)

inicio = "Introduce una palabra que contenga de 4 a 8 letras: "
palabra = input(inicio)

#Aquí acomodé las fórmulas para que el código pueda contar las letras de la palabra ingresada

if len(palabra) < 4:
    input(print("Tu palabra contiene menos de 4 letras, por favor vuelve a intentarlo."))
if len(palabra) > 8:
    input(print("Tu palabra contiene más de 8  letras, por favor vuelve a intentarlo"))
if len(palabra) != 0:
    print("Tu palabra es correcta.")

#Aquí quise dar un pequeño mensaje de éxito

correcto = len(palabra)

input("Tu palabra contiene " + str(correcto) + " letras. (PRESIONA ENTER)")

#Ahora quise confirmar la palabra ingresada

confirmacion = input("Vuelve a escribir la palabra: ")
if len(confirmacion) < len(palabra):
    print("Error en", len(palabra) - len(confirmacion), "letra(s) de menos")
elif len(confirmacion) > len(palabra):
    print("Error en", len(confirmacion) - len(palabra), "letra(s) de más.")
elif confirmacion == palabra:
    print("Palabra confirmada.")
else:
    print("Error en confirmar la palabra.")

#Al parecer sí funciona jaja. Por su atención, gracias.
