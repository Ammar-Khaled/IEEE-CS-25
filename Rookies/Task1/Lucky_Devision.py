def is_lucky(number):
    while number > 0:
        digit = number % 10
        if digit != 4 and digit != 7:
            return False
        number //= 10
    return True

def is_divisible_by_lucky_number(n):
    for i in range(1, n + 1):
        if is_lucky(i) and n % i == 0:
            return True
    return False


n = int(input())

if is_lucky(n):
    print("YES")
else:
    if is_divisible_by_lucky_number(n):
        print("YES")
    else:
        print("NO")