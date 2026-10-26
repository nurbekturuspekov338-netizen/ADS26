import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])
  if n == 0:
    print(0)
    return

  names = input_data[1 : n + 1]

  
  result = [names[0]]

  
  for i in range(1, n):
    if names[i] != names[i - 1]:
      result.append(names[i])

  
  print(len(result))
  print("\n".join(result))


if __name__ == "__main__":
  solve()
    
            