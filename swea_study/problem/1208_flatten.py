T = 10
for tc in range(T):
    N = int(input())
    boxes = list(map(int, input().split()))
    turn_boxes = [0] * 100

    # 90도 회전(값<->인덱스)
    for box in boxes:
        for i in range(box):
            turn_boxes[i] += 1

    while (N+1):
        # 최대, 최소 위치 찾기
        min_idx, max_idx = 0, 99
        for idx in range(len(turn_boxes)):
            if turn_boxes[idx] != 0:
                max_idx = idx
            if turn_boxes[idx] == 100:
                min_idx = idx + 1

        # 평준화
        turn_boxes[max_idx] -= 1
        turn_boxes[min_idx] += 1
        N -= 1
        if turn_boxes[max_idx] == 0 or turn_boxes[min_idx] == 100:
            continue
    
    print('#{} {}'.format(tc+1, max_idx - min_idx + 1))