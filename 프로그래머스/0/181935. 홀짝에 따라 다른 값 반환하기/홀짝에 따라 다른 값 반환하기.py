def solution(n):
    sum = 0
    if n % 2 == 0:
        for i in range(n+1):
            if i % 2 == 0:
                sum += (i * i)
            else:
                pass
        return sum
    elif n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                sum += i
        return sum