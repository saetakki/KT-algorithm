"""
등수를 담을 rank 배열을 만들고
지워진 숫자들이 몇개인지 담을 candidate 변수에 지워진 숫자들(0)이 몇개인지 할당한다 (candidate)
그 후 당첨번호화 현재 남아있는 번호 간 몇개가 일치하는지 set을 활용해 갯수를 계산하고 (remain)
가장 높게 당첨될 수 있는 갯수는 remain + candidate, 가낭 낮은 등수는 remain만 당첨되었을 때 이기에
rank[remain+candidate] 와 rank[remain]을 배열에 담아 리턴한다.
"""

def solution(lottos, win_nums):
    
    rank = [6,6,5,4,3,2,1]
    candidate = lottos.count(0)
    remain = len(set([i for i in lottos if i != 0]) & set(win_nums))
    
    return [rank[remain+candidate], rank[remain]]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)