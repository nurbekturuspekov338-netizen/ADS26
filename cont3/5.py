
import sys


def lower_bound(arr: list, target: int) -> int:
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            high = mid
        else:
            low = mid + 1
    return low


def upper_bound(arr: list, target: int) -> int:
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low


def count_in_range(arr: list, L: int, R: int) -> int:
    if L > R:
        return 0
    return upper_bound(arr, R) - lower_bound(arr, L)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    a = [int(x) for x in input_data[2 : n + 2]]
    a.sort()

    idx = n + 2
    results = []

    for _ in range(q):
        l1, r1, l2, r2 = (
            int(input_data[idx]),
            int(input_data[idx + 1]),
            int(input_data[idx + 2]),
            int(input_data[idx + 3]),
        )
        idx += 4

        L1, R1 = min(l1, r1), max(l1, r1)
        L2, R2 = min(l2, r2), max(l2, r2)

        if L1 > L2:
            L1, R1, L2, R2 = L2, R2, L1, R1

        if L2 <= R1:
            merged_R = max(R1, R2)
            ans = count_in_range(a, L1, merged_R)
        else:
            ans = count_in_range(a, L1, R1) + count_in_range(a, L2, R2)

        results.append(str(ans))

    print("\n".join(results))


if __name__ == "__main__":
    main()
