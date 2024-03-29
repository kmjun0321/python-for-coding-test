# 4-3 구현 예제
'''
왕실의 나이트
8x8 체스판에서 나이트가 움직일 수 있는 경우의 수 구하라
나이트는 한칸직선 한칸 대각선으로 움직인다. (체스룰)

입력 조건
첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된
문자열이 입력된다. 입력문자는 a1처럼 열과 행으로 이뤄진다.

출력 조건
첫째 줄에 나이트가 이동할 수 있는 겨웅의 수를 출력하시오

입력 예시
a1

출력 예시
2
'''

data = input()

x = data[0]
y = int(data[1])

x = int(ord(x)) - int(ord('a'))+1

result = 8

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for i in range(8):
    ox = x + dx[i]
    oy = y + dy[i]
    if ox < 1 or oy < 1 or ox > 8 or oy > 8:
        result -= 1
        
print(result)