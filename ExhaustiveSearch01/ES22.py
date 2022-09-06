# 날짜 : 2022/09/06
# 문제 : 운행되고 있는 시간
# 문제 설명 :
# 회사에서 N명의 개발자가 일을 하고 있습니다. 회사에서는 직원이 한 명이라도 일하고 있으면 ‘운행 되고 있는 시간’이라고 합니다.
# 만약에 N 명중 정확히 한 명을 해고해야 할 때, ‘운행 되고 있는 시간’이 최대가 되도록 하는 프로그램을 작성해보세요.

# 입력 형식 :
# 첫 번째 줄에 정수 N이 주어집니다.
# 두 번째 줄부터는 N개의 줄에 걸쳐 한 줄에 하나씩 각 개발자가 일하는 시간인 A, B가 공백을 사이에 두고 주어집니다.
# 입력으로 주어지는 모든 시간은 전부 유일함을 가정해도 좋습니다.
# 1 ≤ N ≤ 100
# 1 ≤ A < B ≤ 1,000

# 입력 예시 :
# 3
# 5 9
# 1 4
# 3 7

# 출력 예시 :
# 7


MAXTIME = 1000 # 일하는 시간의 최대 범위
n = int(input()) # 개발자 수
worker = [tuple(map(int,input().split())) for _ in range(n)] # n 명의 개발자 정보

ans = 0

for i in range(n):
    workingTime = [0] * (MAXTIME + 1) # 일하는 시간을 기록할 리스트

    for j in range(n):
        if i == j:continue

        start = worker[j][0]
        end = worker[j][1] # 시작과 끝 시간

        for k in range(start,end):
            workingTime[k] += 1

    maxTime = 0

    for j in range(MAXTIME + 1):
        if(workingTime[j] != 0):
            maxTime += 1

    ans = max(ans , maxTime); # 최대 운행 시간 업데이트

print(ans) # 출력