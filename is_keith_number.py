def is_keith_number(n):
    if n < 10:
        return False
    add = 0
    count = 1
    ls = list(str(n))
    for l in range(len(ls)):
        ls[l] = int(ls[l])
    while add < n:
        for s in ls:
            add += s
        if add == n:
            return count
        elif add > n:
            return False
        else:
            del ls[0]
            ls.append(add)
            add = 0
            count += 1


##chatgpt优化
from collections import deque


def is_keith_number_optimized(n):
    if n < 10:
        return False
    c = 1
    digits = deque([int(digit) for digit in str(n)])
    current_sum = sum(digits)
    while current_sum < n:
        digits.popleft()  # Remove the first element
        digits.append(current_sum)  # Add the sum to the end
        current_sum = sum(digits)  # Recalculate the sum
        c += 1
    return c


