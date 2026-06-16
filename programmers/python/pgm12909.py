'''
PGM12909 : 올바른 괄호

[문제 설명]
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
- "()()" 또는 "(())()" 는 올바른 괄호입니다.
- ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

[제한 조건] 
- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

[풀이 방법]
(인 경우, temp에 저장. 
temp가 존재하고, temp의 마지막이 (이고, )인 경우, pop으로 제거.
그 외의 경우, False를 temp에 저장하고 반복문 break.
temp에 남아 있는 경우, 답은 False.
'''

# 풀이
def solution(s):
    temp = []
    for i in range(len(s)):
        if s[i] == '(':
            temp.append(s[i])
        elif temp and s[i] == ')' and temp[-1] == '(':
            temp.pop()
        else:
            temp.append('False')
            break
    if temp:   
        answer = False
    else:
        answer = True
    return answer