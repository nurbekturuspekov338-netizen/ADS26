import sys


def pl(s: str):
    j = 0
    i = 1
    n = len(s)
    p = [0] * n
    while i < n:
        if s[j] == s[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return p


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    p_city = input_data[0].strip()
    p_lower = p_city.lower()
    n = int(input_data[1].strip())

    max_len = 0
    best_cities = []

    for i in range(2, 2 + n):
        city = input_data[i].strip()
        combined = city.lower() + "#" + p_lower
        overlap = pl(combined)[-1]

        if overlap > max_len:
            max_len = overlap
            best_cities = [city]
        elif overlap == max_len and max_len > 0:
            best_cities.append(city)

    print(len(best_cities))
    for city in best_cities:
        print(city)


if __name__ == "__main__":
    solve()