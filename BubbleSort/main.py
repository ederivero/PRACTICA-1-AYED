import time

def bubble_sort():
    arr = [1,2,3]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# bubble_sort(arr)
start_time = time.time()

bubble_sort()

end_time = time.time()
elapsed_time = end_time - start_time
print("Tiempo de procesamiento:", elapsed_time, "segundos")


