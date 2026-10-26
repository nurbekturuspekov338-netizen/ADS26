import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        print()
        return

    idx = 0

    n = int(input_data[idx])
    idx += 1
    list1 = [int(x) for x in input_data[idx : idx + n]]
    idx += n

    m = int(input_data[idx])
    idx += 1
    list2 = [int(x) for x in input_data[idx : idx + m]]

    if n == 0 and m == 0:
        print()
        return

    i, j = 0, 0
    merged = []

    while i < n and j < m:
        if list1[i] <= list2[j]:
            merged.append(str(list1[i]))
            i += 1
        else:
            merged.append(str(list2[j]))
            j += 1

    while i < n:
        merged.append(str(list1[i]))
        i += 1
    while j < m:
        merged.append(str(list2[j]))
        j += 1

    sys.stdout.write(" ".join(merged) + "\n")

if __name__ == "__main__":
    main()