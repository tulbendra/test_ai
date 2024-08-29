
def bubble_sort(arr):
    """This is a code to sort array by bubble sort mechanism"""
    for i in range(1, len(arr)+1):
        y = i
        for idx in range(len(arr) - i):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]


def insertion_sort(arr):
    """This is to sort an array by insertion sort"""
    for idx, item in enumerate(arr):
        position = idx
        y = position
        while position > 0 and item < arr[position - 1]:
            arr[position], arr[position - 1] = arr[position - 1], arr[position]
            position = position - 1
    return arr


if __name__ == "__main__":
    arr = [2, 7, 1, 18, 9, 22, 6, 90, 5, 95, 5]
    bubble_sort(arr)
    print(arr)
