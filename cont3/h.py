import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    a = [int(x) for x in input_data[2 : n + 2]]

    left = 0
    current_sum = 0
    min_len = n + 1

    for right in range(n):
        current_sum += a[right]

        # Как только сумма стала >= k, сжимаем окно слева
        while current_sum >= k:
            min_len = min(min_len, right - left + 1)
            current_sum -= a[left]
            left += 1

    print(min_len)


if __name__ == "__main__":
    main()