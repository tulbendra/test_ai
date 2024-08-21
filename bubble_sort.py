
def bubble_sort(arr):

    for i in range(1, len(arr)+1):
        for idx in range(len(arr) - i):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]


if __name__ == "__main__":
    arr = [2, 7, 1, 18, 9, 22, 6, 90, 5, 95, 5]
    bubble_sort(arr)
    print(arr)
