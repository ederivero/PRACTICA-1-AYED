#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    auto inicio = high_resolution_clock::now();
    int arr[] = { 1,2 };
    int n = sizeof(arr) / sizeof(arr[0]);


    bubbleSort(arr, n);

    auto fin = high_resolution_clock::now();
    auto tiempoEjecucion = duration_cast<milliseconds>(fin - inicio).count();

    cout << "Tiempo de ejecución: " << tiempoEjecucion << " milisegundos" << endl;


    return 0;
}