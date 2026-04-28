def solution(n_str):
    index = 0
    while (index < len(n_str) and n_str[index] == "0"):
        index += 1
    
    return n_str[index:]