import sys


def count_pieces(ropes: list, length: float) -> int:
    count = 0
    for a in ropes:
        count += int(a // length)
    return count


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    ropes = [float(x) for x in input_data[2 : n + 2]]

    low = 0.0
    high = max(ropes)

    # 100 итераций достаточно для достижения точности 10^-9
    for _ in range(100):
        mid = (low + high) / 2.0

        if count_pieces(ropes, mid) >= k:
            low = mid  # Длина подходить, пробуем увеличить
        else:
            high = mid  # Не хватает кусков, уменьшаем длину

    # Выводим ответ с 9 знаками после запятой
    print(f"{low:.9f}")


if __name__ == "__main__":
    main()