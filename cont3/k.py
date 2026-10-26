import sys


def find_row(matrix, N, M, target):
    """Бинарный поиск строки, в которой может находиться target."""
    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2

        min_val = min(matrix[mid][0], matrix[mid][M - 1])
        max_val = max(matrix[mid][0], matrix[mid][M - 1])

        if min_val <= target <= max_val:
            return mid
        elif target < min_val:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_col(row_data, M, target, is_even):
    """Бинарный поиск столбца внутри конкретной строки."""
    low = 0
    high = M - 1

    while low <= high:
        mid = (low + high) // 2

        if row_data[mid] == target:
            return mid

        if is_even:
            # Четная строка: элементы убывают
            if row_data[mid] > target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            # Нечетная строка: элементы возрастают
            if row_data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    queries = [int(x) for x in input_data[1 : k + 1]]

    idx = k + 1
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input_data[idx : idx + m]]
        matrix.append(row)
        idx += m

    results = []

    for target in queries:
        r = find_row(matrix, n, m, target)

        if r == -1:
            results.append("-1")  # Исправлено: одно число -1
        else:
            c = find_col(matrix[r], m, target, is_even=(r % 2 == 0))
            if c != -1:
                results.append(f"{r} {c}")
            else:
                results.append("-1")  # Исправлено: одно число -1

    print("\n".join(results))


if __name__ == "__main__":
    main()