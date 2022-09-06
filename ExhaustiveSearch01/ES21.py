# 날짜 : 2022/09/06
# 문제 : 가장 가까운 두 점 사이의 거리
# 문제 설명 : 2차 평면 상에 n개의 점이 주어졌을 때,
# 가장 가까운 두 점 사이의 거리에 제곱을 한 값을 구하는 프로그램을 작성해보세요.

# 입력 형식 :
# 첫 번째 줄에는 n이 주어집니다.
# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 점의 위치 (x, y) 정보가 공백을 사이에 두고 주어집니다.
# 모든 점의 위치는 다르게 주어짐을 가정해도 좋습니다.
# 2 ≤ n ≤ 100
# 0 ≤ x, y ≤ 1,000

# 입력 예시 :
# 3
# 0 0
# 3 3
# 1 1

# 출력 예시 :
# 2

import sys,math

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)] # n개의 좌표정보 입력 받음

ans = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):

        x1,x2,y1,y2 = arr[i][0],arr[j][0],arr[i][1],arr[j][1]

        dis = int(math.pow(x1 - x2,2) + math.pow(y1 - y2,2)) # 거리 구하기

        ans = min(ans, dis) # 구한 거리를 이용하여 최소값 업데이트

print(ans) # 출력