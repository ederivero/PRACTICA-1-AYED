// Counting sort in C++ programming

// Counting sort in C++ programming
#include<iostream>
#include<ctime>
#define MAX 50000
using namespace std;

void countSort(int array[], int size) {
    int output[MAX];
    int count[MAX];
    int max = array[0];

    // Here we find the largest item in the array
    for (int i = 1; i < size; i++) { if (array[i] > max)
            max = array[i];
    }

    // Initialize the count for each element in array to 0
    for (int i = 0; i <= max; ++i) {
        count[i] = 0;
    }

    // For each element we store the count
    for (int i = 0; i < size; i++) {
        count[array[i]]++;
    }

    // Store the cummulative count of each array
    for (int i = 1; i <= max; i++)
	{
		count[i] += count[i - 1];
	}
	
	// Search the index of each element of the actual array in count array, and
	// place the elements in output array
	for (int i = size - 1; i >= 0; i--) 
    {
        output[count[array[i]] - 1] = array[i];
        count[array[i]]--;
    }

    // Transfer the sorted items into actual array
    for (int i = 0; i < size; i++) {
        array[i] = output[i];
    }
}

// Function to print an array
void display(int array[], int size) {
    for (int i = 0; i < size; i++)
        cout << array[i] << " ";
    cout << endl;
}

// Driver code
int main() {
    int x[15] = {100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000};
    int out[15] = {};
    for (size_t i = 0; i < 15; i++)
    {
        int randArray[x[i]];
        // cout << x[i] << endl;
        for(int j=0;j<x[i];j++)
            randArray[j]=(rand()%9) + 1; 
        // display(randArray, x[i]);
        clock_t begin = clock();
        // cout << begin << endl;
        countSort(randArray, x[i]);

        clock_t end = clock();
        double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
        // out[i] = elapsed_secs;
        cout << elapsed_secs << endl;
    }
    
    // int randArray[sz];
    // for(int i=0;i<sz;i++)
    // randArray[i]=rand()%100; 
    // int array[] = {4, 2, 2, 8, 3, 3, 1};
    // int n = sizeof(array) / sizeof(array[0]);
    // countSort(array, n);
    // printArray(array, n);
    // printArray(out, 15);
}