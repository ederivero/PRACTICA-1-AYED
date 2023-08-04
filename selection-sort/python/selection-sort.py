import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i

        # Buscar el índice del elemento más pequeño en el subarreglo no ordenado
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiar el elemento más pequeño con el primer elemento del subarreglo no ordenado
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

if __name__ == "__main__":
    size = 50000      # Cantidad de números enteros en el arreglo
    min_val = 1       # Valor mínimo del número aleatorio generado
    max_val = 100 # Valor máximo del número aleatorio generado
    arr = generate_random_array(size, min_val, max_val)

    arr_copy = arr.copy()  # Copiamos el arreglo generado para no medir el tiempo de generación

    # print("Arreglo original:", arr)

    # Medición del tiempo de ejecución
    start_time = time.time()
    selection_sort(arr_copy)
    end_time = time.time()

    # print("Arreglo ordenado:", arr_copy)

    # Calculamos el tiempo de ejecución en milisegundos
    elapsed_time = (end_time - start_time) * 1000
    print("Tiempo de ejecución: {:.8f} milisegundos".format(elapsed_time))