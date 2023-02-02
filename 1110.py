""""
핵심 로직은 
1. 숫자를 입력받아 일의 자리와 십의 자리로 나눈 후
2. 각 자리의 수들을 더해 모듈로 연산한 값이 새로운 숫자의 일의 자리가 되고
3. 기존 수의 일의 자리 수가 새로운 수의 십의 자리에 들어가야합니다.

위의 로직대로 새로운 숫자를 조합할 때마다 최초의 숫자와 일치하는지 확인하고
일치한다면 반복문을 탈출하고 몇번 조립과정을 거쳤는지 리턴해주고
일치하지 않는다면 조립과정을 진행한 횟수를 담은 count 변수를 1 증가시켜줍니다.
"""


# input 속도 향상을 위해 sys 라이브러리 사용
import sys
input = sys.stdin.readline

# 최초 input을 담을 origin
origin = int(input())
# 새로 조립된 숫자를 담을 변수 n, 초기값은 origin
n = origin
# 숫자 조합을 진행한 횟수, 초기값 1
count = 1

while True:
    #십의 자리를 담을 변수
    ten = n%10
    #일의 자리를 담을 변수
    digit = (ten + n//10)%10
    
    # 새로 조합된 숫자
    tmp = int(f"{ten}{digit}")
    
    
    # 새로 조합된 숫자가 최초 입력값인 origin과 같으면 while문 탈출
    if origin == tmp:
        break
    
    #그렇지 않다면 n에 tmp값을 할당, count 변수 1 증가
    n = tmp
    count += 1
    @
# count 변수 출력
print(count)