def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
spisok = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 16 #поиск!
result = binary_search(spisok, 0, len(spisok) - 1, x)
if result != -1:
    print("Элемент найден, шаги:", str(result))
else:
    print("Элемент не найден")