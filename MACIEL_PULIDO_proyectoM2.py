inicio = "Introduce una palabra que contenga de 4 a 8 letras: "
palabra = input(inicio)

if len(palabra) < 4:
    print("Tu palabra contiene", len(palabra), "letras, ingresa", 4 - len(palabra), "más.")
if len(palabra) > 8:
    print("Tu palabra contiene", len(palabra), "letras, elimina", len(palabra) - 8, "de ellas.")
if len(palabra) > 4 and len(palabra) < 8:
    print("Tu palabra es correcta, gracias por ingresar una palabra con", len(palabra), "letras.")
