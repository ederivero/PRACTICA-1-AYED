#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

void selectionSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        // Buscar el índice del elemento más pequeño en el subarreglo no ordenado
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        // Intercambiar el elemento más pequeño con el primer elemento del subarreglo no ordenado
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
}

vector<int> generateRandomArray(int size, int min, int max) {
    vector<int> arr(size);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(min, max);

    for (int i = 0; i < size; i++) {
        arr[i] = dis(gen);
    }

    return arr;
}

int main() {
    int size = 50000;   // Cantidad de números enteros en el arreglo
    int min = 1;        // Valor mínimo del número aleatorio generado
    int max = 100;   // Valor máximo del número aleatorio generado
    vector<int> arr = generateRandomArray(size, min, max);

    // Copiamos el arreglo generado para no medir el tiempo de generación
    vector<int> arrCopy = arr;

    // cout << "Arreglo original: ";
    // for (int num : arr) {
    //     cout << num << " ";
    // }
    // cout << endl;

    // Medición del tiempo de ejecución
    auto startTime = high_resolution_clock::now();
    selectionSort(arrCopy);
    auto endTime = high_resolution_clock::now();

    // cout << "Arreglo ordenado: ";
    // for (int num : arrCopy) {
    //     cout << num << " ";
    // }
    // cout << endl;

    // // Calculamos el tiempo de ejecución en milisegundos con 8 decimales
    // double elapsedTime = duration<double, milli>(endTime - startTime).count();
    // cout << "Tiempo de ejecución: " << fixed << elapsedTime << " milisegundos" << endl;

    // return 0;

    // Calculamos el tiempo de ejecución en milisegundos sin decimales
    int elapsedTime = duration_cast<milliseconds>(endTime - startTime).count();
    cout << "Tiempo de ejecución: " << elapsedTime << " milisegundos" << endl;

    return 0;
}