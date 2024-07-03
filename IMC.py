#Primero necesito los datos de la persona.

nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuáles son tus apellidos?: ")

datos = nombre + " " + apellido
         
#Después pedimos sus datos de altura y peso.

altura = float(input("Por favot ingresa tu altura en metros: "))

peso = float(input("Ahora ingresa tu peso en Kg: "))

p = peso
a = round(altura*altura)

#Aquí formulamos para sacar el resultado.

IMC = p / a

if IMC >= 0 and IMC <= 15.99 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes delgadez severa.")
elif IMC >= 16.00 and IMC <= 16.99 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes delgadez moderada.")
elif IMC >= 17.00 and IMC <= 18.49 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes delgadez leve.")
elif IMC >= 18.50 and IMC <= 24.99 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes un peso normal.")
elif IMC >= 25.00 and IMC <= 29.99 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes sobrepeso.")
elif IMC >= 30.00 and IMC <= 34.99 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes obesidad leve.")
elif IMC >= 35.00 and IMC <= 39.00 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes obesidad media.")
elif IMC >= 40.00 :
    print(datos + " tu Índice de masa corporal es de: " + str(IMC) + " significa que tienes obesidad morbida.")

#SÍ FUNCIONÓ!!!