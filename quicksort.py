
def partition(arr, p, q):

    pivot = arr[p]

    i = p + 1
    j = q

    for _ in range(p, q + 1):

        if i > j:
            break

        if arr[i] <= pivot:
            i += 1

        elif arr[j] > pivot:
            j -= 1

        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    arr[p], arr[j] = arr[j], arr[p]

    return j


def quickSort(arr, p, q):

    if p >= q:
        return

    pivot_index = partition(arr, p, q)

    quickSort(arr, p, pivot_index - 1)
    quickSort(arr, pivot_index + 1, q)


arr = [5, 3, 8, 2, 7, 1, 6]

quickSort(arr, 0, len(arr) - 1)

print(arr)
