import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    k_roadblocks = data[1]
    a = data[2 : 2 + n]

    # k перегородок делят массив на (k + 1) блоков
    num_blocks = k_roadblocks + 1

    s = sum(a)
    mx = max(a)

    def can_split(limit):
        blocks = 1
        total = 0
        for x in a:
            if total + x > limit:
                blocks += 1
                total = x
                if blocks > num_blocks:
                    return False
            else:
                total += x
        return True

    left = max(mx, (s + num_blocks - 1) // num_blocks)
    right = s

    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1

    print(left)


if __name__ == "__main__":
    main()