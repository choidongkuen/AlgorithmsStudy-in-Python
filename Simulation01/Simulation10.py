# 날짜 : 2022/09/11
# 문제 : 연속되는 수 4
# 문제 설명 :
# N개의 숫자들이 주어졌을 때, 증가하는 연속 부분 수열 중 최대 길이를 구하는 프로그램을 작성해보세요. 연속 부분 수열이란, 어떤 수열에서 특정 구간에 속하는 숫자들을 모두 뽑았을 때 나오는 부분 수열을 의미하며,
# 증가하는 연속 부분 수열이란 연속 부분 수열 중 원소의 숫자가 계속 커지는 수열을 뜻합니다.

# 입력 형식 :
# 첫 번째 줄에 N이 주어집니다.
# 두 번째 줄부터 N개의 줄에 걸쳐 각 숫자들이 한 줄에 하나씩 주어집니다.
# 1 ≤ N ≤ 1,000
# 1 ≤ 입력으로 주어지는 숫자 ≤ 1,000

# 입력 예시 :
# 7
# 1
# 5
# 2
# 3
# 5
# 8
# 8

# 출력 예시 :
# 4

n = int(input())
arr = [int(input()) for _ in range(n)]

ans,cnt = 0,1

for i in range(1,n):
    if(arr[i] - arr[i - 1] <= 0):
        ans = max(ans,cnt)
        cnt = 1
    else:
        cnt += 1

ans = max(ans,cnt)
print(ans)