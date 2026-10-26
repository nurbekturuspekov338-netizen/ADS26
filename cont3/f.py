import sys


def total_hours(a: list, k: int) -> int:
    """Вычисляет суммарное количество часов, необходимое для кражи всех слитков при скорости k."""
    hours = 0
    for bars in a:
        # Эквивалентно ceil(bars / k)
        hours += (bars + k - 1) // k
    return hours


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    h = int(input_data[1])

    a = [int(x) for x in input_data[2 : n + 2]]

    # Диапазон поиска для скорости k
    low = 1
    high = max(a)
    ans = high

    # Бинарный поиск по ответу (по скорости k)
    while low <= high:
        mid = (low + high) // 2

        # Проверяем, успеет ли Робин забрать все слитки за h часов при скорости mid
        if total_hours(a, mid) <= h:
            ans = mid  # Запоминаем текущую подходящую скорость
            high = mid - 1  # Пробуем найти еще меньшую скорость
        else:
            low = mid + 1  # Скорость слишком мала, увеличиваем low

    print(ans)


if __name__ == "__main__":
    main()