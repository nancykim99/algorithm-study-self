'''
PGM138476 : 귤 고르기

[문제 설명]
경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.
경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

[제한 사항]
- 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
- 1 ≤ tangerine의 원소 ≤ 10,000,000

[해결 방법]
리스트의 값을 세서, 정렬 후, k가 0보다 작거나 같을 때까지 빼기

[메모]
1. Counter(리스트) : 리스트의 값들을 세서 딕셔너리로 변경 -> {값 : 값이 개수}
2. dict(sorted(딕셔너리.items(), key=lambda x: x[1], reverse=True)) : 딕셔너리의 value 별로 재정렬
2-1. 딕셔너리.items() : 딕셔너리의 키와 값을 (key, value) 형태의 튜플 쌍으로 묶은 리스트로 반환
2-2. key=lambda x: x[1] : x[1] == value를 기준으로 정렬 기준 지정
2-3. reverse=True : 내림차순으로 정렬
'''
from collections import Counter

def solution(k, tangerine):
    temp = Counter(tangerine)
    temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True))
    cnt = 0
    for v in temp.values():
        k -= v
        cnt += 1
        if k <= 0:
            break
    answer = cnt
    return answer