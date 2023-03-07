import sys

input = sys.stdin.readline

n = int(input())
tn = n // 2
selected = [False] * n

s = [list(map(int, input().split())) for _ in range(n)]
minscore = 1e9


# 스타트팀 팀원을 모두 선택 완료한다
# 스타트팀 팀원 인원이 만석이 되면 점수계산을 각각 한다
# 점수차가 min인 것을 기록
def dfs(cnt, start):
    global minscore
    if cnt == tn:
        start = 0
        link = 0
        for i in range(n):
            for j in range(i + 1, n):
                if selected[i] and selected[j]:
                    start = start + s[i][j] + s[j][i]
                elif not selected[i] and not selected[j]:
                    link = link + s[i][j] + s[j][i]
        minscore = min(minscore, abs(start - link))
        if minscore == 0:
            print(0)
            exit()
        return

    for i in range(start, n):
        if not selected[i]:
            selected[i] = True
            dfs(cnt + 1, start + 1)
            selected[i] = False


dfs(0, 0)
print(minscore)