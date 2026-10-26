import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

count = 0
current_number = 2


while True:
    if is_prime(current_number):
        count += 1
        if count == n:
            print(current_number)
            break
    current_number += 1