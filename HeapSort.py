def swap(arr, i, j, assignments):
    arr[i], arr[j] = arr[j], arr[i]
    assignments['count'] += 3
    return assignments


def sink(arr, i, n, comparisons, assignments, trace=True):
    k = i
    if trace:
        print(f"  Починаємо 'занурювати' елемент: {arr[k]} з індексу {k}")

    while True:
        j = 2 * k + 1

        if j >= n:
            if trace:
                print(f"  Елемент {arr[k]} на індексі {k} досяг кінця купи. Завершуємо.")
            break

        if trace:
            print(f"    Обираємо лівий дочірній елемент: {arr[j]} на індексі {j}")

        comparisons['count'] += 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            if trace:
                print(f"    Порівнюємо {arr[j]} (лівий) та {arr[j + 1]} (правий). Обираємо {arr[j + 1]}")
            j += 1

        comparisons['count'] += 1
        if arr[k] >= arr[j]:
            if trace:
                print(f"    {arr[k]} (батько) >= {arr[j]} (найбільший дочірній). Елемент на своєму місці.")
            break
        else:
            if trace:
                print(f"    Міняємо місцями {arr[k]} (батько) та {arr[j]} (дочірній)")
            assignments = swap(arr, k, j, assignments)
            if trace:
                print(f"    Масив після обміну: {arr}")
            k = j
            assignments['count'] += 1

    return comparisons, assignments


def heapsort_trace(arr):
    comparisons = {'count': 0}
    assignments = {'count': 0}

    n = len(arr)
    print(f"Початковий масив: {arr}\n")

    print("--- Фаза 1: Побудова максимальної купи ---")

    start_index = n // 2 - 1
    assignments['count'] += 1

    for i in range(start_index, -1, -1):
        comparisons, assignments = sink(arr, i, n, comparisons, assignments, trace=True)

    print(f"\nМасив після побудови купи: {arr}\n")

    print("--- Фаза 2: Сортування ---")

    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        assignments = swap(arr, 0, i, assignments)

        current_heap_size = i
        assignments['count'] += 1

        print(f"Розмір купи зменшився до {current_heap_size}. Відновлюємо властивості купи.")
        comparisons, assignments = sink(arr, 0, current_heap_size, comparisons, assignments, trace=True)
        print(f"Масив на поточному кроці: {arr}\n")

    return arr, comparisons['count'], assignments['count']

my_list_var6 = [58, 5, 50, 99, 61, 32, 27, 45, 75]
original_list_copy = my_list_var6.copy()
sorted_list, total_comps, total_assigs = heapsort_trace(original_list_copy)
print(f"--- ПІДСУМОК (Heapsort) ---")
print(f"Початковий список: {my_list_var6}")
print(f"Відсортований список: {sorted_list}")
print(f"Загальна кількість порівнянь: {total_comps}")
print(f"Загальна кількість присвоювань: {total_assigs}")