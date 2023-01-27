#콜라츠 추측의공식 / 사용법 : 이 셀을 실행(L-Shift+Enter) 후 solution(숫자, 계산식, 등등 수가 반환되는 모든 값) 을 다른 셀에 적고 실행
def solution(num):
    answer = 0
    
    if num == 1:
        return 0
    
    while True:
        num = num/2 if num % 2 == 0 else (num*3)+1
        answer += 1
        if num == 1:
            return answer 
        elif answer == 500:
            return -1
    
    return answer