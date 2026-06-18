def solution(num_str):
    answer = 0
    
    for num_ch in num_str:
        answer += int(num_ch)
    
    return answer