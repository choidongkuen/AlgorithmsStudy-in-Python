# 날짜 : 2022/09/11
# 문제 : 연속되는 수2
# 문제 설명 :
# N개의 숫자들이 주어졌을 때, 연속하여 동일한 숫자가 나오는 횟수 중 최대를 구하는 프로그램을 작성해보세요.

# 입력 형식 :
# 첫 번째 줄에 N이 주어집니다.
# 두 번째 줄부터 N개의 줄에 걸쳐 각 숫자들이 한 줄에 하나씩 주어집니다.
# 1 ≤ N ≤ 1,000
# 0 ≤ 입력으로 주어지는 숫자 ≤ 1,000

# 입력 예시 :
# 7
# 2
# 7
# 7
# 7
# 7
# 5
# 7

# 출력 예시 :
# 4
n = int(input())
arr = [int(input()) for _ in range(n)]

cnt,ans = 1,0

for i in range(1,n):
    if(arr[i] != arr[i-1]):
        ans = max(ans,cnt)
        cnt = 1

    else:
        cnt += 1
ans = max(ans,cnt)
print(ans)



