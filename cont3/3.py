import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    # Считываем размеры блоков
    a = [int(x) for x in input_data[2 : n + 2]]

    # Строим массив префиксных сумм (правых границ блоков)
    pref = [0] * n
    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + a[i]

    # Индекс начала запросов
    idx = n + 2
    results = []

    # Обрабатываем m ошибок
    for _ in range(m):
        x = int(input_data[idx])
        idx += 1

        # Бинарный поиск: ищем первый блок, правая граница которого >= x
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            if pref[mid] >= x:
                right = mid
            else:
                left = mid + 1

        # Индекс блока начинается с 1 (left + 1)
        results.append(str(left + 1))

    # Выводим все результаты через перевод строки
    print("\n".join(results))


if __name__ == "__main__":
    main()