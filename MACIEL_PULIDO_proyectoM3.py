import random
import matplotlib.pyplot as plt

# Aquí le indicas a la máquina de Galton, la cantidad de canicas, y la cantidad de niveles
def galton(num_steps, num_balls):
    slots = [0] * (num_steps + 1)  # aquí se inicia el conteo
    order = []  # éste le da orden a las canicas

    # aquí se abre el primer ciclo, el de las canicas
    for ball in range(1, num_balls):

        position = 0  # la posición inicial

        # aqí se abre otro ciclo, para los niveles
        for step in range(1, num_steps + 1):
            # hay de dos sopas, izquierda o derecha, la canica decidirá aleatoriamente
            if random.choice(["left", "right"]) == "left":
                position -= 1
            else:
                position += 1

        # ajustamos la posición de las canicas, que no se salga del límite
        if position <= -7:
            position = 6 - abs(position) + 6
        elif position < 0:
            position = (6) - abs(position)
        elif position >= 7:
            position = 6 + position - 6
        else:
            position = 6 + position

        # se muestra las posiciones finales de las canicas
        order.append(position)
        slots[position] += 1
    print(slots)

    # regresamos el orden de las canicas
    return order


# aquí configuramos la biblioteca para que nos arroje la imagen
def histogram():
    intervals = range(min(order), max(order) + 2)  # Se definen los intervalos
    plt.hist(x=order, bins=intervals, color='#F2AB6D')  # Aquí lo personalizamos
    plt.title('Galton Board')  # Aquí va el título
    plt.xlabel('Distribution of balls')  # eje x
    plt.ylabel('Number of balls')  # eje y
    plt.xticks(intervals)  # los intervalos

    plt.show()  # fin

if __name__ == "__main__":
    order = galton(12, 3000)  # corre el simulador y...
    histogram()  # reproduce la gráfica si todo está bien jeje
