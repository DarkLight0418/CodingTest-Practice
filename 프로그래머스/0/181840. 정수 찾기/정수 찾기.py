def solution(num_list, n):
    for _ in num_list:
        if n in num_list:
            return 1
        else:
            return 0