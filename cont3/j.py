import sys


def count_covered(required_sides: list, s: int) -> int:
    """Считает количество пастбищ, вмещающихся в квадрат со стороной s."""
    count = 0
    for req in required_sides:
        if req <= s:
            count += 1
    return count


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    idx = 2
    required_sides = []

    for _ in range(n):
        x1 = int(input_data[idx])
        y1 = int(input_data[idx + 1])
        x2 = int(input_data[idx + 2])
        y2 = int(input_data[idx + 3])
        idx += 4

        # Минимальная сторона квадрата для покрытия текущего пастбища
        required_sides.append(max(x1, y1, x2, y2))

    # Бинарный поиск по длине стороны S
    low = 0
    high = max(required_sides)
    ans = high

    while low <= high:
        mid = (low + high) // 2

        if count_covered(required_sides, mid) >= k:
            ans = mid
            high = mid - 1  # Пробуем уменьшить сторону
        else:
            low = mid + 1  # Стороны не хватает, увеличиваем

    print(ans)


if __name__ == "__main__":
    main()