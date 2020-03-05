T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    area = [list(map(int, input().split() for _ in range(H)]
    # 부딪힐 곳 정하기
    # 벽돌 숫자만큼 주위 벽돌 제거
    # 
